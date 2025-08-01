from flask import Flask, render_template, request, jsonify
from chatbot import SimpleChatbot

app = Flask(__name__)
bot = SimpleChatbot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    bot_response = bot.get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)