def name_score(name):
    return sum(ord(c) - ord("A") + 1 for c in name)

with open("0022_names.txt", "r") as file:
    names = file.read().replace('"', '').split(",")

names.sort()
total = sum((i + 1) * name_score(name) for i, name in enumerate(names))
print(total)
