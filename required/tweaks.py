import json

# Read the JSON file
with open('required/tweaks.json', 'r') as file:
    data = json.load(file)

if __name__ == '__main__':
    # Access specific elements
    bl = data['blacklist']
    alt = data['alternative']

    print(f"blacklist: {bl}")