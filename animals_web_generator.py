import json

def load_data(file_path):
  """ Loads a JSON file """
  with open(file_path, "r") as handle:
    return json.load(handle)

animals_data = load_data("animals_data.json")
for animal in animals_data:
    name = animal["name"]
    diet = animal["characteristics"]["diet"]
    locations = animal["locations"][0]
    animal_type = animal["characteristics"].get("type")
    print(f"Name: {name})")
    print(f"Diet: {diet}")
    print(f"Location: {locations}")
    if animal_type:
        print(f"Type: {animal_type}")
    print()