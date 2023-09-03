from collections import namedtuple

animals = set()
Animal = namedtuple('Animal', ['name', 'kind', 'size'])
animals.add(Animal("Scooby", "dog", "big"))
animals.add(Animal("Fluffy", "cat", "medium"))
animals.add(Animal("Marvin", "mouse", "small"))
animals.add(Animal("Hedwig", "bird", "medium"))
animals.add(Animal("Tweety", "bird", "small"))
animals.add(Animal("Scabbers", "rat", "small"))
animals.add(Animal("Jumbo", "elephant", "huge"))

people = set()
Person = namedtuple('Person', ['name', 'age'])
people.add(Person("Agatha", "old"))
people.add(Person("Harry", "young"))
people.add(Person("Shaggy", "middle-aged"))
people.add(Person("Daphne", "middle-aged"))
people.add(Person("Sylvia", "young"))
people.add(Person("Ron", "old"))

pets = set()
Pet = namedtuple('Pet', ['owner', 'animal'])
pets.add(Pet("Shaggy", "Scooby"))
pets.add(Pet("Harry", "Hedwig"))
pets.add(Pet("Sylvia", "Jumbo"))
pets.add(Pet("Agatha", "Fluffy"))
pets.add(Pet("Agatha", "Tweety"))
pets.add(Pet("Ron", "Scabbers"))
pets.add(Pet("Sylvia", "Marvin"))
pets.add(Pet("Daphne", "Muffin"))

def main():
    '''Uses set comprehensions to run queries'''
    # Query 1: What kinds of pets does Sylvia have?
    # Answer: Elephant and Mouse

    sylvia_pets = {Pet.animal for Pet in pets if Pet.owner == "Sylvia"}
    pet_kinds = {animal.kind for animal in animals if animal.name in sylvia_pets}
    print("Kinds of pets that Sylvia has: " + str(pet_kinds))

    # Query 2: What ages of people own small pets?
    # Answer: Young and Old

    smalls = {animal.name for animal in animals if animal.size == "small"}
    owners = {pet.owner for pet in pets if pet.animal in smalls}
    ages = {person.age for person in people if person.name in owners}
    print("Ages of small pet owners: "+ str(ages))

if __name__ == '__main__':
    main()