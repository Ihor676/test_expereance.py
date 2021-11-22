string = "Hello world"
start = -1
count = 0

while True:
    start = string.find("l", start+1)
    if start == -1:
        break
    count += 1

print("Количество вхождений символа в строку: ", count )







