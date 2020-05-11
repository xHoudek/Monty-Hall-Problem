# Xander Houdek
# 05/10/20

from random import randint

class MontyHall:
    """Recreates the Monty Hall Problem, with methods to model switching doors
    and keeping doors."""

    def __init__(self):
        self.doors = [False, False, False]
        self.selection = None

    def scenario_setup(self):
        self.doors[randint(0, 2)] = True  # add winner to random door
        self.selection = randint(0, 2)    # player selects a random door

        # remove a False door
        for index in [0, 1, 2]:
            if self.doors[index] is False and index != self.selection:
                del self.doors[index]
                if self.selection > index:
                    self.selection -= 1
                return True

    def switch_doors(self):
        if self.selection == 0:
            self.selection = 1
        else:
            self.selection = 0

    def reveal_door(self):
        return self.doors[self.selection]


def main():

    # keep same door
    numerator = 0
    for _ in range (10000):
        mh = MontyHall()
        mh.scenario_setup()
        result = mh.reveal_door()
        if result is True:
            numerator += 1
    keep_percentage = numerator / 10000

    #switch doors
    numerator = 0
    for _ in range (10000):
        mh = MontyHall()
        mh.scenario_setup()
        mh.switch_doors()
        result = mh.reveal_door()
        if result is True:
            numerator += 1
    switch_percentage = numerator / 10000

    # print results
    print("Keep percentage: " + str(keep_percentage) + "%")     # should be ~33%
    print("Switch percentage: " + str(switch_percentage) + "%") # should be ~50%


if __name__ == "__main__":
    main()