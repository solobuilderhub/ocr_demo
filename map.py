import json

# Load the JSON data from the file
with open("a901 renewal.json", "r") as json_file:
    data = json.load(json_file)

# Filter the fields with the prefix "page_7"
filtered_fields = {key: value for key, value in data.items() if key.startswith("pg16_")}

# Save the filtered fields to a new JSON file
with open("field map/a901 renewal form/page_16_fields.json", "w") as json_file:
    json.dump(filtered_fields, json_file, indent=4)

print("Filtered fields have been saved to page_8_fields.json")