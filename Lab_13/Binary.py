
src_path = r"E:\College\Python Programming\Lab_13\a.tif"

with open(src_path, 'rb') as f:
    binDT = f.read()

print(binDT)

# Write binary data to new file
with open("c.tif", 'wb') as f:
    f.write(binDT)
