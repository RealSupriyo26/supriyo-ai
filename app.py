# supriyo-ai: Smart Assistant
import time

print("==========================================")
print("     Welcome to Supriyo AI Assistant      ")
print("==========================================")

def supriyo_ai_chat():
    user_name = input("Enter your name: ")
    print(f"\nHello {user_name}! I am your personal AI assistant.")
    
    while True:
        prompt = input("\nAsk Supriyo AI (or type 'exit' to quit): ")
        if prompt.lower() == 'exit':
            print("Goodbye! Thank you for using Supriyo AI.")
            break
        
        print("Thinking...")
        time.sleep(1)
        print(f"Supriyo AI: I received your query: '{prompt}'. I am working on this task!")

if __name__ == "__main__":
    supriyo_ai_chat()
  
