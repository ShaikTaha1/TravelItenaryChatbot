import weaviate

client = weaviate.Client("http://localhost:8080")  # Adjust the URL to your Weaviate instance

# Load the schema from the JSON file
schema = {
    "classes": [
        {
            "class": "Article",
            "description": "A class representing travel articles",
            "properties": [
                {
                    "name": "title",
                    "description": "The title of the article",
                    "dataType": ["string"]
                },
                {
                    "name": "content",
                    "description": "The content of the article",
                    "dataType": ["string"]
                }
            ]
        }
    ]
}

client.schema.create(schema)
