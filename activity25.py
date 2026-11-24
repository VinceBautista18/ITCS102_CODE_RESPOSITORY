def taga_triangle(number):
    for x in range(number, 0, -1):
        for y in range(1, x+1):
            print("*", end= " ")
        print()


def sum(x, y):
    return x+y


def box(size):
    for x in range(size+1):
        for y in range(size+1):
            if y == 0 or x == 0 or x == size or y == size:
                print("*", end= " ")
            else:
                print(" ", end= " ")
        print()
    

taga_triangle(10)
taga_triangle(12)
print(sum(20,1))
print(sum(10,2) * 5)
box(20)