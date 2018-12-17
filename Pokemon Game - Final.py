from time import sleep
Star = ("*"*80)

print (Star)
print ("")
print ("NOTE BEFORE STARTING:")
print ("Before starting, know that '[...]' at the end of a sentence means that you will have to click the [Enter] key in order to play the next line of code")
print ("ONLY FULL SCREEN ONCE THE MUSIC HAS STARTED PLAYING! The Python music player will be shown as '")

import pygame#pygame music
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((100,100))#640 380
pygame.draw.rect(screen,(50,205,50),pygame.Rect(0,0,100,100))
pygame.display.update()
pygame.mixer.music.load("Littleroot.wav")
pygame.mixer.music.play(-1)
print(pygame.mixer.get_busy())
sleep(1)
                                                                                                                                                                #UPDATE: idk what happened to the pokemon logo so just deal with it; too lazy to fix it
print ("")
print ("  .:XHHHHk.              db.   .;;.     dH  MX")
print ("oMMMMMMMMMMM       ~MM  dMMP :MMMMMR   MMM  MR      ~MRMN")
print ("QMMMMMb  'MMX       MMMMMMP IMX  :M~   MMM MMM  .oo. XMMM .MMM")
print ("  `MMMM.  )M> :X!Hk. MMMM   XMM.o'  .  MMMMMMM X?XMMM MMM>!MMP")
print ("   'MMMb.dM! XM M'?M MMMMMX.`MMMMMMMM~ MM MMM XM `' MX MMXXMM")
print ("    ~MMMMM~ XMM. .XM XM`'MMMb.~*?**~ .MMX M t MMbooMM XMMMMMP   <-- says Pokemon")
print ("     ?MMM>  YMMMMMM! MM   `?MMRb.    `'''   !L'MMMMM XM IMMM")
print ("      MMMX   'MMMM'  MM       ~%:           !Mh.''' dMI IMMP")
print ("      'MMM.                                             IMX")
print ("       ~M!M                                             IMP")
print ("NOT MADE BY ME ^")
print ("")
print (Star)
print ("Press [Start], aka. [Enter]")
input()

A = True
while A == True:

    answer = input ("Are you a boy or a girl?") #asking for legit genders
    if answer in ["Boy", "boy"]:
        A = False
        sleep (0.5)
    elif answer in ["girl", "Girl"]:
        A = False
        sleep (0.5)
    else:
        print ("What?")
        
        sleep (0.5)

B = True
while B == True:
    
    name = input("First, what is your name?") #ask for name
    

    sleep (0.5)


    answer = input("So "+ name +" is your name?") #check if input name is correct
    if answer == ("yes"):
        B = False
    elif answer == ("no"):
        B = True
    else:
        B = True

print ("Time to get started! [...]")
input()
print ("August 24th. You finally arrive at Pallet Town. You jump off the truck and smell the air. mm, nothing but the smell of trash. Probably because you're standing next to the trash can. [...]")
input()
print ("Mom:",name,"! You've finally arrived! [...]")
input()
print ("Mom: Quick, run to Professor Oak's labratory! He has something for you! [...]")
input()
pygame.mixer.music.stop()

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((100,100))#640 380
pygame.draw.rect(screen,(50,205,50),pygame.Rect(0,0,100,100))
pygame.display.update()
pygame.mixer.music.load("Oak.wav")
pygame.mixer.music.play(-1)
print(pygame.mixer.get_busy())

print ("You walk in and notice a familiar face [...]")

print("      ,,,,")
print("     /   '")
print("    /.. /")
print("   ( c  D")
print("    \- '\_")
print("     '-'W)W")
print("        I_ W       <--(It's your rival!)")
print("        |U \\")
print("       (__,//")
print("       |. \/")
print("       LL__I")
print("        |||")
print("        |||")
print("     ,,-``'W ")

sleep (1)

rival = input("Professor Oak: This is my grandson. He's been your rival since you were a baby. Erm, what is his name again?") #rival info

sleep (0.5)

print ("That's right! I remember now! His name is "+ rival +"! [...]")

input()

print (name +", your very own POKEMON legend is about to unfold! A world of dreams and adventures with POKEMON awaits! Let's go! [...]")

