from flask_cors import CORS
from flask import Flask
app = Flask(__name__)
CORS(app)
from flask import Flask, request, jsonify
from supabase import create_client
from dotenv import load_dotenv

import os

# Explicitly load the.env file from current directory
load_dotenv(dotenv_path=".env")

app = Flask(__name__)

# Try loading from env, fallback to hardcoded values for testing
url = os.getenv("SUPABASE_URL") or "https://urfzuurlkhgesdvlyrbm.supabase.co"
key = os.getenv("SUPABASE_KEY") or "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InVyZnp1dXJsa2hnZXNkdmx5cmJtIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTY3OTU4NjEsImV4cCI6MjA3MjM3MTg2MX0.1uPY8H2Bm0lxuPyghnY5mBy9bqqM_WzBdDkfxkDbtu8"

print("Supabase URL:", url)
print("Supabase KEY:", key[:5] + "..." if key else "No key found")

supabase = create_client(url, key)

@app.route('/flashcards', methods=['GET'])
def get_flashcards():
    response = supabase.table("flashcards").select("*").execute()
    return jsonify(response.data)

@app.route('/flashcards', methods=['POST'])
def add_flashcard():
    data = request.json
    response = supabase.table("flashcards").insert({
        "front": data.get("front"),
        "back": data.get("back")
    }).execute()
    return jsonify(response.data), 201

if __name__ == '__main__':
    app.run(debug=True)
    
@app.route("/generate", methods=["POST"])
def generate_flashcards():
    data = request.get_json()
    notes = data.get("notes", "")

    flashcards = []
    for line in notes.split("."):
        question = line.strip()
        if question:
            flashcards.append({
                "front": f"What is: {question}?",
                "back": f"{question} means something important."
            })

    return jsonify({"flashcards": flashcards})



