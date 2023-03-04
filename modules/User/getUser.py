def execute(username: str):
    try:
        f = open(f"data/users/{username}_user.json", 'r')
        
        user = f.read()

        f.close()

        return user
    except:
        raise Exception("The specified file does not exist, and cannot be readed")
        
    
    