
def convert_to_upper(lines):
    for line in lines:
        print(line.upper())

# Input lines from user
n = int(input("Enter number of lines: "))
lines = []

for i in range(n):
    line = input(f"Enter line {i+1}: ")
    lines.append(line)

print("\nOutput:")
convert_to_upper(lines)