import requests
import datetime
import os

APIID = os.environ.get("NT_API_ID")
APIKEY = os.environ.get("NT_API_KEY")

GENDER = 'male'
WEIGHT_KG = 70
HEIGHT_CM = 175
AGE = 32

headers = {
    'x-app-id': APIID,
    'x-app-key': APIKEY,
    'x-remote-user-id': '0'
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

input = input("Tell me which exercises you did: ")
exercise_para = {
    "query": input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
response = requests.post(exercise_endpoint, json = exercise_para, headers = headers)
result = response.json()

username = "caf14cc59105725febff04f5bba84d53"
projectName = "stevenWorkoutsCoding"
sheetName = "workouts"

sheety_endpoint = f"https://api.sheety.co/{username}/{projectName}/{sheetName}"

now = datetime.datetime.now()
today_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%X")

sheety_header = {
    "Authorization": "Basic c3RldmVudGV5OkJ2JVg2XjBjQnVoUjRGXiU= "
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(sheety_endpoint, json=sheet_inputs, headers=sheety_header)

    print(sheet_response.text)