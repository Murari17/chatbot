from flask import Flask, render_template, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

# Configure the API key
GOOGLE_API_KEY = "AIzaSyD-GdR0hLwT5h9BttAdGIER6RNPh44ntr0"  # Your actual Google API key
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat_with_bot():
    data = request.get_json()
    user_message = data.get('message')

    # Send the user message to the chatbot model and get the response
    response = chat.send_message(user_message, stream=True)
    
    reply = ""
    for chunk in response:
        if chunk.text:
            reply += chunk.text

    # Return the chatbot's response as a JSON object
    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
