import random 
import string

def generate_password(length, use_letters, use_numbers, use_symbols):
    """Generate a random password based on user-defined criteria."""
    # Define character sets
    letters = string.ascii_letters  # abcdef...XYZ
    numbers = string.digits  # 0123456789
    symbols = string.punctuation  # !@#$%^&*...

    # Create the character pool based on user preferences
    char_pool = ""
    if use_letters:
        char_pool += letters
    if use_numbers:
        char_pool += numbers
    if use_symbols:
        char_pool += symbols

    # Check if at least one character set is selected
    if not char_pool:
        return "Error: At least one character set (letters, numbers, symbols) must be selected."

    # Generate password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")

    # Get password length with validation
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 5): "))
            if length < 4:
                print("Password length must be at least 40 characters.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a numeric value for length.")

    # Get character set preferences
    use_letters = input("Include letters (y/n)? ").lower() == 'y'
    use_numbers = input("Include numbers (y/n)? ").lower() == 'y'
    use_symbols = input("Include symbols (y/n)? ").lower() == 'y'

    # Generate and display password
    password = generate_password(length, use_letters, use_numbers, use_symbols)
    print(f"\nYour generated password is: {password}")
    print("Keep it safe!")
    print("Thank you for using the Random Password Generator!")

if __name__ == "__main__":
    main()