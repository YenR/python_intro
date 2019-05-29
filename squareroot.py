
def get_squareroot(a):
    x= 0.0
    epsilon = 0.01
    step = epsilon**2

    while abs(x**2-a)>=epsilon and x<a:
        x+= step
    if abs(x**2 -a) >= epsilon:
        print("Failed on square root of ", a)
    else:
        return x


if __name__ == "__main__":
    a = float(input("Please input a positive integer: "))
    print("The square root of", a, "is", get_squareroot(a))