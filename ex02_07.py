lines = []

while True :
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)

print("Các dòng sẽ được in đậm")
for line in lines:
    print(line.upper())
