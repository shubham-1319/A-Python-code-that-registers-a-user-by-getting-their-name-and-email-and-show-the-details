#made by shubham
def register_user():
    name = input("Enter your name: ")
    email = input("Enter your Gmail address: ")
    return name, email

def main():
    print("Welcome! Please register:")
    user_details = register_user()
    print("\nRegistration successful!")
    print("User Details:")
    print("Name:", user_details[0])
    print("Gmail:", user_details[1])

if __name__ == "__main__":
    main()
