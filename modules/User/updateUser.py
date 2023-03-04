import json

from .validator import userValidator

def execute(user, newUser):
    f = open(f"data/users/{user['name']}_user.json", 'w')

    isValidUser = userValidator(newUser)

    if(isValidUser):
        f.write(json.dumps(newUser))
    else:
        f.close()
        raise Exception("The new user is not valid, check the informations") 
    f.close()

    return user         
        
    
    