input()

print ("... Later on... [...]")

input()

print ("Oak: Now, "+ name +", which Pokemon do you want? [...]")

input()

print (rival +": Heh, I don't need to be greedy like you! Go ahead and choose, "+ name +"! [...]")

input()


D = True
while D == True:

    AA = input("Oak: Choose a Pokemon! There is Charmander, Bulbasaur, and Squirtle.") #choosing Pokemon
    if AA in ["Charmander", "charmander"]:
        D = False
        sleep (0.5)
    elif AA in ["Bulbasaur", "bulbasaur"]:
        D = False
        sleep (0.5)
    elif AA in ["Squirtle", "squirtle"]:
        D = False
    else:
        print ("I don't have that Pokemon.")
        
        sleep (0.5)

Pokemon = input("So what would you like to name it?")

reply = input("So! You want the "+ AA +", named "+ Pokemon +"?")
if reply in ["Yes", "yes"]:
        D = False
elif reply in ["No", "no"]:
        D = True
else:
        print ("I'm going to take that as a no.")
        D = True

sleep (0.5)

print ("Oak: This Pokemon is really energetic! [...]")

input()

print ("If a wild Pokemon appears, your Pokemon can fight against it! [...]")

input()

print (rival +": My Pokemon looks a lot stronger. [...]")

input()

print ("*You are attempting to leave to go back to your house...* [...]")

input()

print (rival +": Wait, "+ name +"! Let's check out our Pokemon! Come on, I'll take you on! [...]")

input()

pygame.mixer.music.stop()

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((100,100))#640 380
pygame.draw.rect(screen,(50,205,50),pygame.Rect(0,0,100,100))
pygame.display.update()
pygame.mixer.music.load("PStart.wav")
pygame.mixer.music.play(-1)
print(pygame.mixer.get_busy())

print ("*fancy Pokemon intro-fight scene that everybody knows* [...]")

sleep (0.5)

input()

E = True
while E == True:
    
    answer = input("What will "+ Pokemon +" do? [-Options-]: Fight, Bag, Pokemon, Run")#select pokemon moves based on Pokemon choice
    if answer in ["Fight", "fight"]:
        if AA == ("Charmander"):
            fightmoveC = input("[-scratch-]...[-growl-]... [---] ... [---]")
            if fightmoveC in ["Scratch", "scratch"]:
                sleep (0.5)
                print (Pokemon +"'s claws dug deep into "+ rival +"'s Pokemon and it fainted!")
                sleep(1)
                E = False
            elif fightmoveC in ["growl", "Growl"]:
                sleep (0.5)
                print (rival +"'s Pokemon got scared and fainted!")
                sleep(1)
                E = False
            else:
                print ("Can't do that")
                sleep (0.5)
                E = True

        elif AA == ("Bulbasaur"):
            fightmoveB = input("[-tackle-]...[-growl-]... [---] ... [---]")
            if fightmoveB in ["tackle", "Tackle"]:
                sleep (0.5)
                print (Pokemon +" broke the ribs of the "+ rival +"'s Pokemon and it fainted!")
                sleep(1)
                E = False
            elif fightmoveB in ["growl", "Growl"]:
                sleep (0.5)
                print (rival +"'s Pokemon got scared and fainted!")
                sleep(1)
                E = False
            else:
                print ("Can't do that")
                sleep(0.5)
                E = True

        elif AA == ("Squirtle"):
            fightmoveS = input("[-Tackle-]...[-Tail Whip-]... [---] ... [---]")
            if fightmoveS in ["tackle", "Tackle"]:
                sleep (0.5)
                print (Pokemon +" broke the ribs of the "+ rival +"'s Pokemon and it fainted!")
                sleep(1)
                E = False
            elif fightmoveS in ["tail whip", "Tail Whip", "Tail whip"]:
                sleep (0.5)
                print (rival +"'s Pokemon broke all its' teeth and it fainted!")
                sleep(1)
                E = False
            else:
                print ("Can't do that")
                sleep(0.5)
                E = True
                
    elif answer in ["bag", "Bag"]: #selected 'bag'
        E = True
        print ("You don't have any items...")
        sleep (0.5)
    elif answer in ["Pokemon", "pokemon"]:#selected 'pokemon'
        E = True
        print ("You don't have any other Pokemon...")
        sleep (0.5)
    elif answer in ["run", "Run"]:#selected 'run'
        print ("You can't run away from a trainer battle!")        
        E = True
        sleep (0.5)
    else:
        sleep (0.5)
        E = True

