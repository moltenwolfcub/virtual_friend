from os import name, stat_result
import random, time
from grammar import pluralise

names = []
name_words = []
animals = []
objects = []
statements = []
planets = []

numbers = list(range(1, 13))

def setup():
    """Opens up the data from the files and turns it into a list."""

    filename_names = "complex/data/names.txt"
    filename_name_statements = "complex/data/name_statments.txt"
    filename_animals = "complex/data/animals.txt"
    filename_objects = "complex/data/objects.txt"
    filename_statements = "complex/data/stand_alone_statements.txt"
    filename_planets = "complex/data/planets.txt"

    with open(filename_names) as f:
        for line in f:
            names.append(line.strip())

    with open(filename_name_statements) as f:
        for line in f:
            name_words.append(line.strip())

    with open(filename_animals) as f:
        for line in f:
            animals.append(line.strip())

    with open(filename_objects) as f:
        for line in f:
            objects.append(line.strip())

    with open(filename_statements) as f:
        for line in f:
            statements.append(line.strip())

    with open(filename_planets) as f:
        for line in f:
            planets.append(line.strip())

def words(number):
    """Prints a grammatically correct statement based off of the pre-built lists and the number provided."""

    if number == 1:
        print(f"{random.choice(names)} {random.choice(name_words)}")
    
    elif number == 2:
        anichoice = random.choice(animals)
        if anichoice[0].lower() in "aeiou":
            print(f"{random.choice(names)} is an {anichoice}")
        
        else:
            print(f"{random.choice(names)} is a {anichoice}")

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

def main():
    """The main loop of the 'AI'. """

    setup()
    while True:
        randomnum = random.choice(numbers)

        words(randomnum)
    
        time.sleep(2)


main()
