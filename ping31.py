with open("ping2.txt", "r") as file:
    data = file.readlines()

cleaned_data = [line.strip() for line in data if line.strip()]

with open("ping31.txt", "w") as file:
    for line in cleaned_data:
        file.write(line + "\n")