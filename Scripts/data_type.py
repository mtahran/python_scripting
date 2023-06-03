my_strings= "Hello-World!"
print(type(my_strings))
print(my_strings.split('-'))
my_integer= 123
print(type(my_integer))


name = "Mustafa"
print("My name is " + name)
print("My name is %s" % name)
print("My name is {}".format(name))
print(f"My name is {name}")

name = input("What is your Name: ")
print( "Hello there {name}")

print(dir(my_list)) >> it gives the help, ie options.
my_strings= "123"
my_integer= int(my_strings)
print(type(my_integer))

my_list = ['adam' , 'humeyra' , 'fatih']
print(type(my_list))
print(my_list[2])
my_list.append('suma')
print(my_list)

pet = {'name':'cookie' , 'age':'2' , 'home':'Chicago'}
print(type(pet))
print(pet['name'], pet['home'])

pets = [
{'name':'cookie' , 'age':'2' , 'home':'Chicago', 'kind':'cat', 'toys':["bunny","ball"]},
{'name':'jessie' , 'age':'5' , 'home':'Turkey', 'kind':'dog', 'toys':["bunny","ball"]}
]
print(pets)
print(pets[1]['toys'][0])

for pet in pets:
    if pet ['name'] == 'cookie':
        print('My Pet is here!')





