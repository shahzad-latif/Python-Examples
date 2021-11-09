class Car:
    pr = 0

    def __init__(self):
        print('This is constructor')
    
    def start(self):
        print('This is start')

    def price(self, p=0):
        self.pr = p
        print('Price = ', self.pr)

    def __del__(self):
        print('this is destructor')

class Honda(Car):
    mod = 'City'

    def model(self, m = 'City'):
        self.mod = m
        print('Model = ', self.mod)




v = Car()
v.start()
v.price()

h = Honda()
h.start()
h.price()
h.model()

h.price(100)
h.model('Civic')


