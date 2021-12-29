vertically = int(input("Введите высоту:"))
horizontally = (vertically*2)-1

for i in range(vertically):
    print(i+1, end='\t')
    for j in range(horizontally):
        if j == horizontally//2+i or j == horizontally//2-i or i == \
                vertically-1 or horizontally//2-i < j < horizontally//2+i:
            print('* ', end='')
        else:
            print('  ', end='')
    print()