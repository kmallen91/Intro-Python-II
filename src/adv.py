from room import Room
from player import Player
from item import Item


# Items
item = {
    'sword': Item('sword', 'Pointy!'),
    'cup': Item('cup', 'Discarded cup'),
    'helmet': Item('helmet', 'Armor for your head!'),
    'coins': Item('coins', 'Shiny!')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", items={item['sword'], item['coins']}),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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
player1 = Player('Adventurer', 'outside')

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

current_room = room[player1.current_room]
room_name = current_room.name
room_desc = current_room.description
directions = ['n', 's', 'e', 'w']


while True:
    items = current_room.items
    print(f'---------------------------------------------------------------------------')
    print(f'{player1.name} is currently in the {current_room.name}.')
    print(f'{current_room.description}')
    if len(items) > 0:
        for item in items:
            print(
                f'You find {item.name} in the room. ')
    print(f'Use "get" to pick items up. Use "drop" to drop items.')
    print(f'---------------------------------------------------------------------------')
    cmd = input(
        f'Please select a direction ([N], [E], [S], [W]) or [Q] to quit  ')
    if cmd.lower() in directions:
        if getattr(current_room, f'{cmd.lower()}_to') == None:
            print(
                f'---------------------------------------------------------------------------')
            print('There is nothing in that direction')
            print(
                f'---------------------------------------------------------------------------')
        else:
            current_room = getattr(current_room, f'{cmd.lower()}_to')

    elif cmd == "q":
        print('Goodbye!')
        break
    else:
        print(
            f'Command not found, please select a direction ([N], [E], [S], [W]) or [Q] to quit   ')