pygame.mixer.music.stop()

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((100,100))#640 380
pygame.draw.rect(screen,(50,205,50),pygame.Rect(0,0,100,100))
pygame.display.update()
pygame.mixer.music.load("PWon.wav")
pygame.mixer.music.play(-1)
print(pygame.mixer.get_busy())
print("You won! [...]")
input()

pygame.mixer.music.stop()

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((100,100))#640 380
pygame.draw.rect(screen,(50,205,50),pygame.Rect(0,0,100,100))
pygame.display.update()
pygame.mixer.music.load("Route101.wav")
pygame.mixer.music.play(-1)
print(pygame.mixer.get_busy())

sleep (0.5)
print (rival +": WHAT? Unbelievable! I picked the wrong Pokemon! [...]")

input()

print ("You know what? I'll make my Pokemon fight to toughen it up!")

sleep (1)

print (name +", Gramps! Smell you later! [...]")

input()

print("And so, your story as a Pokemon Trainer begins... [...]")

input()

print ("As you start your journey to Oldale City, you notice many signs: 'Watch out for wild pokemon!', and 'remember to catch pokemon with your Pokeballs! [...]'")

input()

print ("You are traversing across the trails. [...]")

input()

print ("*clunk* Hm? You reach down and pick up a bottle... It's a potion! [...]")

input()

pygame.mixer.music.stop()

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((100,100))#640 380
pygame.draw.rect(screen,(50,205,50),pygame.Rect(0,0,100,100))
pygame.display.update()
pygame.mixer.music.load("Item.wav")
pygame.mixer.music.play(1)
print(pygame.mixer.get_busy())

print ("    *Obtained the Potion! You can use it to heal 5HP!* [...]")
Potion = 1
input()

pygame.mixer.music.stop()

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((100,100))#640 380
pygame.draw.rect(screen,(50,205,50),pygame.Rect(0,0,100,100))
pygame.display.update()
pygame.mixer.music.load("Route101.wav")
pygame.mixer.music.play(-1)
print(pygame.mixer.get_busy())

print ("You are happily walking across the tall grass when suddenly! [...]")

input()

pygame.mixer.music.stop()

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((100,100))#640 380
pygame.draw.rect(screen,(50,205,50),pygame.Rect(0,0,100,100))
pygame.display.update()
pygame.mixer.music.load("PStart.wav")
pygame.mixer.music.play(-1)
print(pygame.mixer.get_busy())

print ("*Poof!* Wild pidgey appeared! It has 20HP, you have 22HP[...]")

input()

print ("Go! " +Pokemon+ "! [...]")

input ()

HP = 22
HPN = 20

