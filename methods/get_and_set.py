# __get__ and __set__ tutorial

class Hours:
    def __init__(self, hours_per_day):
        self.hours_per_day = hours_per_day
        self.total_hours = 0
        self.regular_hours = 0
        self.overtime_hours = 0

    def __get__(self, instance, owner):
        return {
            'total': self.total_hours,
            'regular': self.regular_hours,
            'overtime': self.overtime_hours
        }

    def __set__(self, instance, value):
        self.hours_per_day = value

class Manager:
    hours = Hours(8)

    def __init__(self, name):
        self.name = name.lower()


michael = Manager('michael')
michael.