
import random

print("What is your Name")
n = input("")

print("| |__   __ _ _ __ _ __ _   _   _ __   ___ | |_| |_ ___ _ __   ")
print("| '_ \ / _` | '__| '__| | | | | '_ \ / _ \| __| __/ _ \ '__|    ")
print("| | | | (_| | |  | |  | |_| | | |_) | (_) | |_| ||  __/ |     ")
print("|_| |_|\__,_|_|  |_|   \__, | | .__/ \___/ \__|\__\___|_|     ")
print("                       |___/  |_|")

print(n + " Welcome to Hogwarts")
print("                   T~~      ")
print("                   |      ")
print("                  /*\     ")
print("          T~~     |'| T~~   ")
print("      T~~ |    T~ WWWW|      ")
print("      |  /*\   |  |  |/\T~~  ")
print("     /*\ WWW  /*\ |' |WW|   ")
print("    WWWWW/\| /   \|'/\|/*\  ")
print("    |   /__\/]WWW[\/__\WWWW ")
print("    |*  WWWW'|I_I|'WWWW'  | ")
print("    |   |' |/  -  \|' |'  | ")
print("    |'  |  |LI=H=LI|' |   | ")
print("    |   |' | |[_]| |  |'  |  ")
print("    |   |  |_|###|_|  |   | ")
print("     '---'--'-/___\-'--'---' ")


print("Time for the sorting ceremony")
print("")

print("            .")
print("           /:\ ")
print("          /;:.\ ")
print("         //;:. \ ")
print("        ///;:.. \ ")
print("  __--*////;:... \*--__")
print("--__   *--_____--*   __-- ")
print("    ***--_______--***")



h = random.randint(10, 100)
if (h % 3 == 0):
    print(" Your house is Gryffindor")
elif (h % 2 == 0):
    print("Your house is Hufflepuff")
elif (h % 5 == 0):
    print(" Your house is Ravenclaw")
else:
    print(" Your house is Slytherin")

c = ["Harry Potter", "Ronny Weasely", "Hermione Granger", "Remus Lupin", "Sirius Black", "Albus Dumbledore",
     "Fred Weasely", "Nymphadora Tonks", "Percy Weasely", "Severus Snape", "Tom Riddle", "Draco Malfoy",
     "Luna Lovegood", "Neville Longbottom", "Peter Pattigrew", "Dobby", "Rubeus Hagrid"]
ch = ["brave", "a loyal friend", "brilliant", "dedicated", "a righteous person", "an inspiration", "jocular", "daring",
      "disciplined", "loyal", "power hungry", "a misunderstood person", "innocent", "humble", "cunning", "cute",
      "good-at-heart"]
print("*********************************")
no = random.randint(0, 16)
nm = c[no]
chh = ch[no]
print("You are like " + nm)
print("You are  " + chh)
anim = ["doe", "unicorn", "dog", "hippogriff", "whale", "owl", "rat", "cat"]

print("Your animagus is a " + anim[random.randint(0, 7)])


s = ["Charms", "Transfiguration", "Potions", "Magical History", "Defence Against Dark Arts",
     "Care for Magical creatures", "Ancient Runes", "Herbology"]
subj = s[random.randint(0, 7)]
print("Your favourite subject is " + subj)

th = ["Professor Snape", "Professor Mcgonagall", "Professor Slughorn", "Professor Binns", "Professor Sprout",
      "Professor Lupin", "Madame Pomfrey"]
print("You will be a favourite of " + th[random.randint(0, 6)])
