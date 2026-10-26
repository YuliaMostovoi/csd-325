"""CSD-325 Module 1.3: On the Wall.

Author: Yulia Mostovoi
Date: October 25, 2026
Purpose: Prompt for a starting bottle count, display the countdown song,
and remind the user to buy more beer after the countdown.
"""


def sing_countdown(starting_bottles):
    """Display each verse, counting from starting_bottles down to one."""
    for bottles in range(starting_bottles, 0, -1):
        if bottles == 1:
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down, pass it around, no more bottles of beer on the wall!\n")
        else:
            remaining = bottles - 1
            next_word = "bottle" if remaining == 1 else "bottles"
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            print(f"Take one down, pass it around, {remaining} {next_word} of beer on the wall!\n")


def main():
    """Request a positive integer, call the countdown, and display a reminder."""
    while True:
        try:
            bottle_count = int(input("How many bottles of beer are on the wall? "))
            if bottle_count < 1:
                print("Please enter a positive whole number.")
                continue
            break
        except ValueError:
            print("Please enter a valid whole number.")

    sing_countdown(bottle_count)
    print("Time to buy more beer!")


if __name__ == "__main__":
    main()
