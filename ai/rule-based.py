def chatbot():
    print("AI Chatbot: Hello! ")

    while True:
        user_input = input("You: ").lower()

        
        if user_input in ["hi", "hello", "hey"]:
            print("AI Chatbot: Hello there! How can I help you?")

        elif "what is ai" in user_input:
            print("AI Chatbot: Artificial Intelligence means machines or softwares that can think, learn and act like human.")

        elif "who created ai" in user_input:
            print("AI Chatbot: Alan Turing often called the father of AI. He proposed the idea that machines could simulate any human intelligence process.")

        elif user_input in ["bye", "exit"]:
            print("AI Chatbot: Good Bye! Have a nice day!")
            break

        
        else:
            print("AI Chatbot: I'm still learning. Can you rephrase it.")

chatbot()