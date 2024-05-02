import time
import random

class Chatbot:
    def __init__(self):
        self.name = None
    
    def greet(self):
        print("Hi, I am friendly chatbot, JARVIS !!")
        time.sleep(2)
        self.name = input("What's your good name ? ")
        print("It was nice talking to you ", self.name, " !!\n\n")
        time.sleep(5)
    
    def menu(self):
        choice = int(input("Tell me how can I help you ?\nHere are some functionalities in which I can help you : \n1. Tell me a joke \n2. Number guess game \n3. You want to share anything bad happened with you?\n4. exit\n\nEnter Correct number you selected "))
        return choice
    
def main():
    chatbot = Chatbot()
    chatbot.greet()
    while True:
        choice = chatbot.menu()
        if choice ==1:
            print("Sure, here's one:\nWhy don't skeletons fight each other?\nThey don't have the guts!\n\n")
            time.sleep(5)
        elif choice == 2:
            num = random.randint(1, 100)
            guess = None
            no_of_guess = 0
            while num != guess:
                guess = int(input("Guess a number : "))
                if(num < guess):
                    print("its high")
                    no_of_guess+=1
                elif(num > guess):
                    print("its low")
                    no_of_guess += 1
                else:
                    print("congratulation", " \nyou guessed it in ", no_of_guess, " moves\n\n")
            time.sleep(5)
        elif choice == 3:
            em = input("You can share whatever bad happened with you !!")
            print("Be Strong and do write things that will make you strong to fight with the situation. Good Luck\n\n")
            time.sleep(5)
        elif choice == 4:
            print("Thanks for chatting with me !! See you soon")
            time.sleep(3)
            break
        else:
            print("Enter Valid Input")
            time.sleep(2)
            
        
main()
    
