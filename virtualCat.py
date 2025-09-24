from colorama import init as colorama_init
from colorama import Fore
from colorama import Style

colorama_init()

class virtualCat:
    def __init__(self, name):
        self.name = name
        self.weight = 300
        self.hunger = 1

    def legend(self):
        print('\nStats explained:\n')
        print('WEIGHT: \n - Every time the cat gets fed its weight goes up by 30 grams. Every time it indulges in playtime, it loses 5 grams. \n - Be sure to keep an eye on it!\n')
        print("HUNGER: \n - If the hunger is below 5 it means that your cat is hungry. Feed it until hunger reaches 5 - that's how you know your cat is well fed! \n - Every time you play with your cat, its hunger goes down, which means it can be fed again.")
    
    def play(self):

        if self.hunger > 1:
            self.hunger = self.hunger - 1
            self.weight = self.weight - 5

            print(Fore.LIGHTYELLOW_EX + '\n' + self.name + ' is playing...\n' + Style.RESET_ALL)
            print(' /' + '\\' + '_/' + '\\')
            print('(˶ᵔᵕᵔ˶)')
            print('/ > < \\~⁠♡')
        else:
            print(Fore.LIGHTYELLOW_EX + '\nYou cannot play with your cat - needs to be fed first. Hunger levels are too low.\n' + Style.RESET_ALL)

            print('   ／＞    フ')
            print('   |   _  _| ')
            print('  ／`ミ＿xノ') 
            print(' /       |')
            print('/   ヽ   ﾉ')  

    def feed(self):
        if self.hunger <= 4:
            self.hunger = self.hunger + 1
            self.weight = self.weight + 30
            print(f'\n{Fore.LIGHTYELLOW_EX}{self.name} is eating...{Style.RESET_ALL}\n')

            print(' ∧,,,∧')
            print('( • ·•)')
            print('/    づ♡')

        else:
            print(Fore.LIGHTYELLOW_EX + '\nCat is full\n' + Style.RESET_ALL)
            print(' /' + '\\' + '_/' + '\\')
            print("*' - '*")



    def showStats(self):
        print(' ∧,,,∧')
        print('( • ·•)')
        print('/    づ \n')
        print("STATS")
        print("+--------+----------+----------+")
        print(f'|  name  |  weight  |  hunger  |')
        print("+--------+----------+----------+")
        print(f'| {self.name}   | {self.weight}      |  {self.hunger}       |')
        print("+--------+----------+----------+")
        print("")



class menu:
    def __init__(self,currentCat):
        self.currentCat = currentCat
        self.menuDict = {0:'Exit Game', 1:'Help', 2:'Play', 3:'Feed', 4:'Show Stats'}
    
    def main(self):
        while True:
            print('\n\n--------------\n' + Fore.MAGENTA + 'Main Menu:' + Style.RESET_ALL)
            for option in range(0,len(self.menuDict)):
                print(str(option) + '. ' + self.menuDict[option])
            
            print('--------------\n')
            inpOption = int(input('\nChoice: '))

            if inpOption == 0:
                break
            else:
                self.inpOption = self.menuDict[inpOption]
                self.options()

    def options(self):
        if self.inpOption == self.menuDict[1]:
            self.currentCat.legend()

        elif self.inpOption == self.menuDict[2]:
            self.currentCat.play()

        elif self.inpOption == self.menuDict[3]:
            self.currentCat.feed()
            
        elif self.inpOption == self.menuDict[4]:
            self.currentCat.showStats()


#STORYLINE

print(Fore.BLUE + '\n˳✧ ༚* Virtual Cat' + Style.RESET_ALL)
print('\nWelcome! This is your virtual cat - a sweet pet for you to take care of!\n')
print(' ∧,,,∧')
print('( • ·•)')
print('/    づ')
print('First you have to name your cat!\n')

usrNameInp = input('Name: ')
cat1 = virtualCat(usrNameInp)

print('\nGreat! Your virtual cat has been named! Below you can read the initial stats of ' + cat1.name + ':\n')
cat1.showStats()

print(f'The hunger is below 5 - it means that {cat1.name} is hungry! Hurry up and feed them by choosing the right option in the menu:')

gameMenu = menu(cat1)
gameMenu.main()