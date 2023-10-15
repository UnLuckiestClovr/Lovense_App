import requests
import random
import time
import subprocess
import threading

running = True
start = False

# --------------------------------------------------------------------------------------------------------------------------------------------- #

print("Welcome to PyLove! To get started Connect your Phone and Computer to the same Wifi.")
print("Then go into your Lovense Remote App and go to Settings>Game Mode. Connect your toy(s), then you will find the needed info there.")
print()

# Lovense Info Grabbing

while True:
    print()
    print("Input your Phone's Local API shown in the Lovense App: ")
    domain = input(">>> ")

    print("Input the Http Port shown on the Application.")
    httpPort = input(">>> ")

    api_url = f"http://{domain}:{httpPort}/command"
    print(api_url)

    if (domain != "" and httpPort != ""):
        print(f"IP: {domain}\nHttp: {httpPort}")
        confirm = input("^ ^ ^ Does this look Correct? Y/N >>> ")

        if(confirm.capitalize() == "Y"):
            break
    else:
        print("Invalid Input, values cannot be Empty.")


def randomSurpriseHandler():
    global running
    global start

    print("Input how many seconds will occur between")
    intervalSec = int(input())
    print(f"You Have selected {intervalSec} seconds.")

    print("\n \n ")
    input("Press Enter to Start with these Settings:")

    start = True

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

            RussianRoulette(random_number, rand_time)
        elif randRoulette == 10:
            # Randomizes Activation Strength
            random_number = random.randint(10, 20)
            print("Lvl2: Strength of Activation:" + str(random_number))

            # Randomizes Activation Duration
            rand_time = random.randint(2, 8)
            print(f"Duration: {rand_time} seconds")

            RussianRoulette(random_number, rand_time)
        else:
            print('You got Lucky this time.')
        print()

        if not running:
            break

        time.sleep(intervalSec)

    print("Randomization cycle stopped.")


def RussianRoulette(Strength: int, timesec: int):
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

surprise_thread = threading.Thread(target=randomSurpriseHandler)
surprise_thread.start()

while not start:
    time.sleep(1)

input("Press Enter to stop the randomization cycle.")
print("Might take a moment to Restart.")
running = False
surprise_thread.join()