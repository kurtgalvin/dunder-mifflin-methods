# main

class Manager:
    salary = 60000

    def __init__(self, name):
        self.name = name.lower()


bob = Manager('Bob')
joe = Manager('Joe')

print(bob.name)
print(bob.salary)
print('---')
print(joe.name)
print(joe.salary)