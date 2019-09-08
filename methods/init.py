# __inti__ tutorial

class Manager:
    salary = 60000 # class attribute

    def __init__(self, name):
        self.name = name.lower() # instance attribute


bob = Manager('Bob')
joe = Manager('Joe')

print(bob.name)
print(bob.salary)
print('---')
print(joe.name)
print(joe.salary)