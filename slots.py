import random,os,toml
from time import sleep
data = {}
with open("data.toml") as f:
    data = toml.loads(f.read())
username, money,debugEnabled = data['name'], data['money'],data['debug']
gainMoney,purchase = 100,25
print(f"Welcome to a classic roll the dice game, {username}. Type 'roll' to roll the slots. Type 'money' to see your money.\nIt costs ${purchase} to roll the dice.\nNumber rewards:\n  1-6: You lose. Nothing happens.\n  7: That's the jackpot. The reward varies per day. Currently it is ${jackpot}.\n  8-12: You win. You earn ${gainMoney}.")
def getinput(money,debugEnabled):
    cmd = input(">>> ").lower().split(" ")
    if cmd[0] == "roll":
        money = roll(money)
    elif cmd[0] == "money":
        print(money)
    # START OF DEBUG COMMANDS
    elif cmd[0] == "debug-enable":
        debugPrompt = input("Are you sure you want to enable debug commands?\n  1: Yes.\n  2: No.")
        if debugPrompt == "1":
            print("Debug commands enabled. Type 'debug-help' for debug commands or type 'debug-disable' to disable them.")
            debugEnabled = True
    elif cmd[0] == "debug-disable":
        debugPrompt = input("Are you sure you want to disable debug commands?\n  1: Yes.\n  2: No.")
        if debugPrompt == "1":
            print("Debug commands disabled. Type 'debug-enable' to re-enable.")
            debugEnabled = False
    elif cmd[0] == "debug-help":
        if debugEnabled:
            print("Current debug commands:\n  debug-enable: enables debug commands\n  debug-disable\n  debug-help: displays this message\n  add-money <num>: adds 'num' to your current money \n  subtract-money <num>: subtracts num from your current money")
    elif cmd[0] == "add-money":
        if debugEnabled:
            num = int(cmd[1])
            money += num
    elif cmd[0] == "subtract-money":
        if debugEnabled:
            num = int(cmd[1])
            money -= num
    elif cmd[0] == "save":
        with open("data.toml","w") as f:
            toml.dump({'username': username,'money': money,'debug': debugEnabled},f)
            print("Saved game.")
    elif cmd[0] == "exit":
        with open("data.toml","w") as f:
            toml.dump({'username': username,'money': money,'debug': debugEnabled},f)
            print("Saved game.")
        exit()
    elif cmd[0] == "help":
        print("Type one of the following commands to do the corresponding action:\n  help: Shows this message.\n  roll: Rolls the slots.\n  money: Prints your money.\n  exit: Exits the program.")
    return money
def roll(money):
    money -= purchase
    dice,dice1 = random.randint(1,6),random.randint(1,6) 
    num = dice + dice1
    print("Numbers: {0} {1}".format(dice,dice1))
    if num > 7 and num != 12:
        print("You won! You earned ${0}.".format(gainMoney))
        money += gainMoney
    elif num < 7: 
        print("You lost!")
    elif num == 7:
        print("You won the jackpot and got ${0}!".format(jackpot))
        money += jackpot
    return money
while True:
   money = getinput(money,debugEnabled)