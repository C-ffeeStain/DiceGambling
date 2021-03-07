import random,os,toml,urllib.request
from time import sleep
data = {}
with open("data.toml") as f:
    data = toml.load(f)

help = """Type one of the following commands to do the corresponding action:
  help: Shows this message.
  roll: Rolls the slots.
  money: Prints your money.
  exit: Saves your money and then exits the program.
  save: Saves your money."""

debugHelp = """Current debug commands:
  debug enable: Enables debug commands.
  debug disable: Disables debug commands.
  debug help: Displays this message.
  debug add money <num>: Adds 'num' to your current money.
  debug subtract money <num>: Subtracts 'num' from your current money."""
with open("jackpot.txt") as j:
    jackpot = int(j.read())
username, money,debugEnabled = data['username'], data['money'],data['debug']
gainMoney,purchase = 100,25
print(f"Welcome to a classic roll the dice game, {username}. Type 'roll' to roll the slots. Type 'money' to see your money.\nIt costs ${purchase} to roll the dice.\nNumber rewards:\n  1-6: You lose. Nothing happens.\n  7: That's the jackpot. The reward varies per day. Currently it is ${jackpot}.\n  8-12: You win. You earn ${gainMoney}.")
def getinput(money,debugEnabled):
    cmd = input(">>> ").lower().split(" ")
    if cmd[0] == "roll":
        money = roll(money)
    elif cmd[0] == "money":
        print(money)
    # START OF DEBUG COMMANDS
    elif cmd[0] == "debug":
        print(debugEnabled)
        if cmd[1] == "enable":
            debugPrompt = input("Are you sure you want to enable debug commands?\n  1: Yes.\n  2: No.\n")
            if debugPrompt == "1":
                print("Debug commands enabled. Type 'debug-help' for debug commands or type 'debug-disable' to disable them.")
                debugEnabled = True
        elif cmd[1] == "disable":
            debugPrompt = input("Are you sure you want to disable debug commands?\n  1: Yes.\n  2: No.")
            if debugPrompt == "1":
                print("Debug commands disabled. Type 'debug-enable' to re-enable.")
                debugEnabled = False
        elif cmd[1] == "help":
            if debugEnabled:
                print(debugHelp)
        elif cmd[1] == "add" and cmd[2] == "money":
            if debugEnabled:
                num = int(cmd[1])
                money += num
        elif cmd[1] == "subtract" and cmd[2] == "money":
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
        print(help)
    return money,debugEnabled
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
   money, debugEnabled = getinput(money,debugEnabled)