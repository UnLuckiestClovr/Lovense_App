import requests
import json

domain = "192.168.0.129"
httpPort = "20010"
httpsPort = "30010"

url = f"http://{domain}:{httpPort}/command"
print(f"API-URL = {url}")

def getToys():
    try:
        command = {"command": "GetToys"}

        response = requests.post(url, json=command)

        print("Available Toys: ", response.json())

        response.json()
        response.status_code
    except Exception as error:
        print(f"Error Found: {error}")


def getToyName():
    try:
        command = {"command": "GetToyName"}

        response = requests.post(url, json=command)

        print("ToyName: ", response.json())

        response.json()
        response.status_code

    except Exception as error:
        print(f"Error Found: {error}")


# V V Command Setup V V
"""

    command: [required]
        Type of request
        Var = String

    action: 
        Control the function and strength of the toy
        Var = string
        Actions can be Vibrate, Rotate, Pump, Thrusting, Fingering, Suction or Stop. Use All to make all functions respond. Use Stop to stop the toy’s response.
        Range:
        Vibrate:0 ~ 20
        Rotate: 0~20
        Pump:0~3
        Thrusting:0~20
        Fingering:0~20
        Suction:0~20
        All:0~20

    timeSec: [required]
        Total running time
        Var = double
        0 = indefinite length
        Otherwise, running time should be greater than 1.

    loopRunningSec: [optional]
        Running time
        Var = double
        Should be greater than 1

    loopPauseSec: [optional]
        Suspend Time
        Var = double
        Should be greater than 1

    toy: [optional]
        Toy ID
        Var = string
        If you do not include this, it will be applied to all toys

    stopPrevious: [optional]
        Stop all previous commands and execute current commands
        Var = int
        Default: 1, If set to 0 , it will not stop the previous command.

    apiVer: [required]
        The version of the request
        Var = int
        Always Uses 1
"""

#Examples
"""
    // Vibrate toy ff922f7fd345 at 16th strength, run 9 seconds then suspend 4 seconds. It will be looped. Total running time is 20 seconds.
    {
    "command": "Function",
    "action": "Vibrate:16",
    "timeSec": 20,
    "loopRunningSec": 9,
    "loopPauseSec": 4,
    "toy": "ff922f7fd345",
    "apiVer": 1
    }

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    // Vibrate 9 seconds at 2nd strength
    // Rotate toys 9 seconds at 3rd strength
    // Pump all toys 9 seconds at 4th strength
    // For all toys, it will run 9 seconds then suspend 4 seconds. It will be looped. Total running time is 20 seconds.
    {
    "command": "Function",
    "action": "Vibrate:2,Rotate:3,Pump:3",
    "timeSec": 20,
    "loopRunningSec": 9,
    "loopPauseSec": 4,
    "apiVer": 1
    }

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

    // Vibrate 9 seconds at 2nd strength
    // The rest of the functions respond to 10th strength 9 seconds
    {
    "command": "Function",
    "action": "Vibrate:2,All:10",
    "timeSec": 20,
    "loopRunningSec": 9,
    "loopPauseSec": 4,
    "apiVer": 1
    }

    - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
    
    // Stop all toys
    {
    "command": "Function",
    "action": "Stop",
    "timeSec": 0,
    "apiVer": 1
    }
"""

def CommandToy_HUSH(funcSet):

    toyCommand = {
        "command": "Function",
        "action": f"Vibrate:{str(funcSet['vibrateIntens'])}",
        "timeSec": funcSet['timeSec'],
        "loopRunningSec": funcSet['loopRunningSec'],
        "loopPauseSec": funcSet['loopPauseSec'],
        "apiVer": 1
    }

    response = requests.post(url, json=toyCommand)
    print(response.json())

    response.status_code
    

def CommandAllToys(funcSet):
    toyCommand = {
        "command": "Function",
        "action": f"All:{str(funcSet['vibrateIntens'])}",
        "timeSec": funcSet['timeSec'],
        "loopRunningSec": funcSet['loopRunningSec'],
        "loopPauseSec": funcSet['loopPauseSec'],
        "apiVer": 1
    }

    response = requests.post(url, json=toyCommand)
    print(response.json())

    response.status_code

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

def liveChanges(Strength: float):
    toyCommand = {
        "command": "Pattern",
        "rule": "V:1;F:v,r,p,f,s,t;S:200#",
        "strength": f"{Strength}",
        "timeSec": 9,
        "toy": "ff922f7fd345",
        "apiVer": 2
    }

    response = requests.post(url, json=toyCommand)
    print(response.json())

    response.status_code

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

