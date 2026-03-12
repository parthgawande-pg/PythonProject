source = input("Enter source python file: ")
destination = input("Enter destination file: ")

f = open(source, "r")
lines = f.readlines()
f.close()

clean_lines = []

for line in lines:
    text = line.strip()
    if not text.startswith("#") and text != "":
        clean_lines.append(line)

f2 = open(destination, "w")
f2.writelines(clean_lines)
f2.close()

print("\nSource File Content:\n")
f = open(source, "r")
print(f.read())
f.close()

print("\nDestination File Content (without comments):\n")
f2 = open(destination, "r")
print(f2.read())
f2.clo