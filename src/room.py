# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.n_to = None
        self.e_to = None
        self.s_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        return f'{self.name} {self.description}'

    def display_items(self, items):
        if len(self.items) > 0:
            for item in self.items:
                print(
                    f'You find {item.name} in the room. {item.description} ')
            print(f'Use "get" to pick items up. Use "drop" to drop items.')
