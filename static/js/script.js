class ChatBot {
    constructor() {
        this.chatMessages = document.getElementById('chatMessages');
        this.messageInput = document.getElementById('messageInput');
        this.sendButton = document.getElementById('sendButton');
        this.typingIndicator = document.getElementById('typingIndicator');
        
        this.init();
    }

    init() {
        // Event listeners
        this.sendButton.addEventListener('click', () => this.sendMessage());
        this.messageInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
                e.preventDefault();
                this.sendMessage();
            }
        });

        // Focus on input
        this.messageInput.focus();
    }

    addMessage(content, isUser = false, isHTML = false) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${isUser ? 'user-message' : 'bot-message'}`;

        const avatarDiv = document.createElement('div');
        avatarDiv.className = `message-avatar ${isUser ? 'user-avatar' : 'bot-avatar'}`;
        avatarDiv.innerHTML = isUser ? '<i class="fas fa-user"></i>' : '<i class="fas fa-robot"></i>';

        const contentDiv = document.createElement('div');
        contentDiv.className = 'message-content';
        
        if (isHTML) {
            contentDiv.innerHTML = this.formatMessage(content);
        } else {
            contentDiv.textContent = content;
        }

        messageDiv.appendChild(avatarDiv);
        messageDiv.appendChild(contentDiv);
        
        // Insert before typing indicator if it exists
        if (this.typingIndicator.style.display !== 'none') {
            this.chatMessages.insertBefore(messageDiv, this.typingIndicator);
        } else {
            this.chatMessages.appendChild(messageDiv);
        }

        this.scrollToBottom();
    }

    formatMessage(content) {
        // Convert URLs to clickable links
        const urlRegex = /(https?:\/\/[^\s]+)/g;
        let formatted = content.replace(urlRegex, '<a href="$1" target="_blank" rel="noopener noreferrer">$1</a>');
        
        // Convert markdown-like bold text
        formatted = formatted.replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>');
        
        // Convert newlines to HTML breaks
        formatted = formatted.replace(/\n/g, '<br>');
        
        return formatted;
    }

    showTypingIndicator() {
        this.typingIndicator.style.display = 'block';
        this.scrollToBottom();
    }

    hideTypingIndicator() {
        this.typingIndicator.style.display = 'none';
    }

    scrollToBottom() {
        this.chatMessages.scrollTop = this.chatMessages.scrollHeight;
    }

    setInputState(disabled) {
        this.messageInput.disabled = disabled;
        this.sendButton.disabled = disabled;
        
        if (!disabled) {
            this.messageInput.focus();
        }
    }

    async sendMessage(message = null) {
        const userMessage = message || this.messageInput.value.trim();
        if (!userMessage) return;

        // Add user message to chat
        this.addMessage(userMessage, true);
        this.messageInput.value = '';

        // Disable input
        this.setInputState(true);
        this.showTypingIndicator();

        try {
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: userMessage })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            
            // Simulate typing delay for better UX
            setTimeout(() => {
                this.hideTypingIndicator();
                this.addMessage(data.response, false, true);
                this.setInputState(false);
            }, 800);

        } catch (error) {
            console.error('Error:', error);
            setTimeout(() => {
                this.hideTypingIndicator();
                this.addMessage('Sorry, I encountered an error while processing your request. Please try again.', false);
                this.setInputState(false);
            }, 500);
        }
    }

    async searchGoogle(query) {
        try {
            const response = await fetch('/search', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ query: query })
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const data = await response.json();
            return data;

        } catch (error) {
            console.error('Search error:', error);
            return { error: 'Failed to perform search' };
        }
    }
}

// Suggestion functionality
function sendSuggestion(suggestion) {
    if (window.chatBot) {
        window.chatBot.sendMessage(suggestion);
    }
}

// Initialize chatbot when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    window.chatBot = new ChatBot();
    
    // Add welcome animation
    setTimeout(() => {
        const welcomeMessages = document.querySelectorAll('.bot-message');
        welcomeMessages.forEach((msg, index) => {
            msg.style.opacity = '0';
            msg.style.transform = 'translateY(20px)';
            setTimeout(() => {
                msg.style.transition = 'all 0.5s ease';
                msg.style.opacity = '1';
                msg.style.transform = 'translateY(0)';
            }, index * 200);
        });
    }, 100);
});

// Service Worker for offline functionality (optional)
if ('serviceWorker' in navigator) {
    window.addEventListener('load', function() {
        navigator.serviceWorker.register('/static/js/sw.js')
            .then(function(registration) {
                console.log('ServiceWorker registration successful');
            }, function(err) {
                console.log('ServiceWorker registration failed: ', err);
            });
    });
}