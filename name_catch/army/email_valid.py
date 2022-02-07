import re

def main():
    print("Regex checker active")
    email = input("Enter your email: ")
    re.match('^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$', email)
    
if __name__ == "__main__":
    main()