import json

fruit = {
    "vehicle": "Car",
    "wheels": "4",
    "color": "Red"
}

with open("fruit.json", "w") as output_file:
    json.dump(fruit, output_file)

with open("fruit.json", "r") as input_file:
    dictionary = json.load(input_file)

result = []

for key, value in dictionary.items():
    result.append((key, value))

result = tuple(result)

for element in result:
    print(element)
