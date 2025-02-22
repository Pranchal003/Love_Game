logo = """  **                                         ********                                **
/**                                        **//////**                              /**
/**        ******  **    **  *****        **      //   ******   **********   ***** /**
/**       **////**/**   /** **///**      /**          //////** //**//**//** **///**/**
/**      /**   /**//** /** /*******      /**    *****  *******  /** /** /**/*******/**
/**      /**   /** //****  /**////       //**  ////** **////**  /** /** /**/**//// // 
/********//******   //**   //******       //******** //******** *** /** /**//****** **
////////  //////     //     //////         ////////   //////// ///  //  //  ////// //  


"""


from random import randint
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(logo)

print("Welcome to My Valentine’s Day Love Game! \n")
print(" Think of a number between 1 and 1000. If I guess right, you owe me a kiss! ")




LOW_LOVE_LEVEL = 9
MEDIUM_LOVE_LEVEL = 99
HIGH_LOVE_LEVEL = 999
# Simulated heartbeat data (Replace with actual dataset)
time = np.linspace(0, 10, 500)  # 10 seconds, 500 samples
heartbeat = np.sin(2 * np.pi * 1.5 * time) + 0.5 * np.random.randn(500)  # Simulated signal

# Convert to DataFrame
df = pd.DataFrame({'Time (s)': time, 'Heartbeat': heartbeat})


def set_difficulty():
    choice = input("\nChoose a difficulty. Type 'low', 'medium' or 'high'")
    if choice == "low":
        return LOW_LOVE_LEVEL
    elif choice == "medium":
        return MEDIUM_LOVE_LEVEL
    else: 
        return HIGH_LOVE_LEVEL

def check_guess(guess, answer, attempts_left):
    """ Check the guess and respond with a romantic message. """
    if guess == answer:
        print("OMG BABE! You guessed it right! You owe me a big hug and a kiss.")
        return 0
    
    # Lucky number
    if guess in [69, 99, 777, 999]:
        print("Whoa! You choose a lucky love number! But it's is not a answer! Try again baby. ")
    
    
    elif (guess - answer)  <= 10:
        print("Sooo close! Just like us, always near each other. Try again bubu!")

    elif (guess - answer) <= 50:
        print("You're getting warmer! just like my heart when I see you!")
    
    elif  guess < answer  <= 100:
        print("I can feel the love, but you're still a bit far. Keep going!")

    else:
        print("You got it , But no worries, my heart is always close to you! ")


    return attempts_left -1
        

def game():

    """Main Love Guessing Game Loop"""
    answer = randint(1, 1000)
    attempts = set_difficulty()
    guess = -1
 
    while guess != answer or attempts == 0:
        print(f"\n You have {attempts} attempts left. Make a guess, my love! ")
        guess = int(input("Enter your number:"))
        attempts = check_guess(guess, answer, attempts)

        if attempts == 0:
            print(" Oh no! You've run out of attempts... But don't worry, I still love you! ")
            return

    print(" Let's celebrate our love with some heartbeats! ")


def show_heartbeat():

    plt.figure(figsize=(10, 5))
    sns.lineplot(x="Time (s)", y="Heartbeat", data=df, color='red')
    plt.xlabel("Time (s)")
    plt.ylabel("Heartbeat Signal")
    plt.title("Your Love MAkes My Heartbeat Faster!")
    plt.grid(True)
    plt.show()

    plt.figure(figsize=(8, 5))
    sns.histplot(df["Heartbeat"], bins=30, kde=True, color='pink')
    plt.xlabel("Heartbeat Amplitude")
    plt.ylabel("Frequency")
    plt.title("Heartbeat Signal Distribution")
    plt.show()

game()
show_heartbeat()