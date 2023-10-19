import requests
import random
import time
import threading
import msvcrt

running = True
start = False
api_url = ""

def is_key_pressed():
    # Check if a key has been pressed
    return msvcrt.kbhit()

def get_key():
    # Get the key that was pressed
    key = msvcrt.getch()
    return key

# --------------------------------------------------------------------------------------------------------------------------------------------- #

print("Welcome to PyLove! To get started Connect your Phone and Computer to the same Wifi.")
print("Then go into your Lovense Remote App and go to Settings>Game Mode. Connect your toy(s), then you will find the needed info there.")
print()

# Lovense Info Grabbing

def pyLove_Surprise():
    global running
    global start

    while True:
        print("\n\nInput how many seconds will occur between")
        intervalSec = int(input())
        print(f"You Have selected {intervalSec} seconds.\n")

        if isinstance(intervalSec, int) or intervalSec >= 0:
            break
        else:
            print("Invalid Input: Input Must be a Number [0 or Greater]")

    while True:
        if not start:
            print("Press Enter to start the randomization cycle.")
            input()
            running = True
            start = True

        surprise_thread = threading.Thread(target=lambda: surp_GameHandler(intervalSec))
        surprise_thread.start()

        print("Press Esc to stop the randomization cycle.")
        while running:
            if is_key_pressed():
                key = get_key()
                if key == b'\x1b':  # Check for Esc key
                    running = False
            time.sleep(0.1)  

        print("Might take a moment to Restart.")
        surprise_thread.join()

        print("Do you wish to Restart Surprise Round [y/n]?")
        restart = input(">>> ").upper()

        if restart=="N":
            print("\n\n\n\n\n\n\n\n\n")
            start = False
            break
        else:
            print("Restarting app. . .")
            running = True
            start = False

def surp_GameHandler(intervalSec : int):
    global running

    running = True

    while running:
            if not running:
                break

            print("Looped")

            randRoulette = random.randint(1,10)
            print(f"Roulette Roll: {randRoulette}")

            if randRoulette == 5:
                # Randomizes Activation Strength
                random_number = random.randint(1, 10)
                print("Lvl1: Strength of Activation:" + str(random_number))

                # Randomizes Activation Duration
                rand_time = random.randint(2, 8)
                print(f"Duration: {rand_time} seconds")

                Surprise_Random(random_number, rand_time)
            elif randRoulette == 10:
                # Randomizes Activation Strength
                random_number = random.randint(10, 20)
                print("Lvl2: Strength of Activation:" + str(random_number))

                # Randomizes Activation Duration
                rand_time = random.randint(2, 8)
                print(f"Duration: {rand_time} seconds")

                Surprise_Random(random_number, rand_time)
            else:
                print('You got Lucky this time.')
            print()

            if not running:
                break

            time.sleep(intervalSec)

    print("Randomization cycle stopped.")


def Surprise_Random(Strength: int, timesec: int):
    global api_url
    toyCommand = {
        "command": "Pattern",
        "rule": "V:1;F:v,r,p,f,s,t;S:200#",
        "strength": f"{Strength}",
        "timeSec": timesec,
        "apiVer": 2
    }

    response = requests.post(api_url, json=toyCommand)
    print(response.json())

    response.status_code


def main():
    global api_url

    while True:
        print()
        print("Input your Phone's Local API shown in the Lovense App: ")
        domain = input(">>> ")

        print("\nInput the Http Port shown on the Application.")
        httpPort = input(">>> ")

        api_url = f"http://{domain}:{httpPort}/command"
        print(api_url)

        if (domain != "" and httpPort != ""):
            print(f"\n\nIP: {domain}\nHttp: {httpPort}")
            confirm = input("\n\n^ ^ ^ Does this look Correct? Y/N >>> ")

            if(confirm.capitalize() == "Y"):
                break
        else:
            print("Invalid Input, values cannot be Empty.")

    while True:
        
        print("Which Game would you like to Play?\n\n1 : Surprise! \nQUIT : Close PyLove\n\n")
        gameOption = input(">>> ")
        gameOption = gameOption

        match gameOption:
            case "1":
                pyLove_Surprise()
            case "QUIT":
                break


main()