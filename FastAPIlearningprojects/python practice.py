def greet():
    return ("Hello")

print(greet())

def greet(name,age):
    return (f"Hello {name}, You are {age} years")
print(greet("Limo",18))

def share():
    content = input("What would you like to share? ").strip()
    if content:
        print(f"You shared: {content}")
    else:
        print("Nothing to share.")

def choose_operation():
    print("Operations available:\n1.Share\n2.Read")
    while True:
        operation = input("Enter operation: ")
        try:
            operation = int(operation)
        except ValueError:
            print("Please enter a valid number.")
            continue

        if operation == 1:
            share()
        elif operation == 2:
            print("Read is not available yet.")
        else:
            print("Please choose 1 or 2.")

print(choose_operation())