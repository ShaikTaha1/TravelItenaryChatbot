Youtube Link: https://youtu.be/rvDLmLyWyDY

![image](https://github.com/user-attachments/assets/a959e50f-c6ba-4139-8522-8901e237d52b)


# TravelItenaryChatbot
Travel Itenary Chatbot with recommends destination places based on the user input and also shows its metric score


The application is a chatbot system designed to provide users with travel itinerary information. It integrates Weaviate, a vector search engine, and OpenAI's language models to deliver relevant responses to user queries. The application evaluates the quality of its responses using performance metrics and continuously improves by storing and reusing responses.

Certainly! Here’s a summary of the Streamlit application code, including the libraries used, how to use the application, and its overall functionality:

---

## Application Summary

### **1. Libraries Used**

1. **`streamlit`**: For building the web application interface.
   - **Installation**: `pip install streamlit`
2. **`weaviate-client`**: For interacting with the Weaviate vector search engine.
   - **Installation**: `pip install weaviate-client`
3. **`openai`**: For querying OpenAI's language models.
   - **Installation**: `pip install openai`
4. **`scikit-learn`**: For calculating performance metrics (Precision, Recall, F1 Score).
   - **Installation**: `pip install scikit-learn`

### **2. Application Overview**

The application integrates Weaviate and OpenAI to provide responses to user queries about travel itineraries. It also calculates and displays performance metrics to evaluate the effectiveness of the responses.

#### **2.1. Functionality**

1. **User Query Input**:
   - Users can input queries related to travel itineraries into the text input field provided by Streamlit.

2. **Response Retrieval**:
   - **Weaviate Query**: The application first queries the Weaviate vector database for a relevant response.
     - If a relevant response is found, it is displayed and used for metric calculation.
     - If no response is found, the application falls back to querying OpenAI.
   - **OpenAI Query**: If Weaviate does not have a relevant response, the application uses OpenAI’s API to generate a response.
     - This response is then stored in Weaviate for future queries.

3. **Metric Calculation**:
   - **Metrics Calculated**: Precision, Recall, and F1 Score are calculated for both Weaviate and OpenAI responses.
     - These metrics help evaluate the relevance and quality of the responses.
   - **Metric Display**: The calculated metrics are displayed alongside the responses.

4. **Response Management**:
   - Responses are displayed with the most recent query and response at the top of the list.
   - Previous responses include the user’s query for context.

5. **Response Storage**:
   - OpenAI responses are stored in Weaviate to ensure that future queries on similar topics can retrieve answers from the database instead of generating new ones.

### **3. How to Use the Application**

1. **Setup**:
   - Ensure that Weaviate is running and accessible at the specified URL.
   - Replace `'YOUR_OPENAI_API_KEY'` with your actual OpenAI API key.

2. **Running the Application**:
   - Save the code in a file named `chatbot_app.py`.
   - Run the application using Streamlit:
     ```sh
     streamlit run chatbot_app.py
     ```

3. **Interacting with the Application**:
   - Enter a travel-related question in the text input field and click "Submit."
   - The application will first try to retrieve a response from Weaviate.
   - If Weaviate does not have an answer, it will use OpenAI to generate one and store it in Weaviate.
   - The response, along with the calculated metrics, will be displayed on the screen.

### **4. Code Summary**

The code is organized as follows:

1. **Imports and Configuration**:
   - Import necessary libraries and configure connections to Weaviate and OpenAI.

2. **Function Definitions**:
   - `query_weaviate(question)`: Queries Weaviate for a relevant response.
   - `query_openai(question)`: Queries OpenAI for a response if Weaviate does not have one.
   - `store_response_in_weaviate(question, answer)`: Stores the OpenAI response in Weaviate.
   - `calculate_metrics(true_labels, predictions)`: Calculates Precision, Recall, and F1 Score.

3. **Main Function**:
   - Handles user input, queries, response management, metric calculation, and display.
   - Manages state using `st.session_state` to keep track of responses and metrics.

This summary provides an overview of the application’s functionality, the libraries used, and instructions on how to use it effectively.

Certainly! Here’s a detailed report based on the Streamlit application that integrates Weaviate and OpenAI for querying and metric calculations:

---

## Detailed Report: Chatbot Performance Evaluation and Improvement

### 1. **Methodology for Calculating Metrics**

#### **1.1. Precision**
- **Definition**: Precision measures the accuracy of positive predictions. It is the ratio of true positive predictions to the sum of true positive and false positive predictions.
- **Formula**: 
  \[
  \text{Precision} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Positives}}
  \]
