import re
import random
from datetime import datetime

class SimpleChatbot:
    def __init__(self):
        self.name = "SimpleBot"
        self.patterns = {
            # Greetings
            r'(?i)^(hi|hello|hey|greetings?).*': [
                "Hello! How can I help you today?",
                "Hi there! What's on your mind?",
                "Hey! Nice to meet you!",
                "Greetings! How are you doing?"
            ],
            
            # How are you
            r'(?i).*(how are you|how\'re you).*': [
                "I'm doing great, thank you for asking!",
                "I'm fine, thanks! How about you?",
                "I'm good! Ready to chat with you!",
                "Doing well! What about yourself?"
            ],
            
            # Name questions
            r'(?i).*(what.*your name|who are you).*': [
                f"I'm {self.name}, your friendly chatbot!",
                f"My name is {self.name}. Nice to meet you!",
                f"I'm {self.name}, here to chat with you!"
            ],
            
            # Time questions
            r'(?i).*(what.*time|current time).*': [
                f"The current time is {datetime.now().strftime('%H:%M:%S')}",
                f"Right now it's {datetime.now().strftime('%I:%M %p')}"
            ],
            
            # Date questions
            r'(?i).*(what.*date|today\'s date|what day).*': [
                f"Today is {datetime.now().strftime('%B %d, %Y')}",
                f"The date today is {datetime.now().strftime('%Y-%m-%d')}"
            ],
            
            # Weather (mock responses since we don't have API)
            r'(?i).*(weather|temperature|hot|cold|rain).*': [
                "I don't have access to real weather data, but I hope it's nice where you are!",
                "I can't check the weather, but I hope you're having a pleasant day!",
                "Sorry, I don't have weather information. Maybe check your local weather app?"
            ],
            
            # Help
            r'(?i).*(help|what can you do).*': [
                "I can chat with you! Try asking me about the time, date, or just have a conversation!",
                "I'm here to chat! Ask me questions or just talk to me about anything!",
                "I can help with basic conversation. Ask me about myself, the time, or just chat!"
            ],
            
            # Thanks
            r'(?i).*(thank you|thanks|thx).*': [
                "You're welcome!",
                "No problem!",
                "Happy to help!",
                "My pleasure!"
            ],
            
            # Goodbye
            r'(?i).*(bye|goodbye|see you|farewell).*': [
                "Goodbye! Have a great day!",
                "See you later! Take care!",
                "Bye! It was nice chatting with you!",
                "Farewell! Come back anytime!"
            ],
            
            # Yes/No responses
            r'(?i)^(yes|yeah|yep|sure|ok|okay)$': [
                "Great!",
                "Awesome!",
                "Sounds good!",
                "Perfect!"
            ],
            
            r'(?i)^(no|nope|nah)$': [
                "I understand.",
                "No problem!",
                "That's okay!",
                "Fair enough!"
            ],
            
            # Compliments
            r'(?i).*(you.*good|you.*great|you.*awesome|you.*cool).*': [
                "Thank you! That's very kind of you to say!",
                "Aww, thanks! You're pretty awesome too!",
                "I appreciate the compliment!",
                "You're too kind! Thank you!"
            ],
            
            # Questions about feelings
            r'(?i).*(are you.*happy|do you.*feel).*': [
                "I'm always happy to chat with you!",
                "I feel great when I'm helping people!",
                "I'm in a good mood! Thanks for asking!"
            ],
            
            # Default fallback for unknown inputs
            r'.*': [
                "That's interesting! Tell me more.",
                "I'm not sure I understand completely, but I'm listening!",
                "Could you rephrase that? I want to make sure I understand.",
                "Hmm, I'm still learning. Can you explain that differently?",
                "That's a good point! What else would you like to talk about?",
                "I see! What made you think about that?",
                "Interesting perspective! Can you elaborate?",
                "I'm here to listen. What's on your mind?"
            ]
        }
    
    def get_response(self, user_input):
        """Get a response based on user input using pattern matching"""
        if not user_input.strip():
            return "I didn't catch that. Could you say something?"
        
        # Try to match patterns in order (except default)
        patterns_list = list(self.patterns.items())[:-1]  # Exclude the default pattern
        
        for pattern, responses in patterns_list:
            if re.search(pattern, user_input):
                return random.choice(responses)
        
        # If no pattern matches, use default responses
        default_responses = self.patterns[r'.*']
        return random.choice(default_responses)
    
    def chat(self):
        """Start an interactive chat session"""
        print(f"Hello! I'm {self.name}. Type 'quit' to exit.")
        print("-" * 50)
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print(f"{self.name}: Goodbye! Have a great day!")
                break
            
            response = self.get_response(user_input)
            print(f"{self.name}: {response}")

if __name__ == "__main__":
    bot = SimpleChatbot()
    bot.chat()