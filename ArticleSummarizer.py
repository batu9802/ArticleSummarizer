import requests

class ArticleSummarizer:
    def __init__(self, api_key):
        self.api_key = api_key
        self.endpoint = "https://api.openai.com/v1/engines/davinci-codex/completions"

    def summarize(self, article_text):
        # Define the API parameters
        params = {
            "prompt": f"summarize: {article_text}",
            "max_tokens": 100,
            "stop": "."
        }

        # Define the headers
        headers = {"Content-Type": "application/json", "Authorization": f"Bearer {self.api_key}"}

        # Make the API request
        response = requests.post(self.endpoint, json=params, headers=headers)

        # Extract the summary from the response
        summary = response.text

        # Return the summary
        return summary

# Define the API key
api_key = "api_key"

# Create an instance of the ArticleSummarizer class
summarizer = ArticleSummarizer(api_key)

# Define the article text
article_text = "Article text goes here."

# Generate a summary of the article
summary = summarizer.summarize(article_text)

# Print the summary
print(summary)
