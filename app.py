from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import random
import re
from datetime import datetime

app = Flask(__name__)
CORS(app)

class SimpleChatbot:
    def __init__(self):
        self.responses = {
            'greeting': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Great to see you. How can I assist?",
                "Hello! I'm here to chat. What would you like to talk about?"
            ],
            'goodbye': [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Bye! It was nice chatting with you!",
                "Farewell! Come back anytime!"
            ],
            'how_are_you': [
                "I'm doing great, thank you for asking! How are you?",
                "I'm fantastic! Thanks for checking in. How about you?",
                "I'm wonderful! How has your day been?",
                "I'm doing well! What about you?"
            ],
            'name': [
                "I'm ChatBot, your friendly AI assistant!",
                "You can call me ChatBot. What's your name?",
                "I'm ChatBot! Nice to meet you!",
                "My name is ChatBot. How can I help you today?"
            ],
            'help': [
                "I can chat about various topics! Try asking me about the weather, time, or just say hello!",
                "I'm here to help! You can ask me questions, have a conversation, or just chat casually.",
                "I can assist with basic questions and have friendly conversations. What would you like to know?",
                "Feel free to ask me anything! I can chat about different topics and answer simple questions."
            ],
            'time': [
                f"The current time is {datetime.now().strftime('%H:%M:%S')}",
                f"Right now it's {datetime.now().strftime('%I:%M %p')}",
                f"The time is currently {datetime.now().strftime('%H:%M')}"
            ],
            'weather': [
                "I don't have access to real weather data, but I hope it's nice where you are!",
                "I can't check the weather, but I hope you're having good weather today!",
                "Sorry, I don't have weather information, but I hope it's beautiful outside!"
            ],
            'default': [
                "That's interesting! Tell me more about that.",
                "I see! What else would you like to chat about?",
                "Hmm, that's a good point. What do you think about that?",
                "Interesting! I'd love to hear more of your thoughts.",
                "That's cool! What else is on your mind?",
                "I understand. Is there anything specific you'd like to know or discuss?"
            ]
        }
        
        self.patterns = {
            'greeting': r'\b(hello|hi|hey|greetings|good morning|good afternoon|good evening)\b',
            'goodbye': r'\b(bye|goodbye|see you|farewell|talk to you later|ttyl)\b',
            'how_are_you': r'\b(how are you|how\'re you|how do you do|how are things)\b',
            'name': r'\b(what\'s your name|who are you|what are you called|your name)\b',
            'help': r'\b(help|what can you do|how can you help|assistance)\b',
            'time': r'\b(time|what time|current time|clock)\b',
            'weather': r'\b(weather|temperature|rain|sunny|cloudy|forecast)\b'
        }
    
    def get_response(self, message):
        message = message.lower().strip()
        
        # Check each pattern
        for intent, pattern in self.patterns.items():
            if re.search(pattern, message):
                return random.choice(self.responses[intent])
        
        # Default response
        return random.choice(self.responses['default'])

# Initialize chatbot
chatbot = SimpleChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        bot_response = chatbot.get_response(user_message)
        
        return jsonify({
            'response': bot_response,
            'timestamp': datetime.now().isoformat()
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health():
    return jsonify({'status': 'healthy', 'message': 'Chatbot is running!'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)