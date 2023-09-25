class User:
    class UserSet:
        def __init__(self):
            self.users = {}

        def __getitem__(self, key):
            return self.users[key]

        def add_user(self, user):
            self.users[user.username] = user

    # Avoid repetition of usernames
    taken_user_names = set()

    # a hash-map for users and another for admins
    users = UserSet()

    @staticmethod
    def add_to_database(username):
        with open("Database", "a") as file:
            file.write(username)

    def __init__(self, username, password):
        self._username = username
        self._password = password
        self._tasks = {}

        self.add_to_database(username)

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        self._username = username

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    @classmethod
    def check_unique(cls, username):
        while username in cls.taken_user_names:
            username = input("Please Enter another username as this one is taken: ").strip()

def main():
    pass

if __name__ == '__main__':
    main()