def userValidator(user) -> str | bool:
    if(type(user['name']) != str):
        return False
    if(type(user['age']) != int):
        return False
    if(type(user['email']) != str):
        return False
    return True