- **Implementation**: In our case, the positive predictions are considered when the chatbot provides a relevant response.

#### **1.2. Recall**
- **Definition**: Recall measures the ability of the model to identify all relevant instances. It is the ratio of true positive predictions to the sum of true positives and false negatives.
- **Formula**: 
  \[
  \text{Recall} = \frac{\text{True Positives}}{\text{True Positives} + \text{False Negatives}}
  \]
- **Implementation**: This metric reflects the chatbot's ability to retrieve relevant responses from the database or generate useful answers when querying OpenAI.

#### **1.3. F1 Score**
- **Definition**: The F1 Score is the harmonic mean of Precision and Recall. It provides a single metric that balances both concerns.
- **Formula**: 
  \[
  \text{F1 Score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}
  \]
- **Implementation**: F1 Score combines the Precision and Recall into one metric, providing a comprehensive view of performance.

### 2. **Results Obtained for Each Metric**

#### **2.1. Precision, Recall, and F1 Score for Weaviate**
- **Precision**: Calculated based on how many times Weaviate returned a relevant response out of all responses provided.
- **Recall**: Evaluated based on how many relevant responses Weaviate was able to retrieve from the database.
- **F1 Score**: Combined measure of Precision and Recall.

#### **2.2. Precision, Recall, and F1 Score for OpenAI**
- **Precision**: Determined by the relevance of responses generated by OpenAI when Weaviate did not provide an answer.
- **Recall**: Measures how well OpenAI’s responses cover the range of possible relevant responses.
- **F1 Score**: Aggregated measure of Precision and Recall for OpenAI responses.

### 3. **Methods Proposed and Implemented for Improvement**

#### **3.1. Improved Response Handling**
- **Initial Approach**: Initially, responses were directly compared and displayed without a metric-based assessment.
- **Improvement**: Introduced metric-based evaluation (Precision, Recall, F1 Score) to assess and compare responses from Weaviate and OpenAI.

#### **3.2. Storing OpenAI Responses in Weaviate**
- **Initial Approach**: OpenAI responses were not utilized for future queries.
- **Improvement**: Implemented functionality to store OpenAI responses in Weaviate, ensuring that future queries can retrieve responses from the database instead of generating new answers.

#### **3.3. Enhanced Metric Calculation**
- **Initial Approach**: Metrics were either 0% or 100% due to incorrect handling of predictions and true labels.
- **Improvement**: Corrected the calculation of metrics to provide precise values between 0% and 100%, ensuring accurate performance evaluation.

### 4. **Comparative Analysis Before and After Improvements**

#### **4.1. Before Improvements**
- **Response Handling**: Responses were either from Weaviate or OpenAI, without considering performance metrics.
- **Metric Calculation**: Metrics were either 0% or 100% due to improper length matching of true labels and predictions.
- **Response Storage**: No mechanism to store and reuse OpenAI responses.

#### **4.2. After Improvements**
- **Response Handling**: Responses are now evaluated based on Precision, Recall, and F1 Score, with the best response being displayed.
- **Metric Calculation**: Metrics are now calculated correctly with values ranging between 0% and 100%, providing a more accurate performance assessment.
- **Response Storage**: OpenAI responses are stored in Weaviate for future use, improving efficiency and consistency in response retrieval.

### 5. **Challenges Faced and How They Were Addressed**

#### **5.1. Challenge: Inconsistent Metric Values**
- **Issue**: The initial metric calculations resulted in binary values (0% or 100%).
- **Solution**: Implemented correct metric calculations and ensured consistency in the length of `y_true` and `y_pred`.

#### **5.2. Challenge: Handling Missing Responses**
- **Issue**: If Weaviate did not provide a response, the metrics could not be calculated.
- **Solution**: Added a fallback to OpenAI and implemented logic to store OpenAI responses in Weaviate for future queries.

#### **5.3. Challenge: Displaying New Responses First**
- **Issue**: New responses were displayed at the bottom of the list.
- **Solution**: Updated the Streamlit app to display new responses at the top, ensuring that the most recent responses are always visible.

---


