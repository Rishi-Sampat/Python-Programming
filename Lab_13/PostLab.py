import csv

text_file = r"E:\College\Python Programming\Lab_13\ict1.txt"

with open(text_file, 'r') as f:
    txt = f.read()

with open(text_file, 'r') as f:
    line_list = f.readlines()

lines = len(line_list)
words = len(txt.split())
chrs = len(txt)

print("No. of Lines:", lines)
print("No. of words:", words)
print("No. of chrs:", chrs)

lines_clean = []
with open(text_file, 'r') as f:
    for i in f:
        lines_clean.append(i.strip())
print(lines_clean)

csv_file = r"E:\College\Python Programming\Lab_13\data-1.csv"

with open(csv_file, 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

file1 = r"E:\College\Python Programming\Lab_13\ict1.txt"
file2 = r"E:\College\Python Programming\Lab_13\ict2.txt"
merged = r"E:\College\Python Programming\Lab_13\merged.txt"

with open(file1, 'r') as f1, open(file2, 'r') as f2, open(merged, 'w') as m:
    m.write(f1.read())
    m.write("\n")
    m.write(f2.read())

print("merged:")
