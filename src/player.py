# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room, inventory=[]):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory

    def __str__(self):
        return f'{self.name} {self.current_room}'

    def travel(self, direction):
        next_room = getattr(self.current_room, f'{direction}_to')
        if next_room is not None:
            self.current_room = next_room
        else:
            print(
                f'---------------------------------------------------------------------------')
            print('There is nothing in that direction')
            print(
                f'---------------------------------------------------------------------------')

    def get_item(self, current_room, inventory, item):
        self.inventory.append(item)
        self.current_room.items.remove(item)
        print(
            f'---------------------------------------------------------------------------')
        print(f'Inventory now contains {self.inventory[-1]}')

    def drop_item(self, current_room, inventory, item):
        items = []
        for thing in inventory:
            getattr(thing, 'name', 'description')
            items.append(thing.name)
        if item.name in items:
            self.current_room.items.append(item)
            self.inventory.remove(item)
        print(
            f'---------------------------------------------------------------------------')
        print(f'You have dropped {item.name}')

    def display_current_room(self, name, current_room):
        print(f'{self.name} is currently in the {self.current_room.name}.')
        print(f'{self.current_room.description}')
