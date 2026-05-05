def bot():
    print("chatbot:hello!type bye to exit")
    while True:
        word=input("enter word=").lower()
        if word=="hello":
            print("Chatbot:HI!")
        elif word=="how are you":
            print("Chatbot:I'm fine,thanks!")
        elif word=="bye":
            print("Chatbot:Goodbye!")
        else:
            print("Chatbot:i don't understand!")
            break
bot()

            
