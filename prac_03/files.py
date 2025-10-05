#1
FILE_NAME = "name.txt"
name = str(input("Enter name: "))
out_file = open(FILE_NAME, 'w')
print(f"{name}", file=out_file)
out_file.close()

#2
in_file = open(FILE_NAME, 'r')
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

#3
with open("numbers.txt", 'r') as in_file:
    number1 = int(in_file.readline())
    number2 = int(in_file.readline())
    result = number1 + number2
    print(result)

#4
with open("numbers.txt", 'r') as in_file:
    total = 0
    for line in in_file:
        total += int(line)
    print(total)