H = True
while H == True:
        HP = HP-3
        print ("Wild PIDGEY used Tackle! You now have", HP ,"HP left. [...]")
        input()
        if HP <=0:
            print (Charmander+" fainted! [...]")
            input()
            H = False
        elif HP >0:
            sleep (1)
            answer = input("What will "+ Pokemon +" do? [-Options-]: Fight, Bag, Pokemon, Run")
            if answer == ("Fight"):
                sleep (0.4)
                if AA == ("Charmander"):
                    fightmoveC = input("[-scratch-]...[-growl-]... [---] ... [---]")
                    if fightmoveC in ["Scratch", "scratch"]:
                        sleep (0.5)
                        print (Pokemon +"'s attack hit Pidgey! [...]")
                        HPN = HPN - 7
                        input()
                        if HPN <= 0:
                            print ("Foe PIDGEY fainted!")
                            H = False
                        elif HPN >0:
                            print ("Pidgey now has", HPN, "HP left. [...]")
                            input()
                            H = True
                    elif fightmoveC in ["growl", "Growl"]:
                        sleep (0.5)
                        print ("PIDGEY got scared!")
                        if HPN <= 0:
                            print ("PIDGEY's attack decreased!")
                            H = False
                        elif HPN >0:
                            H = True
                    else:
                        print ("Can't do that")
                        sleep (0.5)
                        H = True

                elif AA == ("Bulbasaur"):
                    fightmoveB = input("[-tackle-]...[-growl-]... [---] ... [---]")
                    if fightmoveB in ["tackle", "Tackle"]:
                        sleep (0.5)
                        print (Pokemon +"'s attack hit Pidgey! [...]")
                        HPN = HPN - 5
                        input()
                        if HPN <= 0:
                            print ("Foe PIDGEY fainted!")
                            H = False
                        elif HPN >0:
                            print ("PIDGEY now has", HPN, "HP left. [...]")
                            input()
                            H = True
                    elif fightmoveB in ["growl", "Growl"]:
                        sleep (0.5)
                        print ("PIDGEY's attack decreased!")
                        if HPN <= 0:
                            print ("Foe Pidgey fainted!")
                            H = False
                        elif HPN >0:
                            H = True
                    else:
                        print ("Can't do that")
                        sleep(0.5)
                        H = True

                elif AA == ("Squirtle"):
                    fightmoveS = input("[-Tackle-]...[-Tail Whip-]... [---] ... [---]")
                    if fightmoveS in ["tackle", "Tackle"]:
                        sleep (0.5)
                        print (Pokemon +"'s attack hit Pidgey! [...]")
                        HPN = HPN - 6
                        input()
                        if HPN <= 0:
                            print ("Foe Pidgey fainted!")
                            H = False
                        elif HPN >0:
                            print ("PIDGEY now has", HPN, "HP left.")
                            H = True
                    elif fightmoveS in ["tail whip", "Tail Whip", "Tail whip"]:
                        sleep (0.5)
                        print (Pokemon +"'s attack hit Pidgey!")
                        sleep(1)
                        HPN = HPN - 4
                        print ("PIDGEY now has", HPN, "HP left. [...]")
                        input()
                        if HPN <= 0:
                            print ("Foe Pidgey fainted!")
                            H = False
                        elif HPN >0:
                            H = True
                    else:
                        print ("Can't do that")
                        sleep(0.5)
                        H = True
                
            elif answer in ["bag", "Bag"]:
                H = True
                if Potion == 1:
                    Drink = input ("You found a potion! Drink it?")
                    if Drink in ["Yes", "yes"]:
                        print ("You gave the potion to", Pokemon+"! "+Pokemon,"gained 5HP! [...]")
                        input()
                        HP = HP+5
                        Potion = 0
                    elif Drink in ["No", "no"]:
                        print ("You don't give", Pokemon, "the potion")
                        Potion = 1
                elif Potion == 0:
                    print ("You find an eraser. It won't do much good.")
                sleep (0.5)
            elif answer in ["Pokemon", "pokemon"]:
                H = True
                print ("You don't have any other Pokemon...")
                sleep (0.5)
            elif answer in ["run", "Run"]:
                print ("No. I won't let you. Simply because I want you to use the really long code I had to write")        
                H = True
                sleep (0.5)
            else:
                sleep (0.5)
                H = True

if HP <= 0:
    RevTime = True
else:
    Revtime = False
sleep (1)

pygame.mixer.music.stop()

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((100,100))#640 380
pygame.draw.rect(screen,(50,205,50),pygame.Rect(0,0,100,100))
pygame.display.update()
pygame.mixer.music.load("PWon.wav")
pygame.mixer.music.play(-1)
print(pygame.mixer.get_busy())
print("You won! [...]")

print ("Your first battle with a wild pokemon went well! [...]")

input ()

print ("You head down the trail path, into Oldale City. [...]")

input()

print ("You reached Oldale City. You stay to enjoy the music. [...]")
input()
pygame.mixer.music.stop()

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((100,100))#640 380
pygame.draw.rect(screen,(50,205,50),pygame.Rect(0,0,100,100))
pygame.display.update()
pygame.mixer.music.load("Oldale.wav")
pygame.mixer.music.play(-1)
print(pygame.mixer.get_busy())

sleep(1)
print (Star)
print ("")
print ("Thank you for playing my Pokemon game. Hope you enjoyed")
print ("")
print (Star)
