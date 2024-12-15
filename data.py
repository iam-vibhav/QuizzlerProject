import requests


API_URL = "https://opentdb.com/api.php?amount=10&category=18&difficulty=medium&type=boolean"

response = requests.get(url=API_URL)

question_data = response.json()["results"]

