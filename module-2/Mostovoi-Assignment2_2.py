"""CSD-325 Module 2.2: Countdown program for debugging."""

def countdown(bottles):
    while bottles > 0:
        unit = "bottle" if bottles == 1 else "bottles"
        print(f"{bottles} {unit} of beer on the wall")
        bottles -= 1
    print("Time to buy more beer!")


def main():
    number = int(input("Enter number of bottles: "))
    countdown(number)


if __name__ == "__main__":
    main()
