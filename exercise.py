import requests

# part 1
ottawa_wards_response = requests.get('https://represent.opennorth.ca/boundaries/ottawa-wards/?limit=30')
python_dict_1 = ottawa_wards_response.json()
ottawa_wards = python_dict_1["objects"]
print("[Number of wards in Ottawa]:")
print(len(ottawa_wards))
print()
print("[Names of wards in Ottawa]:")
for ward in ottawa_wards:
    print("*", ward["name"])

# part 2
house_of_commons_response = requests.get('https://represent.opennorth.ca/representatives/house-of-commons/?limit=500')
python_dict_2 = house_of_commons_response.json()
reps = python_dict_2["objects"]
print("[Number of reps in the House of Commons:]")
print(len(reps))
print()
print("[Reps in the House of Commons]:")
for rep in reps:
    print(f"* Name: {rep['name']}\n  Party: {rep['party_name']}")
