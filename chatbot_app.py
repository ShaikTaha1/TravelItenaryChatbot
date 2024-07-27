import streamlit as st
import weaviate
import time
import openai
from sklearn.metrics import precision_score, recall_score, f1_score

# Connect to Weaviate
client = weaviate.Client("http://localhost:8080")  # Adjust the URL to your Weaviate instance

# Set up OpenAI API key
openai.api_key = 'OPEN AI API KEY'  # Replace with your actual OpenAI API key

def query_weaviate(question):
    query = """
    {
        Get {
            Article(where: {
                path: ["title"],
                operator: Equal,
                valueText: "%s"
            }) {
                title
                content
            }
        }
    }
    """ % question

    response = client.query.raw(query)
    if 'data' in response:
        return response['data']['Get']['Article']
    else:
        st.error(f"Query failed: {response.get('errors', 'Unknown error')}")
        return []

def query_openai(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question}
        ],
        max_tokens=150
    )
    return response.choices[0].message['content'].strip()

def store_response_in_weaviate(question, answer):
    properties = {
        "title": question,
        "content": answer
    }
    client.data_object.create(
        properties,
        class_name="Article"
    )

def calculate_metrics(y_true, y_pred):
    precision = precision_score(y_true, y_pred, average='binary', zero_division=0)
    recall = recall_score(y_true, y_pred, average='binary', zero_division=0)
    f1 = f1_score(y_true, y_pred, average='binary', zero_division=0)
    return precision * 100, recall * 100, f1 * 100  # Convert to percentage

def main():
    st.title("Travel Itinerary Chatbot")

    if "responses" not in st.session_state:
        st.session_state.responses = []

    if "y_true" not in st.session_state:
        st.session_state.y_true = []
        st.session_state.y_pred_weaviate = []
        st.session_state.y_pred_openai = []

    user_input = st.text_input("Ask a question about travel itineraries:")

    if st.button("Submit"):
        start_time = time.time()
        weaviate_response = query_weaviate(user_input)
        weaviate_time = time.time()

        weaviate_answer = None
        openai_answer = None

        if weaviate_response:
            weaviate_answer = weaviate_response[0]['content']
            response_text = f"**Weaviate Response:** {weaviate_answer}"
            st.session_state.y_pred_weaviate.append(1)
            st.session_state.y_pred_openai.append(0)  # No OpenAI needed if Weaviate has answer
        else:
            st.session_state.y_pred_weaviate.append(0)

            openai_start_time = time.time()
            openai_answer = query_openai(user_input)
            openai_end_time = time.time()

            # Store OpenAI response in Weaviate
            store_response_in_weaviate(user_input, openai_answer)

            response_text = f"**OpenAI Response:** {openai_answer}"
            st.session_state.y_pred_openai.append(1)

        # Store the response and user query
        st.session_state.responses.insert(0, f"**User Query:** {user_input}\n{response_text}")

        # Display all responses with the latest response at the top
        for response in st.session_state.responses:
            st.write(response)

        # Calculate metrics
        y_true = [1] * len(st.session_state.y_pred_weaviate)  # Assuming all responses are relevant
        weaviate_response_time = weaviate_time - start_time
        openai_response_time = (openai_end_time - openai_start_time) if openai_answer else None

        st.write("Weaviate Response Time:", weaviate_response_time, "seconds")
        if openai_response_time:
            st.write("OpenAI Response Time:", openai_response_time, "seconds")

        precision_weaviate, recall_weaviate, f1_weaviate = calculate_metrics(y_true, st.session_state.y_pred_weaviate)
        st.write(f"Weaviate Precision: {precision_weaviate:.2f}%")
        st.write(f"Weaviate Recall: {recall_weaviate:.2f}%")
        st.write(f"Weaviate F1 Score: {f1_weaviate:.2f}%")

        if openai_answer:
            precision_openai, recall_openai, f1_openai = calculate_metrics(y_true, st.session_state.y_pred_openai)
            st.write(f"OpenAI Precision: {precision_openai:.2f}%")
            st.write(f"OpenAI Recall: {recall_openai:.2f}%")
            st.write(f"OpenAI F1 Score: {f1_openai:.2f}%")

if __name__ == "__main__":
    main()
