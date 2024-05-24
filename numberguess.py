import random
def numb():
    print("Number Guessing Game with Python")
    print("Introduction:")
    print("1. The user selects a range of numbers","2.Let’s say User selected a range, i.e., from A to B, where A and B belong to Integer.","3. Some random integer will be selected by the system and the user has to guess that integer in the minimum number of guesses")
    n1=int(input("Enter the lower limit of the range:"))
    n2=int(input("Enter the end limit of the range:"))
    t=random.randint(n1,n2)
    lives=[1,2,3]
    for i in lives:
        guess=int(input("enter your guess:"))
        if guess==t:
            print("Congrats, you guessed it right!")
            break
        elif guess<t:
            print("NO!, you guessed it too low")
            print("you have",3-i,"chances left")
            continue
        elif guess>t:
            print("NO!, you guessed it too high")
            print("you have",3-i,"chances left")
            continue
    print("The correct answer is",t)
numb()            

        


       
    
