films = {
    "a":[3,5],
    "b":[18,5],
    "c":[15,5],
    "d":[12,5]
}
choice = input("Enter movie name:->").strip()
if choice in films:
    age =int(input("How old are you:->").strip())
    if age>= films[choice][0]:
        if films[choice][-1]>0:
            print("Go")
            films[choice][-1] -=1
            print("Enjoy the file")
    else:
        print("Film is not for you")
else:
    print("We dont have that film")

print(films)