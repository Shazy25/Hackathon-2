import requests

url = "http://127.0.0.1:5000/flashcards"

# POST a new flashcard
response = requests.post(url, json={"front": "What is the capital of Kenya?", "back": "Nairobi"})
print("POST response:", response.status_code, response.json())

# GET all flashcards
response = requests.get(url)
print("GET response:", response.status_code, response.json())

