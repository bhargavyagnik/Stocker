import requests

def call_perplexity_chat(api_key, prompt):
  """
  Calls the Perplexity.ai chat API and returns the response.

  Args:
      api_key: Your Perplexity.ai API key.
      prompt: A list of dictionaries representing the conversation history.

  Returns:
      A dictionary containing the response from the API.
  """

  url = "https://api.perplexity.ai/chat/completions"

  payload = {
      "model": "llama-3.1-sonar-small-128k-online",
      "messages": prompt,
      "max_tokens": "Optional",
      "temperature": 0.2,
      "top_p": 0.9,
      "return_citations": True,
      "search_domain_filter": ["perplexity.ai"],
      "return_images": False,
      "return_related_questions": False,
      "search_recency_filter": "month",
      "top_k": 0,
      "stream": False,
      "presence_penalty": 0,
      "frequency_penalty": 1
  }

  headers = {
      "Authorization": f"Bearer {api_key}",
      "Content-Type": "application/json"
  }

  response = requests.post(url, json=payload, headers=headers)

  # Check for successful response
  if response.status_code == 200:
    return response.json()
  else:
    raise Exception(f"Error: {response.status_code}, {response.text}")

# Example usage
if __name__ == "__main__":
  your_api_key = "YOUR_PERPLEXITY_API_KEY"  # Replace with your actual key
  prompt = [
      {
          "role": "system",
          "content": "Be precise and concise."
      },
      {
          "role": "user",
          "content": "Todays financial news, list 5 news that could impact stock market. return as a text script of a news anchor"
      }
  ]

  response = call_perplexity_chat(your_api_key, prompt)
  print(response)