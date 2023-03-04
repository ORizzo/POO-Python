import os

def execute(user):
    try:
        os.remove(f"data/users/{user['name']}_user.json")
        return "The file is successfully deleted"
    except:
        raise Exception("The specified file does not exist, and cannot be deleted") 
    