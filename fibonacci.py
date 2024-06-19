#!/usr/bin/env python3

def fibonacci_generator(n):
    # Allocate variables for the first two Fibonacci numbers
    a, b = 0, 1

    # Generate Fibonacci sequence up to the nth number
    for _ in range(n):
        yield a
        a, b = b, a + b

def instructions():
    print("Instructions")
    print("**Cannot Generate Fibonacci for Fractional, Decimal, Real or Complex Numbers")
    print("**Cannot Generate Fibonacci for Negative values")
    print("**Cannot Generate Fibonacci for Zero")
    print("**Cannot Generate Fibonacci for Non-Numerical values\n")


def interface():
    while True:
        try:
            n = int(input("Enter the number of Fibonacci numbers to generate (0 to main menu): "))
            if n < 0:
                print("Please enter a non-negative integer.")
                continue
            elif n == 0:
                print("Exiting the calculator...")
                break
            else:
                # Generate Fibonacci numbers using the generator
                fib_gen = fibonacci_generator(n)
                fibonacci_numbers = list(fib_gen)

                # Print the generated Fibonacci numbers
                print("Generated Fibonacci numbers:", fibonacci_numbers,"\n")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def info():
    print("Developed by")
    print("Thelu Pavani")
    print("thelupavani41@gmail.com")
    print("www.linkedin.com/in/thelu-pavani-b9512b309")
    print("A mini project for CodeAlpha internship programme")


def main():
    while True:
        print("*** Welcome to the Fibonacci Number Generator mini app ***")
        print("Press 1 for Instructions")
        print("Press 2 for Fibonacci Calculator")
        print("Press 3 for Developer Info")
        print("Press 0 for Exit")
        try:
            x = int(input())
            if x == 1:
                instructions()
            elif x == 2:
                interface()
            elif x == 3:
                info()
            elif x == 0:
                print("Exiting the program... Goodbye...")
                break
        except ValueError:
                print("Invalid option. Please choose options from 1 to 3 or 0.")


if __name__ == "__main__":
    main()