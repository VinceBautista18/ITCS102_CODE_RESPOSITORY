size = int(input("Type your x-----------> "))
for i in range(size):
    for j in range(size):
        if i + j == size - 1 or i == j:
            print("*", end=" ")
        else:
            print(" ", end= " ")
    print()  
