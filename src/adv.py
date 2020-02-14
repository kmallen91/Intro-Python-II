from room import Room
from player import Player
from item import Item


# Items
listed_items = {

    'sword': Item('Sword', 'Pointy!'),
    'cup': Item('Cup', "It's a rusty cup."),
    'helmet': Item('Helmet', 'Armor for your head!'),
    'coins': Item('Coins', 'Shiny!')
}


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items=[listed_items['sword'], listed_items['coins']]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", items=[listed_items['helmet']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", items=[listed_items['cup']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']

room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']

room['overlook'].s_to = room['foyer']

room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']

room['treasure'].s_to = room['narrow']


#
# Main
#

# Make a new player object that is currently in the 'outside' room.

player1 = Player(input("What is your name? "), room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


directions = ['n', 's', 'e', 'w']
actions = ['get', 'drop']


while True:
    current_room = player1.current_room
    items = current_room.items
    inventory = player1.inventory

    print(f'---------------------------------------------------------------------------')
    player1.display_current_room(player1.name, current_room)
    current_room.display_items(items)
    print(f'---------------------------------------------------------------------------')
    cmd = input(
        f'Please select a direction ([N], [E], [S], [W]) or [Q] to quit  ').lower().split(' ')

    if len(cmd) == 1:
        if cmd[0] in directions:
            player1.travel(cmd[0])
        elif cmd[0] == "q":
            print('Goodbye!')
            break
        else:
            print(
                f'Command not found, please select a direction ([N], [E], [S], [W]) or [Q] to quit   ')

    elif len(cmd) == 2 and cmd[0] in actions:
        item = cmd[1]
        print(item)
        if len(inventory) > 0:
            print(inventory.index(item))
        if len(items) > 0:
            if 'get' in cmd[0]:
                player1.get_item(current_room, inventory, listed_items[item])
        else:
            if 'drop' in cmd[0] and item in inventory.index(item).name:
                player1.drop_item(current_room, inventory, listed_items[item])
