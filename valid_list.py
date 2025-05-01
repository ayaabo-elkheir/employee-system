def validuser(name, password):
    users = [{"name": "aya", "pass": "123"},
        {"name": "ahmed", "pass": "456"}]
    
    name = name.lower()

    for user in users:
        if user["name"] == name and user["pass"] == password:
            return True
    return False



user_name = input("enter yr name")
user_password = input("enter yr pass")

if validuser(user_name, user_password):
    print("valid")
else:
    print("invalid")