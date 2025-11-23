
file_path = r"E:\College\Python Programming\Lab_13\ict.txt"

with open(file_path, 'r') as file:
    lines = file.readlines()   # Read all lines

    for line in lines:
        words = line.split()   # Split each line into words
        print(words)


with open("E:\College\Python Programming\Lab_13\ict.txt",'r') as file:
    dt=file.readlines()
    for i in dt:
        word=i.split()
        print(word)