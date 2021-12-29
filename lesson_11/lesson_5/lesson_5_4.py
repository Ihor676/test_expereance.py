vertically = int(input("Введите высоту(нечетное число):"))
horizontally = vertically
for i in range(vertically):
    print(i+1, end='\t')
    for j in range (horizontally):
        if j == horizontally//2+i or j == horizontally//2-i or  \
                horizontally//2-i < j < horizontally//2+i and i <= \
                vertically//2 or j == -horizontally//2+i+1 or j == \
                horizontally -1-i + horizontally//2 or j == horizontally//2:
            print('*', end=' ')
        else:
            print('  ', end='')
    print()