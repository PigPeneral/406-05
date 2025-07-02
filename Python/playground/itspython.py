num_int = "123456789"
num_list = [1,2,3,4,5,6,7,8,9]

for p in range(len(num_int)-1, -1, -1):
    print(num_int[p], end=" ")
print()

print(" ".join(map(str, num_list[::-1])))

print(" ".join(map(str, (list(map(lambda x: 10-x, range(1,10)))))))
