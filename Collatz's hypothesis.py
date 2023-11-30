def collatz_hypothesis(c0):
    steps = 0
    while c0 != 1:
        if c0 % 2 == 0:
            c0 //= 2
        else:
            c0 = 3 * c0 + 1
        steps += 1
        print(c0, end=' ')

    return steps

# Test the program with the provided data
initial_number = int(input("Enter a natural number: "))
print("Intermediate values of c0:")
print(initial_number, end=' ')
total_steps = collatz_hypothesis(initial_number)
print("\nNumber of steps needed:", total_steps)
