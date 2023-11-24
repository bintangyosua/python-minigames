print('''
888                                888                           
888                                888                           
888                                888                           
888 .d88b. 888  888 .d88b. .d8888b 888888 .d88b. 888d888888  888 
888d88""88b888  888d8P  Y8b88K     888   d88""88b888P"  888  888 
888888  888Y88  88P88888888"Y8888b.888   888  888888    888  888 
888Y88..88P Y8bd8P Y8b.         X88Y88b. Y88..88P888    Y88b 888 
888 "Y88P"   Y88P   "Y8888  88888P' "Y888 "Y88P" 888     "Y88888 
                                                             888 
                                                        Y8b d88P 
                                                         "Y88P"  
''')

print("Welcome to Love Story World. You are gonna play a love story game which is so fun to play together with your crush or whatever it is.")

# Transportation
transportation = input("Which one do you like? drive a car or ride a motorcycle? (car/motorcycle) ")
if (transportation == "car"):
    print("You not gonna be wet if there is rain")
elif (transportation == "motorcycle"):
    print("You will be so freaking have a romantized moments")

# Place to go
place = input("Where do you wanna go? cinema or bookstore? ")
if (place == "cinema"):
    movie = input("Which one you wanna watch? (spiderman/dilan 1991/kimi no nawa) ")
    
    if (movie == "spiderman"):
        print("Spiderman is a good movie for action lover")
    elif (movie == "dilan 1991"):
        print("It's a romance movie. you'll have a good moment")
    elif (movie == "kimi no nawa"):
        print("It's a good movie. a combination of fantasy and romance")

book1 = "Sapiens"
book2 = "Start With Why"
book3 = "Detective Conan"
book4 = "The World According to Physic"

if (place == "bookstore"):
    book = input(f"What book do you wanna buy? ({book1}/{book2}/{book3}/{book4}) ")
    if (book == book1):
        print("its a good book to buy. you'll have a lot of insights about human being from this book :')")
    elif (book == book2):
        print("Why is the best question declaration coz it has a lot of meanings, it can answer a lot of another 4W & 1H")
    elif (book == book3):
        print("You must be a mystery lover")
    elif (book == book4):
        print("Physic is one of the best things in this world. it is learnt us about how this world is happening, what is going on in this world, why it was happen, etc")

print("\n")
