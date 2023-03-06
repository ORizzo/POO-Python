# Import modules for modules/User/
from modules.User import createUser, updateUser, getUser, deleteUser

# Declare User class (It's an object with methods)
class User():
    # Declare User class constructor (an method that will be called when the User class is initialized)
    def __init__(self, name: str, age: int, email: str) -> None:
        self.user = {
            "name": name,
            "age": age,
            "email": email
        }
    # Declare some methods that can modify User properties (name, age, email).
    # Self in class methods refers to the class properties => User -> user -> (name, age, email)/
    def create_user(self):
        try:
            createdUser = createUser.execute(self.user)
            return createdUser
        except Exception as exceptionInstance:
            return exceptionInstance
    def update_user(self):
        try:
            updatedUser = updateUser.execute(self.user, {
                "name": "updated name",
                "age": 18,
                "email": 'updated email'
            })
            return updatedUser
        except Exception as exceptionInstance:
            return exceptionInstance
    def get_user(self):
        try:
            username = self.user['name']
            user = getUser.execute(username)
            return user
        except Exception as exceptionInstance:
            return exceptionInstance
    def delete_user(self):
        try:
            deletedUser = deleteUser.execute(self.user)
            return deletedUser
        except Exception as exceptionInstance:
            return exceptionInstance

# Initiate a new user with User class constructor, with passed params
user = User("henrique", 18, 'gmail')

    

