# AI Search Chatbot 🤖

A modern, responsive web application that combines an AI chatbot with Google search functionality. The chatbot can understand user queries and automatically perform web searches to provide relevant, up-to-date information.

![AI Search Chatbot](https://img.shields.io/badge/Python-3.8+-blue.svg) ![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## ✨ Features

- **Intelligent Chatbot**: Responds to user queries with contextual understanding
- **Google Search Integration**: Automatically searches Google for relevant information
- **Modern UI**: Beautiful, responsive design with smooth animations
- **Real-time Chat**: Interactive chat interface with typing indicators
- **Search Results**: Formatted search results with clickable links
- **Mobile Responsive**: Works perfectly on desktop and mobile devices
- **Suggestion Chips**: Quick-start suggestions for common queries

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project**
   ```bash
   cd /workspace
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Open your browser**
   Navigate to `http://localhost:5000` to start chatting!

## 🛠️ Usage

### Basic Chat
- Type any message in the chat input
- The bot will respond conversationally for general queries

### Search Functionality
The bot automatically triggers Google search when you use phrases like:
- "search for..."
- "what is..."
- "how to..."
- "find information about..."
- "latest news on..."

### Example Queries
Try these example queries:
- "What is artificial intelligence?"
- "How to learn Python programming"
- "Latest news about technology"
- "Best restaurants near me"

## 📁 Project Structure

```
/workspace/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── .env                  # Environment configuration
├── README.md             # This file
├── templates/
│   └── index.html        # Main HTML template
└── static/
    ├── css/
    │   └── style.css     # Stylesheet
    └── js/
        └── script.js     # JavaScript functionality
```

## 🔧 Configuration

### Environment Variables
Edit the `.env` file to customize settings:

```env
FLASK_ENV=development
FLASK_DEBUG=True
SEARCH_RESULTS_LIMIT=5
REQUEST_TIMEOUT=10
```

### Search Configuration
The application uses web scraping to search Google. For production use, consider:

1. **Google Custom Search API** (Recommended for production)
   - Get API key from Google Cloud Console
   - Create Custom Search Engine
   - Add credentials to `.env` file

2. **Rate Limiting**
   - The current implementation includes basic rate limiting
   - Consider adding more robust rate limiting for production

## 🎨 Customization

### Styling
- Modify `static/css/style.css` to change the appearance
- The design uses CSS Grid and Flexbox for responsive layout
- Color scheme can be easily modified by changing CSS variables

### Search Triggers
Edit the `search_triggers` list in `app.py` to customize when searches are triggered:

```python
search_triggers = ['search', 'find', 'look up', 'what is', 'who is', 'how to']
```

### Response Templates
Modify the `responses` dictionary in `app.py` to customize bot responses:

```python
responses = {
    'hello': "Your custom greeting here!",
    'help': "Your custom help message here!"
}
```

## 📱 API Endpoints

The application provides REST API endpoints:

### POST /chat
Send a message to the chatbot
```json
{
  "message": "Your message here"
}
```

### POST /search
Perform a direct Google search
```json
{
  "query": "Your search query"
}
```

### GET /history
Get conversation history
```json
{
  "history": [...],
  "status": "success"
}
```

## 🔒 Security Considerations

- The application uses web scraping which may be subject to rate limiting
- Consider implementing user authentication for production use
- Add input validation and sanitization
- Use HTTPS in production
- Consider implementing CSRF protection

## 🐛 Troubleshooting

### Common Issues

1. **Search not working**
   - Check internet connection
   - Google may be rate limiting requests
   - Try different search queries

2. **Styling issues**
   - Clear browser cache
   - Check if CSS files are loading correctly

3. **Port already in use**
   - Change the port in `app.py`: `app.run(port=5001)`

### Error Messages
- Check browser console for JavaScript errors
- Check terminal output for Python errors
- Verify all dependencies are installed

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Flask framework for the backend
- Font Awesome for icons
- Google Fonts for typography
- Beautiful Soup for web scraping

## 📞 Support

If you encounter any issues or have questions:

1. Check the troubleshooting section above
2. Review the code comments for implementation details
3. Test with different browsers
4. Ensure all dependencies are correctly installed

---

**Happy Chatting! 🎉**