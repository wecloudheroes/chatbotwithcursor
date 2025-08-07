from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import re
import time
from urllib.parse import quote

load_dotenv()

app = Flask(__name__)
CORS(app)

class ChatBot:
    def __init__(self):
        self.conversation_history = []
    
    def search_google(self, query, num_results=5):
        """Search Google and return formatted results"""
        try:
            # Use requests to search Google (simple approach)
            search_url = f"https://www.google.com/search?q={quote(query)}"
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
            }
            
            response = requests.get(search_url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract search results
            results = []
            search_results = soup.find_all('div', class_='g')
            
            for result in search_results[:num_results]:
                title_elem = result.find('h3')
                link_elem = result.find('a')
                snippet_elem = result.find('span', class_=['aCOpRe', 'st'])
                
                if title_elem and link_elem:
                    title = title_elem.get_text()
                    link = link_elem.get('href', '')
                    snippet = snippet_elem.get_text() if snippet_elem else "No description available"
                    
                    # Clean up the link if it starts with /url?q=
                    if link.startswith('/url?q='):
                        link = link.split('/url?q=')[1].split('&')[0]
                    
                    results.append({
                        'title': title,
                        'link': link,
                        'snippet': snippet
                    })
            
            return results
        except Exception as e:
            print(f"Search error: {e}")
            return []
    
    def generate_response(self, user_message):
        """Generate chatbot response with search integration"""
        self.conversation_history.append({"role": "user", "message": user_message})
        
        # Determine if we need to search
        search_triggers = ['search', 'find', 'look up', 'what is', 'who is', 'how to', 'where is', 'when', 'latest', 'news', 'information about']
        should_search = any(trigger in user_message.lower() for trigger in search_triggers)
        
        if should_search:
            # Perform Google search
            search_results = self.search_google(user_message)
            
            if search_results:
                response = f"I found some information about '{user_message}':\n\n"
                for i, result in enumerate(search_results, 1):
                    response += f"{i}. **{result['title']}**\n"
                    response += f"   {result['snippet']}\n"
                    response += f"   🔗 {result['link']}\n\n"
                
                response += "Is there anything specific you'd like to know more about?"
            else:
                response = f"I couldn't find specific search results for '{user_message}'. Could you try rephrasing your question or being more specific?"
        else:
            # Generate a conversational response
            responses = {
                'hello': "Hello! I'm your AI assistant. I can help you search for information on Google. Just ask me anything!",
                'hi': "Hi there! How can I help you today? I can search for information on any topic.",
                'help': "I'm here to help! You can ask me to search for information about anything. Try asking questions like 'search for Python tutorials' or 'what is machine learning?'",
                'thanks': "You're welcome! Feel free to ask me anything else.",
                'bye': "Goodbye! Have a great day!"
            }
            
            user_lower = user_message.lower().strip()
            response = responses.get(user_lower, 
                "I'm here to help you find information! Try asking me to search for something, or ask questions starting with 'what is', 'how to', 'where is', etc.")
        
        self.conversation_history.append({"role": "assistant", "message": response})
        return response

# Global chatbot instance
chatbot = ChatBot()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Empty message'}), 400
        
        response = chatbot.generate_response(user_message)
        
        return jsonify({
            'response': response,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/search', methods=['POST'])
def search():
    try:
        data = request.get_json()
        query = data.get('query', '').strip()
        
        if not query:
            return jsonify({'error': 'Empty query'}), 400
        
        results = chatbot.search_google(query)
        
        return jsonify({
            'results': results,
            'query': query,
            'status': 'success'
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/history')
def history():
    return jsonify({
        'history': chatbot.conversation_history,
        'status': 'success'
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)