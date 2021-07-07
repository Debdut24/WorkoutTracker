import requests
import os
import datetime as dt
# "73dd0ef0"
API_ID = os.environ.get("API_ID")
API_KEY = os.environ.get("API_KEY")
endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id" : API_ID,
    "x-app-key" : API_KEY,
}
query = input("What did you do ?")
parameters = {
    "query":query,
    "gender":"male",
    "weight_kg":54.5,
    "height_cm":174.64,
    "age":21
}
response = requests.post(url = f"{endpoint}",json = parameters,headers = headers)
response = response.json()
exercise = response["exercises"][0]["name"]
exercise = exercise.title()
duration = response["exercises"][0]["duration_min"]
calories = response["exercises"][0]["nf_calories"]
time_now = dt.datetime.now()
date = time_now.strftime("%d/%m/%Y")
time = time_now.strftime("%H:%M:%S")

sheety_getapi = "https://api.sheety.co/a44f1e7a48d59692274e02871effb520/workoutTracking/sheet1"
sheety_postapi = os.environ.get("sheety_postapi")
sheety_putapi = os.environ.get("sheety_putapi")

entry = {
    "sheet1":{
        "date" : date,
        "time" : time,
        "exercise" : exercise,
        "duration" : duration,
        "calories" : calories,
    }
}
username = os.environ.get("user")
password = os.environ.get("password")
response2 = requests.post(url = f"{sheety_postapi}",json = entry,auth = (username,password))
print(response2.text)