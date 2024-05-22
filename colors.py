import random


color_list = ["Y", "B", "G", "R", "W", "O"]
tries = 10
code_lenght = 4
chosen_ones = []


def random_color():

    for i in range(code_lenght):
        random_co = random.choices(color_list)
        chosen_ones.append(random_co)
    print(chosen_ones)
    return chosen_ones


random_color()


def choice_foo():
    choice = input("guess colors:").upper().split()
    # print(choice)

    while True:
        if len(choice) != code_lenght:
            print(f'you must guess {code_lenght} colors!')
            continue

        for choice in color_list:
            if choice not in color_list:
                print(f'invalid color{choice}.Try again.')
                break
        else:
            break


choice_foo()
