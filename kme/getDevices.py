import pykath
import requests
import json

## Get ClientId from clientIds file
clientIdFile = "myClientIds.json"
with open(clientIdFile, "r") as file:
    clientIds = json.load(file)

cId = clientIds['kme']

## Initialize Knox Access Token HelperLibrary (pyKATh)
kat = pykath.init(kcsKeyFilePath = 'myKeys.json', regionalServer = 'us-kcs-api.samsungknox.com', clientId = cId)

## Generate a signed Access token to be used to authenticate to the KCS API 
signedAccessToken = kat.getSignedAccessToken()

## KCS Base URL for the US region
baseUrl = "https://us-kcs-api.samsungknox.com/kcs/v1/"

## Function to call the getDeviceList API
def getDeviceList():
    api = baseUrl+"kme/devices/list"
    headers = {
        'Content-Type': 'application/json',
        'x-knox-apitoken': signedAccessToken
    }

    response = requests.get(api, headers=headers)
    if response.status_code == 200:
        print(response.text)
    else:
        print(f"Request failed. Status code: {response.status_code}, Response: {response.text}")

getDeviceList()