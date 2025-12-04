from flask import Flask, render_template, request, jsonify
from chatbot import AdmissionChatbot

app = Flask(__name__)
bot = AdmissionChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Handle chat messages."""
    data = request.get_json()
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'response': 'Please enter a message.'})
    
    # Get bot response
    bot_response = bot.get_response(user_message)
    
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
