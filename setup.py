import re

username = input("What's your username? ")
if re.match("^\w+$",username):
    
    with open("data.toml","w") as f:
        f.write(f"""name = \"{username}\"
money = 100
debug = false""")
else:
    print("Your username can't have anything but letters, numbers, and the underscore.")