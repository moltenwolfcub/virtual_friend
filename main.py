import random, time

def pluralise(word):
    stay_same = ["sheep", "deer", "series", "species"]
    
    if word in stay_same:
        return(word)
        
    elif word[-1].lower() in ["s", "x", "z", "o"]:
        return(f"{word}es")

    elif word[-1].lower() == "f":
        return(f"{word[:1]}ves")

    elif word[-1].lower() == "y" and word[-2].lower() in "aeiou":
        return(f"{word}s")

    elif word[-1].lower() == "y" and word[-2].lower() not in "aeiou":
        return(f"{word[:-1]}ies")
    
    elif word[-1].lower() == "s" and word[-2].lower() == "u":
        return(f"{word[:-2]}i")
    
    elif word[-1].lower() == "s" and word[-2].lower() == "i":
        return(f"{word[:-2]}es")

    elif word[-1].lower() == "n" and word[-2].lower() == "o":
        return(f"{word[:-2]}a")
    
    else:
        return(f"{word}s")


names = [
    "Steve"
]
name_words = [
    "is amazing"
]
animals = [
    "pig"
]
objects = [
    "nuclear bomb"
]
statements = [
    "How long do I have to wait?"
]
planets = [
    "Neptune"
]

numbers = list(range(1, 13))

#def setup():
#    """Opens up the data from the files and turns it into a list."""
#
#    filename_names = "data/names.txt"
#    filename_name_statements = "data/name_statments.txt"
#    filename_animals = "data/animals.txt"
#    filename_objects = "data/objects.txt"
#    filename_statements = "data/stand_alone_statements.txt"
#    filename_planets = "data/planets.txt"
#
#    with open(filename_names) as f:
#        for line in f:
#            names.append(line.strip())
#
#    with open(filename_name_statements) as f:
#        for line in f:
#            name_words.append(line.strip())
#
#    with open(filename_animals) as f:
#        for line in f:
#            animals.append(line.strip())
#
#    with open(filename_objects) as f:
#        for line in f:
#            objects.append(line.strip())
#
#    with open(filename_statements) as f:
#        for line in f:
#            statements.append(line.strip())
#
#    with open(filename_planets) as f:
#        for line in f:
#            planets.append(line.strip())

def words(number):
    """Prints a grammatically correct statement based off of the pre-built lists and the number provided."""

    if number == 1:
        print(f"{random.choice(names)} {random.choice(name_words)}")
    
    elif number == 2:
        anychoice = random.choice(animals)
        if anychoice[0].lower() in "aeiou":
            print(f"{random.choice(names)} is an {anychoice}")
        
        else:
            print(f"{random.choice(names)} is a {anychoice}")

    elif number == 3:
        print(f"{random.choice(names)} likes {pluralise(random.choice(animals))}")

    elif number == 4:
        print(f"{random.choice(names)} owns a {random.choice(objects)}")

    elif number == 5:
        print(f"A {random.choice(objects)} looks like a {random.choice(objects)}")

    elif number == 6:
        print(f"I wonder what would happen if I gave {random.choice(names)} a {random.choice(objects)}")

    elif number == 7:
        print(f"{random.choice(statements)}")

    elif number == 8:
        print(f"{random.choice(names)} dislikes {random.choice(names)}")

    elif number == 9:
        print(f"Imagine {random.choice(names)} dressed up as a {random.choice(animals)}")

    elif number == 10:
        print(f"{random.choice(names)}>{random.choice(names)}")

    elif number == 11:
        print(f"{random.choice(names)}<{random.choice(names)}")

    elif number == 12:
        print(f"{random.choice(planets)} is the best!")

    elif number == 13:
        print(f"Hello, {random.choice(names)}")

    elif number == 14:
        answer = input("What is your name?")
        names.append(answer)
        print(f"Hello, {answer}. \n you're name is now in my database.")

def main():
    """The main loop of the 'AI'. """

    #setup()
    while True:
        randomnum = random.choice(numbers)

        words(randomnum)
    
        time.sleep(2)


main()
