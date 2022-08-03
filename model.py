import json


class Model:
    file = 'users.json'

    def check_email(self, email, all_users_data):
        for user in all_users_data:
            if email == user['email']:
                return True
        return False

    # functions which used for adding users to user.json
    def user_add(self):
        user = {
            "first_name": input("First Name: "),
            "last_name": input("Last Name: "),
            "email": input("Email: "),
            "number_of_cars": input("Number of cars: "),
            "cars": []
        }
        for i in range(int(user["number_of_cars"])):
            user["cars"].append(input("Car " + str(i + 1) + ": "))

        file = open('database/users.json', 'r')
        all_users_data_json = file.read()
        all_users_data = json.loads(all_users_data_json)
        file.close()
        if len(all_users_data) > 0:
            user['id'] = all_users_data[-1]['id'] + 1
        else:
            user['id'] = 1
        if self.check_email(user['email'], all_users_data) == False:
            all_users_data.append(user)
            with open('database/users.json', 'w') as file:
                file.write(json.dumps(all_users_data))
        else:
            print("User with this email already exist!!!")

    def get_all(self):
        with open('database/users.json', 'r') as file:
            users = json.loads(file.read())
            for user in users:
                print("User #" + str(user['id']))
                print("First Name: " + user['first_name'])
                print("Last Name: " + user['last_name'])
                print("Email: " + user['email'])
                for car in user['cars']:
                    print("Car: " + car)

    def search_by(self, search_str, what_to_search):
        with open('database/users.json', 'r') as file:
            users = json.loads(file.read())
            for user in users:
                if str(user[what_to_search]).lower() == str(search_str).lower():
                    print("User #" + str(user['id']))
                    print("First Name: " + user['first_name'])
                    print("Last Name: " + user['last_name'])
                    print("Email: " + user['email'])
                for car in user['cars']:
                    if car == str(search_str):
                        print("User #" + str(user['id']))
                        print("First Name: " + user['first_name'])
                        print("Last Name: " + user['last_name'])
                        print("Email: " + user['email'])
                        for i in user['cars']:
                            print("Car: " + i)

    def update_user(self):
        file = open('database/users.json', 'r')
        users = json.loads(file.read())
        file.close()
        id = int(input("Type id of user which you want to update: "))
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        email = input("Email: ")
        number_of_cars = input("Number of cars: ")
        cars = []
        for i in range(int(number_of_cars)):
            cars.append(input(("Car " + str(i + 1) + ": ")))
        for user in users:
            if user['id'] == id:
                user['first_name'] = first_name
                user['last_name'] = last_name
                user['email'] = email
                user['number_of_cars'] = number_of_cars
                user['cars'] = cars

        with open('database/users.json', 'w') as file:
            file.write(json.dumps(users))