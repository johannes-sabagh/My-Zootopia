import requests
import os
from dotenv import load_dotenv

load_dotenv()
os.getenv("API_KEY")
def fetch_data(animal_name):
  """
  Fetches the animals data for the animal 'animal_name'.
  Returns: a list of animals, each animal is a dictionary:
  {
    'name': ...,
    'taxonomy': {
      ...
    },
    'locations': [
      ...
    ],
    'characteristics': {
      ...
    }
  },
  """
  headers = {}
  API_KEY = "D8w7JPL6XS56dpBBiggENoUYKdf9h5vb8z4ZaB0M"
  headers["x-api-key"] = API_KEY
  animal_data = requests.get(f"https://api.api-ninjas.com/v1/animals?name={animal_name}", headers= headers)
  return animal_data.json()

