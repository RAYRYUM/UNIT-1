#imports ;
import cmd
import textwrap
import sys
import time
import timeit
import os
from timeit import default_timer as timer
import random

screen_width = 100

def print_text(text, char_wait, line_wait):
    #### Time btwn each character ####
    if char_wait == "short":
        char_wait = 0.01
    elif char_wait == "long":
        char_wait = 0.1
    else:
        char_wait = 0.05  # normal

    #### Time btwn this line and the next ####
    if line_wait == "short":
        line_wait = 0.25
    elif line_wait == "long":
        line_wait = 2
    else:
        line_wait = 0.5  # normal

    #### Writing the line ####

    for character in text:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(char_wait)
    time.sleep(line_wait)

##### player setup ######
class player:
    def __init__(self):
        self.name =''
        self.hp = 0
        self.score = 0
        self.location = 'b1'
        self.game_over = False

Myplayer = player()

#### title screen ####

def title_screen_selections():
    option = input(">")
    if option.lower() == ("play"):
        setup_game()
    if option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play','help','quit']:
        print("Please enter valid command.")
        option=input("> ")
        if option.lower() == ("play"):
            setup_game()
        if option.lower() == ("help"):
            help_menu()
        elif option.lower() == ("quit"):
            sys.exit()


####title screen###

def title_screen():
    os.system('clear')
    print('#########################')
    print('# Welcome to GAMENAME ! #')
    print('#########################')
    print('         -play-          ')
    print('         -help-          ')
    print('         -quit-          ')
    print('  Copyright 2021 161.me  ')
    title_screen_selections()

def help_menu():
    os.system('clear')
    print('#########################')
    print('# Welcome to GAMENAME ! #')
    print('#########################')
    print('-Type your commands to choose')
    print('-use look to inspect something')
    print('-GLHF!                   ')
    title_screen_selections()

### game functionallity ###



ZONENAME = ''
DESCRIPTION = 'DESC'
EXAMINATION = 'INFO'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'

solved_places = {
                'a1':False, 'a2':False,'a3':False,'a4':False,'a5':False,
                'b1':False, 'b2':False,'b3':False,'b4':False,'b5':False,
                'c1':False, 'c2':False,'c3':False,'c4':False,'c5':False,
                'd1':False, 'd2':False,'d3':False,'d4':False,'d5':False,
                }
