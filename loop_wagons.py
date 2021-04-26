import random

STATEMENT_PHRASES = [
    "Well, of course!",
    "I knew it!",
    "Well it's finally over",
]


class Wagon:
    previous: None
    next: None
    light: bool
    number: int
    
    def __init__(self, number):
        self.light = random.choice([True, False])
        self.number = number
        
    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next

    def set_previous(self, previous):
        self.previous = previous

    def get_previous(self):
        return self.previous

    def set_light(self, light_onoff):
        self.light = light_onoff
        
    def get_light(self):
        return self.light


def make_loop_wagons():
    max_qty_wagons = input('enter the maximum number of wagons, more than (3) : ')
    wagons_list = []
    if max_qty_wagons.isdigit():
        qty_wagons = random.randint(3, int(max_qty_wagons))
        i = 0
        first_wagon = None
        previous_wagon = None
        while i < qty_wagons:
            i += 1
            wagon = Wagon(i)
            wagons_list.append(wagon)
            wagon.set_previous(previous_wagon)
            if first_wagon is None:
                first_wagon = wagon
                previous_wagon = wagon
                continue
            previous_wagon.set_next(wagon)
            previous_wagon = wagon
        wagon.set_next(first_wagon)
        first_wagon.set_previous(wagon)
    return wagons_list

def count_wagons(wagon):
    qty_wagons = 0
    buff_number = 1
    direct = True
    print(
        "Wagon {}, light {}, direct {}, buff_number {}, qty_wagons {}".format(
            wagon.number, wagon.get_light(), direct, buff_number, qty_wagons
        )
    )
    if not wagon.light:
        wagon.set_light(True)
        print('Turn light on')
    while True:
        if buff_number==1 and not direct and not wagon.get_light():
            print(random.choice(STATEMENT_PHRASES))
            return qty_wagons
        elif buff_number==1 and not direct:
            direct = True
            print('switch direct')
        if direct:
            wagon = wagon.get_next()
            buff_number += 1
        else:
            wagon = wagon.get_previous()
            buff_number -= 1
        print(
            "Wagon {}, light {}, direct {}, buff_number {}, qty_wagons {}".format(
                wagon.number, wagon.get_light(), direct, buff_number, qty_wagons
            )
        )
        if wagon.get_light() and buff_number != 1:
            qty_wagons = buff_number-1
            wagon.set_light(False)
            direct = False
            print('turn light off; switch direct')

def main():
    wagons_list = make_loop_wagons()
    if wagons_list:
        wagon_to_start = random.choice(wagons_list)
        for w in wagons_list:
            print(
                "Number {}, light {}, previous {}, next {}".format(
                    w.number, w.light, w.previous.number, w.next.number
                )
            )
        print('Start from', wagon_to_start.number)
        print('Number of wagons #', count_wagons(wagon_to_start))
    else:
        print('wagons_list is empty, try enter correct value')


if __name__=="__main__":
    main()
