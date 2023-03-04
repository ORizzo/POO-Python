from modules.User import createUser, updateUser, getUser, deleteUser

class User():
    def __init__(self, name: str, age: int, email: str) -> None:
        self.user = {
            "name": name,
            "age": age,
            "email": email
        }
    def create_user(self):
        content = createUser.execute(self.user)
        return content
    def update_user(self):
        content = updateUser.execute(self.user, {
            "name": "updated name",
            "age": 18,
            "email": 'updated email'
        })
        return content
    def get_user(self):
        username = self.user['name']
        content = getUser.execute(username)
        return content
    def delete_user(self):
        content = deleteUser.execute(self.user)
        return content


user = User("henrique", 18, 'gmail')

print(user.update_user())
print(user.get_user())
    

