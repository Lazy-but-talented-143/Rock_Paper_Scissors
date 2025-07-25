def game():
    print("*****************Welcome to Rock_Paper_ScissorsGame*****************")
    import random
    options=["rock","paper","scissor"]
    i=random.choice(options)
    print("Chose from the below Three options")
    print("rock","paper","scissor")
    a=input("Enter your value:").lower()
    if a==i:
        print(f"Your choice={[ a ]}:Computer choice={[ i ]} \n['********[Game]-<Tie>-*********']")
    elif a=="paper" and i =="scissor":
        print(f"Your choice={[ a ]}:Computer choice={[ i ]} \n['********[Game]-<Lose>-********']")
    elif a=="rock" and i=="paper":
        print(f"Your choice={[ a ]}:Computer choice={[ i ]} \n['********[Game]-<Lose>-********']")
    elif a=="scissor" and i=="rock":
        print(f"Your choice={[ a ]}:Computer choice={[ i ]} \n['********[Game]-<Lose>-********']")
    elif a=="scissor" and i=="paper":
        print(f"Your choice={[ a ]}:Computer choice={[ i ]} \n['********[Game]-<Win>-********']")
    elif a=="paper" and i=="rock":
        print(f"Your choice={[ a ]}:Computer choice={[ i ]} \n['********[Game]-<Win>-********']")
    elif a=="rock" and i=="scissor":
       print(f"Your choice={[ a ]}:Computer choice={[ i ]} \n['********[Game]-<Win>-********']")
    else:
       print("Enter a valid choice:")
    print("Do you want to play again?")
    print("Yes/No")
    b=input("Enter your choice:").lower()
    if b=='yes' :
        print("Ok, Don't Stop Until You Win \nKeep on Trying ")
        return game()
    else:
        print("Bye Thank you For Playing")
        return 
game()