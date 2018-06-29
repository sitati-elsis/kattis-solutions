names = input()
separated_names = names.split("-")
scientific_name= ""
for item in separated_names:
    scientific_name = scientific_name + item[0]
print(scientific_name)