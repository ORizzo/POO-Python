import json

def execute(user):
    try:
        f = open(f"data/users/{user['name']}_user.json", 'x')
        
        f.write(json.dumps(user))

        f.close()
        return user
    except:
        return "The specified file already exists, and cannot be created"
        
    
    