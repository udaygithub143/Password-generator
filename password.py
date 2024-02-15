import random
import string
 
def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password
 
def main():
    num_passwords = int(input("How many passwords do you want to generate? "))
    password_length = int(input("Enter the length of each password: "))
 
    passwords = [generate_password(password_length) for _ in range(num_passwords)]
 
    print("\nGenerated Passwords:")
    for password in passwords:
        print(password)
 
if __name__ == "__main__":
    main()