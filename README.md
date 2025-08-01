# Simple Chatbot

A simple rule-based chatbot built with Python that doesn't require OpenAI or any external AI APIs. The chatbot uses pattern matching and predefined responses to have conversations with users.

## Features

- 🤖 Rule-based conversation system
- 🌐 Beautiful web interface
- 💬 Command-line interface
- 📱 Mobile-responsive design
- ⏰ Time and date queries
- 🎯 Pattern matching for natural responses
- 🎨 Modern UI with typing indicators

## Installation

1. Clone or download this repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### Web Interface (Recommended)

1. Start the web server:

```bash
python app.py
```

2. Open your browser and go to `http://localhost:5000`
3. Start chatting with the bot!

### Command Line Interface

Run the chatbot directly in your terminal:

```bash
python chatbot.py
```

Type your messages and press Enter. Type 'quit', 'exit', or 'q' to stop the conversation.

## What the Chatbot Can Do

The chatbot can respond to various types of messages:

- **Greetings**: "Hi", "Hello", "Hey"
- **Time queries**: "What time is it?", "Current time"
- **Date queries**: "What's the date?", "Today's date"
- **Name questions**: "What's your name?", "Who are you?"
- **How are you**: "How are you doing?"
- **Help**: "What can you do?", "Help"
- **Thanks**: "Thank you", "Thanks"
- **Goodbyes**: "Bye", "Goodbye", "See you"
- **Yes/No responses**: "Yes", "No", "Okay"
- **Compliments**: "You're awesome", "You're good"
- **General conversation**: The bot will try to keep the conversation going

## Example Conversations

```
You: Hello!
SimpleBot: Hi there! What's on your mind?

You: What time is it?
SimpleBot: The current time is 14:30:25

You: How are you?
SimpleBot: I'm doing great, thank you for asking!

You: What can you do?
SimpleBot: I can chat with you! Try asking me about the time, date, or just have a conversation!

You: You're awesome!
SimpleBot: Thank you! That's very kind of you to say!
```

## Customization

You can easily customize the chatbot by editing the `patterns` dictionary in `chatbot.py`:

1. Add new regex patterns as keys
2. Add corresponding response lists as values
3. The bot will randomly select from the response list when a pattern matches

Example of adding a new pattern:

```python
# Add to the patterns dictionary
r'(?i).*(favorite.*color|what color).*': [
    "I like blue! It's calming and peaceful.",
    "Blue is my favorite color. What's yours?",
    "I'm partial to blue, like the sky!"
]
```

## File Structure

```
├── chatbot.py          # Main chatbot logic
├── app.py              # Flask web application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── templates/
    └── index.html     # Web interface template
```

## Technical Details

- **Backend**: Python with Flask
- **Frontend**: HTML, CSS, JavaScript
- **Pattern Matching**: Regular expressions (regex)
- **Response Selection**: Random selection from predefined lists
- **No AI APIs**: Completely self-contained, no external dependencies

## Browser Compatibility

The web interface works on:
- Chrome/Chromium
- Firefox
- Safari
- Edge
- Mobile browsers

## Contributing

Feel free to add more patterns, improve responses, or enhance the UI! The chatbot is designed to be easily extensible.

## License

This project is open source and available under the MIT License.