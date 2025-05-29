# A simple program to sum user-provided integers.

def get_integer(prompt, min_value=1, max_value=100):
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def main():
    n = get_integer("How many numbers would you like to sum? (1-100): ")
    numbers = []
    print(f"Enter {n} integers:")
    for i in range(n):
        num = get_integer(f"  Number {i+1}: ", min_value=-1_000_000, max_value=1_000_000)
        numbers.append(num)
    total = sum(numbers)
    print(f"Sum of the numbers: {total}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram terminated by user.")
