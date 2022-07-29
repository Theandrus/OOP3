from model import Model


class Controller(Model):

    def menu(self):
        while True:
            print("1. Add New User\n"
                   + "2. Get All Users\n"
                   + "3. Search\n"
                   + "4. Update User By Id"
                  )
            break
        self.menu_flag = int(input("Type your choose: "))

    def create_user(self):
        if self.menu_flag == 1:
            self.user_add()

    def get_users(self):
        if self.menu_flag == 2:
            self.get_all()

    def search(self):
        if self.menu_flag == 3:
            what_to_search = input('By Which Parametr you want to search: ')
            search_str = input('Search: ')
            self.search_by(search_str, what_to_search)

    def update_user(self):
        if self.menu_flag == 4:
            super().update_user()

    def run(self):
        c = Controller()
        c.menu()
        c.create_user()
        c.get_users()
        c.search()
        c.update_user()