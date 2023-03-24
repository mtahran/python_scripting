# name = input("What is your Name: ")
# print(f"Hello {name}")
# age = input("What is your age: ")
# print(f"You look much younger!!!")
# job = input("What is your job: ")
# if job in ['doctor','engineer','businessman','economist']:
#     print(f"Wow! Good For You!")
# else:
#     print(f"Sorry for you :( You should find a better job!")

    #Also works this way:

# pets = []
# name = input("What is your Name: ")
# age = input(f"Hello {name} What is your age: ")
# job = input(f"You look much younger!!! What is your job: ")
# if job in ['doctor','engineer','businessman','economist']:
#     print(f"Wow! Good For You!")
# else:
#     print(f"Sorry for you :( You should find a better job!")

# pet = input("Do you have any pets: Y or N")
# pet_name = input("What is its name: ")
# if pet in ['y', 'Y', 'yes', 'yep', 'for sure', 'totally']:
#     pets.append(pet_name)
#     print(f"{name} has a pet named {pet_name}!")
# else:
#     print(f"{name} doesn't have a pet 🙁")

# print(pets)



family=[]
Name = input("What is your Name: ")
wife = input(f"OK {Name}. What is your Wife's name: ")
child_1 = input("OK Good. What is 1.Child's name: ")
child_2 = input("OK Good. What is 2.Child's name: ")
family.append(Name)
family.append(wife)
family.append(child_1)
family.append(child_2)

print(f"{family} make a good family!")

print(type(family))