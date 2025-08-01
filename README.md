# Simple Chatbot

A modern, responsive web-based chatbot built with Flask (Python backend) and vanilla JavaScript (frontend). This chatbot features a beautiful UI with smooth animations and can respond to various user inputs using pattern matching.

## Features

- 🤖 **Intelligent Responses**: Pattern-based response system for natural conversations
- 💬 **Real-time Chat**: Instant messaging with typing indicators
- 📱 **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- 🎨 **Modern UI**: Beautiful gradient design with smooth animations
- ⚡ **Fast Performance**: Lightweight and optimized for speed
- 🔧 **Easy to Extend**: Simple to add new response patterns and intents

## What the Chatbot Can Do

The chatbot can respond to various types of messages:

- **Greetings**: "Hello", "Hi", "Hey", "Good morning", etc.
- **Farewells**: "Goodbye", "Bye", "See you later", etc.
- **Personal Questions**: "How are you?", "What's your name?", etc.
- **Help Requests**: "Help", "What can you do?", etc.
- **Time Queries**: "What time is it?", "Current time", etc.
- **Weather Questions**: Basic weather responses (mock data)
- **General Conversation**: Engaging default responses for other topics

## Project Structure

```
chatbot/
├── app.py                 # Flask backend application
├── requirements.txt       # Python dependencies
├── templates/
│   └── index.html        # Main HTML template
├── static/
│   ├── css/
│   │   └── style.css     # Stylesheet
│   └── js/
│       └── script.js     # Frontend JavaScript
└── README.md             # This file
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. **Clone or download the project files** to your local machine

2. **Navigate to the project directory**:
   ```bash
   cd chatbot
   ```

3. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows:
   venv\Scripts\activate
   
   # On macOS/Linux:
   source venv/bin/activate
   ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your web browser** and go to:
   ```
   http://localhost:5000
   ```

## Usage

1. **Start the server** by running `python app.py`
2. **Open your browser** to `http://localhost:5000`
3. **Type a message** in the input field at the bottom
4. **Press Enter** or click the send button to send your message
5. **Wait for the bot's response** (indicated by typing animation)

### Example Conversations

```
You: Hello!
Bot: Hello! How can I help you today?

You: What's your name?
Bot: I'm ChatBot, your friendly AI assistant!

You: What time is it?
Bot: The current time is 14:30:25

You: How are you?
Bot: I'm doing great, thank you for asking! How are you?
```

## Customization

### Adding New Response Patterns

To add new conversation topics, edit the `SimpleChatbot` class in `app.py`:

1. **Add new responses** to the `self.responses` dictionary
2. **Add corresponding patterns** to the `self.patterns` dictionary

Example:
```python
# In the responses dictionary:
'jokes': [
    "Why don't scientists trust atoms? Because they make up everything!",
    "I told my wife she was drawing her eyebrows too high. She looked surprised!"
]

# In the patterns dictionary:
'jokes': r'\b(joke|funny|humor|laugh)\b'
```

### Styling Customization

- Edit `static/css/style.css` to change colors, fonts, and layout
- The design uses CSS custom properties for easy theme customization
- All animations and transitions can be modified in the CSS file

### Frontend Functionality

- Edit `static/js/script.js` to add new frontend features
- The JavaScript is modular and easy to extend
- Add new keyboard shortcuts, UI interactions, or API calls

## API Endpoints

- `GET /` - Serves the main chat interface
- `POST /api/chat` - Processes chat messages and returns bot responses
- `GET /api/health` - Health check endpoint

### API Usage Example

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello"}'
```

Response:
```json
{
  "response": "Hello! How can I help you today?",
  "timestamp": "2024-01-15T14:30:25.123456"
}
```

## Development

### Running in Development Mode

The Flask app runs in debug mode by default, which means:
- Automatic reloading when you make changes
- Detailed error messages
- Development server warnings

### Production Deployment

For production deployment, consider:
- Using a production WSGI server like Gunicorn
- Setting up environment variables for configuration
- Adding proper logging and error handling
- Implementing rate limiting and security measures

## Troubleshooting

### Common Issues

1. **Port already in use**: If port 5000 is busy, change the port in `app.py`:
   ```python
   app.run(debug=True, host='0.0.0.0', port=8000)
   ```

2. **Module not found errors**: Make sure you've activated your virtual environment and installed dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Browser cache issues**: Hard refresh your browser (Ctrl+F5 or Cmd+Shift+R) to clear cached files

### Getting Help

If you encounter any issues:
1. Check the console output for error messages
2. Verify all dependencies are installed correctly
3. Ensure Python 3.7+ is being used
4. Check that all files are in the correct directory structure

## Future Enhancements

Potential improvements you could add:
- Database integration for conversation history
- User authentication and personalization
- Integration with external APIs (weather, news, etc.)
- Natural Language Processing with libraries like NLTK or spaCy
- Voice input/output capabilities
- Multi-language support
- Admin panel for managing responses

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this project and submit pull requests for any improvements!