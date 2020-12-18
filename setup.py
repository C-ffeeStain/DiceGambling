username = input("What's your username? ")
with open("info.txt","w") as f:
    f.write(f"name = \"{username}\"\nmoney = \"100\"\ndebug = \"false\"")