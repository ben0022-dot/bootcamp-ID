#You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
keys = ['ten ', 'twenty', 'thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)
#Output: {'ten ': 10, 'twenty': 20, 'thirty': 30}
 #Write a program that calculates the total cost of movie tickets for a family based on their ages.
 #Family members’ ages are stored in a dictionary. The ticket prices are as follows:
#Under 3 years): $0
#3-12 years): $10
#Over 12 years): $15
family_ages = {
    'Alice': 2,
    'Bob': 5,
    'Charlie': 15,
    'David': 30
}
total_cost = 0
for name, age in family_ages.items():
    if age < 3:
        total_cost += 0
    elif 3 <= age <= 12:
        total_cost += 10
    else:
        total_cost += 15
print(f"Total cost of movie tickets: ${total_cost}")
#family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#Loop through the family dictionary to calculate the total cost.
#total_cost = sum(10 if 3 <= age <= 12 else 15 for age in family.values() if age >= 3)
#print(f"Total cost of movie tickets: ${total_cost}")

#Create and manipulate a dictionary that contains information about the Zara brand.
zara_info = {
    "brand": "Zara",
    "founded": 1975,
    "founder": "Amancio Ortega",
    "headquarters": "Spain"
}
print(zara_info)
#Accessing and modifying dictionary elements
print(zara_info["brand"])
zara_info["founded"] = 1976
print(zara_info)
#Change the value of number_stores to 2
zara_info["number_stores"] = 2
print(zara_info)
#Add a new key called "country_creation" with the value "Spain"
zara_info["country_creation"] = "Spain"
print(zara_info)
#Check if international_competitors exists and, if so, add “Desigual” to the list.
if "international_competitors" in zara_info:
    zara_info["international_competitors"].append("Desigual")
print(zara_info)
#Delete the information about the date of creation.
del zara_info["founded"]
print(zara_info)
#Print the last item international competitor.
if "international_competitors" in zara_info:
    print(zara_info["international_competitors"][-1])
#Print the major colors in the US.
if "major_colors_us" in zara_info:
    print(zara_info["major_colors_us"])
#Print the number of keys in the dictionary.
print(f"Number of keys in the dictionary: {len(zara_info)}")
#Print the keys of the dictionary.
print(f"Keys in the dictionary: {list(zara_info.keys())}")
#Create another dictionary called more_on_zara with the following details:
more_on_zara = {
    "creation_date": 1975,
    "number_stores": 2
}
#You are given a list of Disney characters. Create three dictionaries based on different patterns as shown below:

disney_characters = ["Mickey", "Minnie", "Donald", "Ariel", "Pluto"]
#Create a dictionary that maps characters to their indices:
character_indices = {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
print(character_indices)
#Create a dictionary that maps indices to characters:
index_characters = {0: "Mickey", 1: "Minnie", 2: "Donald", 3: "Ariel", 4: "Pluto"}
print(index_characters)
#Create a dictionary where characters are sorted alphabetically and mapped to their indices:
character_indices_sorted = {0: "Ariel", 1: "Donald", 2: "Mickey", 3: "Minnie", 4: "Pluto"}
print(character_indices_sorted)



