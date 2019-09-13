# __call__ tutorial

class Pay:
    total_hours = 0
    total_pay = 0

    def __init__(self, hourly_wage):
        self.hourly_wage = hourly_wage

    def __call__(self, hours_worked):
        self.total_hours += hours_worked
        self.total_pay += hours_worked * self.hourly_wage
        return hours_worked * self.hourly_wage


pay = Pay(15)
print('Week 1:', pay.total_hours, pay.total_pay)
pay(8)
print('Week 2:', pay.total_hours, pay.total_pay)
pay(8)
print('Week 3:', pay.total_hours, pay.total_pay)


class Manager:
    pay = Pay(15)

    def __init__(self, name):
        self.name = name.lower()


michael = Manager('michael')
print('michael', michael.pay.total_hours, michael.pay.total_pay)
michael.pay(8)
print('michael', michael.pay.total_hours, michael.pay.total_pay)
michael.pay(8)
print('michael', michael.pay.total_hours, michael.pay.total_pay)