zonemap = {
        'a1':{
            ZONENAME : 'SOUTH RIGHT WING ROAD',
            DESCRIPTION : 'A paved road.',
            EXAMINATION : "It's a paved road.",
            SOLVED : False ,
            UP : 'a2',
            DOWN : '',
            LEFT : '',
            RIGHT : 'b1',
        },
         'a2': {
             ZONENAME : 'FLOWER FIELD',
             DESCRIPTION : 'A field covered by thousands of florishing flowers.',
             EXAMINATION : 'It seems to never end over the horizon.',
             SOLVED : False ,
             UP : 'a3',
             DOWN : 'a1',
             LEFT : '',
             RIGHT : 'b2',
         },
         'a3': {
             ZONENAME : 'THE KICTHEN',
             DESCRIPTION : 'The kitchen that runs a little restaurant.',
             EXAMINATION : 'A very tempting smell comes out of the slightly open caged window.',
             SOLVED : False ,
             UP : 'a4',
             DOWN : 'a2',
             LEFT : '',
             RIGHT : 'b3',
         },
         'a4': {
             ZONENAME : 'RESIDENTIAL ROAD',
             DESCRIPTION : 'A road in the middle of a residential area.',
             EXAMINATION : "The road dosen't seem to derive and is strictly straight.",
             SOLVED : False ,
             UP : 'a5',
             DOWN : 'a3',
             LEFT : '',
             RIGHT : 'b4',
         },
         'a5': {
             ZONENAME : 'NORTH RIGHT WING ROAD',
             DESCRIPTION : 'A paved road.',
             EXAMINATION : "It's a paved road.",
             SOLVED : False ,
             UP : '',
             DOWN : 'a4',
             LEFT : '',
             RIGHT : 'b5',
         },
         'b0':{
             ZONENAME : """.̡̢͍̻̦̼̜̔́ͅh̸̨͚̼̥̝͈̮̼̞̎̍͌̈̄͡͝ẙ̸̙̗̮̦͖̽̃̓͛̕̕ a̢͕̘̲̻͓̫̱̼͑̈̉̀̔̄͝ṛ̨̛̮͙̫͇̪̟͂̏̏̄̍e̵͚̻͔̼͋͊̍́̀̽̄̚͢͞͝ y̸̞̦̜̠͆̊̓̎̂̇́͌͢͝ͅǫ̹̺̦̺͎̜̭͇͌̃̌͘͟͞͞u͔̘̲̰̹͓̗̓́̿̔͑͘͜͞ h̻̱̣͍͚̠̺̗̱̖͂̑͛̒̀̕e̸̡̫̼̜̹̊͛̐̐͡͠r̨̡̼͈͑̾̆̃͌̄͐͜͠͞e̷̡͙̱̩̊̓͒͗̅̓͗̐͟""",
             DESCRIPTION : "????" ,
             EXAMINATION : 'Home is the same. Nothing has changed.',
             SOLVED : False ,
             UP : 'b1',
             DOWN : '',
             LEFT : '',
             RIGHT : '',
         },
         'b1':{
             ZONENAME : 'HOME',
             DESCRIPTION : "Your home sweet home, where you've always been.",
             EXAMINATION : 'Home is the same. Nothing has changed',
             SOLVED : False ,
             UP : 'b2',
             DOWN : 'b0',
             LEFT : 'a1',
             RIGHT : 'c1',
         },
         'b2': {
             ZONENAME : 'CENTRAL ROAD FROM HOME',
             DESCRIPTION : "It's the central road.",
             EXAMINATION : "It's barricaded.",
             SOLVED : False ,
             UP : 'b3',
             DOWN : 'b1',
             LEFT : 'a2',
             RIGHT : 'c2',
         },
         'b3': {
             ZONENAME : 'THE INN',
             DESCRIPTION : 'A nice welcoming inn that has been here for as long as you can remember.',
             EXAMINATION : 'The exterior is decorated with pots with flowers. You can hear voices of people coming from inside.',
             SOLVED : False ,
             UP : 'b4',
             DOWN : 'b2',
             LEFT : 'a3',
             RIGHT : 'c3',
         },
         'b4': {
             ZONENAME : 'CENTRAL ROAD FROM INN',
             DESCRIPTION : "It's the central road. Again.",
             EXAMINATION : 'It is barricaded',
             SOLVED : False ,
             UP : 'b5',
             DOWN : 'b3',
             LEFT : 'a4',
             RIGHT : 'c4',
         },
         'b5': {
             ZONENAME : 'THE CASTLE',
             DESCRIPTION : 'The grand castle that can be seen from anywhere in town! How exciting!',
             EXAMINATION : 'It looks majestic as always, intimidating and magical even.',
             SOLVED : False ,
             UP : '',
             DOWN : 'b4',
             LEFT : 'a5',
             RIGHT : 'c5',
         },
         'c1':{
             ZONENAME : 'SOUTH LEFT WING ROAD',
             DESCRIPTION : 'A paved road.',
             EXAMINATION : "It's a paved road.",
             SOLVED : False ,
             UP : 'c2',
             DOWN : '',
             LEFT : 'b1',
             RIGHT : '',
         },
         'c2': {
             ZONENAME : 'BUS STOP',
             DESCRIPTION : 'Its a bus stop with a small resting place.',
             EXAMINATION : "Theres a timetable for the bus, but it's been all scratched up.",
             SOLVED : False ,
             UP : 'c3',
             DOWN : 'c1',
             LEFT : 'b2',
             RIGHT : '',
         },
         'c3': {
             ZONENAME : 'DAY CARE',
             DESCRIPTION : 'Its the local daycare. The building is painted colorfully and is surrounded by a playground.',
             EXAMINATION : "Today too, you hear the kid's screams as they play around.",
             SOLVED : False ,
             UP : 'c4',
             DOWN : 'c2',
             LEFT : 'b3',
             RIGHT : '',
         },
         'c4': {
             ZONENAME : 'CORNER SHOP',
             DESCRIPTION : 'Its the local shop.',
             EXAMINATION : 'You can buy everything and anything here!',
             SOLVED : False ,
             UP : 'c5',
             DOWN : 'c3',
             LEFT : 'b4',
             RIGHT : '',
         },
         'c5': {
             ZONENAME : 'NORTH LEFT WING ROAD',
             DESCRIPTION : 'A paved road.',
             EXAMINATION : "It's a paved road.",
             SOLVED : False ,
             UP : '',
             DOWN: 'c4',
             LEFT: 'b5',
             RIGHT: '',
         }
    }


###Game interactivity###

def print_location():
    print('\n'+('#'*(4+len(Myplayer.location))))
    print('# ' + Myplayer.location.upper() + ' #')
    print('# '+ zonemap[Myplayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(Myplayer.location))))
    time.sleep(0.15)


def player_move(myAction):
    ask="Where would you like to travel to? \n"
    dest = input(ask)
    if dest in ['up','north']:
        destination = zonemap[Myplayer.location][UP]
        movement_handler(destination)
    elif dest in ['left','west']:
        destination = zonemap[Myplayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['down','south']:
        destination = zonemap[Myplayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['right','east']:
        destination = zonemap[Myplayer.location][DOWN]
        movement_handler(destination)


def movement_handler(destination):
    os.system('clear')
    print("\n" + "========================")
    print('\n''you have travelled to',destination+'.')
    Myplayer.location = destination
    print_location()
    time.sleep(0.15)

def player_examine(action):
    os.system('clear')
    if zonemap[Myplayer.location][SOLVED]:
        print("You've already seen all  of  this... you move on.")
    else:
        print(zonemap[Myplayer.location][EXAMINATION])
    time.sleep(0.15)

def prompt():
        print("\n"+"========================")
        print("What would you like to do?")
        action = input('>')
        acceptable_actions = ['move','go','travel','walk','quit','examine','inspect','interact','look','t','i']
        while action.lower() not in acceptable_actions:
            print('unknown action, try again. \n')
            action = input('> ')
        if action.lower() == 'quit':
            sys.exit()
        elif action.lower() in ['move','go','travel','walk','t']:
            player_move(action.lower())
        elif action.lower() in ['examine','inspect','interact','look','i']:
            player_examine(action.lower())





### Game functionallity ###


def main_game_loop():
    while Myplayer.game_over is False:
        prompt()
        ##fill in later

def setup_game():
    os.system('clear')

    #name collector#
    question1 = "what is your name? \n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("> ")
    Myplayer.name = player_name

    Myplayer.hp = 160
    Myplayer.score = 100

    question3 = 'Welcome,',Myplayer.name
    for character in question3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)

    time.sleep(0.5)
    os.system('clear')
    print('\n''###################')
    print('#   Lets begin!   #')
    print('###################')
    main_game_loop()

title_screen()
