import requests
import random
import time
import subprocess

# --------------------------------------------------------------------------------------------------------------------------------------------- #

# Lovense Info Grabbing

domain = input("Input your Phone's Local API:")
httpPort = input("")

api_url = f"http://{domain}:{httpPort}/command"
print(api_url)


def randomSurpriseHandler():
    print("Input how many seconds will occur between")
    intervalSec = int(input())
    print(f"You Have selected {intervalSec} seconds.")

    while True:
        print("Looped")

        randRoulette = random.randint(1,16)
        print(f"Roulette Roll: {randRoulette}")

        if randRoulette == 4:
            random_number = random.randint(1, 5)
            print("Lvl1: Strength of Activation:" + str(random_number))
        elif randRoulette == 8:
            random_number = random.randint(5, 10)
            print("Lvl2: Strength of Activation:" + str(random_number))
        elif randRoulette == 12:
            random_number = random.randint(10, 15)
            print("Lvl3: Strength of Activation:" + str(random_number))
        elif randRoulette == 16:
            random_number = random.randint(15, 20)
            print("Lvl4: Strength of Activation:" + str(random_number))
        else:
            print('You got Lucky this time.')

        time.sleep(intervalSec)


def RussianRoulette(Strength: float, timesec: int):
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

randomSurpriseHandler()