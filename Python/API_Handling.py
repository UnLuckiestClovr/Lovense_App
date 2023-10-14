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

        print("We Successfully Got to the End")
    except Exception as error:
        print(f"Error Found: {error}")


def getToyName():
    try:
        command = {"command": "GetToyName"}

        response = requests.post(url, json=command)

        print("ToyName: ", response.json())

        response.json()
        response.status_code

        print("We Successfully Got to the End")

    except Exception as error:
        print(f"Error Found: {error}")


def CommandCertainToy():
    toyCommand = {
        "command": "Function"
    }

def CommandAllToys():
    toysCommand = {
        "command": "Funciton"
    }

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ #

getToys()

