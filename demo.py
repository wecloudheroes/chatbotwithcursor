#!/usr/bin/env python3
"""
Demo script to showcase the Simple Chatbot capabilities
"""

from chatbot import SimpleChatbot

def run_demo():
    print("=" * 60)
    print("🤖 SIMPLE CHATBOT DEMO")
    print("=" * 60)
    print()
    
    bot = SimpleChatbot()
    
    # Demo conversations
    demo_inputs = [
        "Hello!",
        "What's your name?",
        "How are you?",
        "What time is it?",
        "What's the date today?",
        "What can you do?",
        "You're awesome!",
        "How's the weather?",
        "Thank you!",
        "Goodbye!"
    ]
    
    print("Here are some example conversations with the chatbot:")
    print("-" * 50)
    
    for user_input in demo_inputs:
        response = bot.get_response(user_input)
        print(f"👤 User: {user_input}")
        print(f"🤖 {bot.name}: {response}")
        print()
    
    print("=" * 60)
    print("💡 TIP: Run 'python3 chatbot.py' for interactive mode")
    print("💡 TIP: Run 'python3 app.py' for web interface")
    print("=" * 60)

if __name__ == "__main__":
    run_demo()