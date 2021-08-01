name = ["a","b","c","d"]
while True:
    user = input("Enter your name->")
    if user in name:
        print("Hello"+user)
        print("Would you like to resign")
        if input() =="Y":
            name.pop(name.index(user))
            print("Resign successful")
        break

    
