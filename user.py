from model import Model


class User(Model):
    file = 'users.json'

    def __init__(self, first_name, last_name, email, id, number_of_cars, cars):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.id = id
        self.number_of_cars = number_of_cars
        self.cars = cars
