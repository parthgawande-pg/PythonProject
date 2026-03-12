source_file = input("Enter the source file name: ")
new_file = input("Enter the new file name: ")

f = open(source_file, "r")
content = f.read()
f.close()

upper_content = content.upper()

f2 = open(new_file, "w")
f2.write(upper_content)
f2.close()

print("Content written to new file in uppercase.")