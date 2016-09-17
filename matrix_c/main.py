# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt


p_list = [
    [0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1],
    [0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0],
]

a = [2, 2]
b = [3, 3]
c = [7, 7]
d = [2, 2]
e = [2, 2]
f = [8, 3]

pos = [[0, 0], [0, 0], [0, 0], [0, 0]]

plt.axis([-20, 20, -20, 20])


def controller_x_pos(position, room):

    plt.plot([position[1][0], position[1][0] + room[0], position[1][0] + room[0], position[1][0], position[1][0]],
             [position[1][1], position[1][1], position[1][1] + room[1], position[1][1] + room[1], position[1][1]],
             color='red')
    position = [[position[1][0], position[1][1]],
                [position[1][0] + room[0], position[1][1]],
                [position[1][0] + room[0], position[1][1] + room[1]],
                [position[1][0], position[1][1] + room[1]]
    ]
    return position


def controller_x_neg(position, room):

    plt.plot([position[0][0], position[0][0] - room[0], position[0][0] - room[0], position[0][0], position[0][0]],
             [position[0][1], position[0][1], position[0][1] + room[1], position[0][1] + room[1], position[0][1]],
             color='blue')
    position = [[position[0][0] - room[0], position[0][1]],
                [position[0][0], position[0][1]],
                [position[0][0], position[0][1] + room[1]],
                [position[0][0] - room[0], position[0][1] + room[1]]
    ]
    return position


def controller_y_pos(position, room):

    plt.plot([position[3][0], position[3][0] + room[0], position[3][0] + room[0], position[3][0], position[3][0]],
             [position[3][1], position[3][1], position[3][1] + room[1], position[3][1] + room[1], position[3][1]],
             color='green')
    position = [[position[3][0], position[3][1]],
                [position[3][0] + room[0], position[3][1]],
                [position[3][0] + room[0], position[3][1] + room[1]],
                [position[3][0], position[3][1] + room[1]]
    ]
    return position


def controller_y_neg(position, room):

    plt.plot([position[0][0], position[0][0] + room[0], position[0][0] + room[0], position[0][0], position[0][0]],
             [position[0][1], position[0][1], position[0][1] - room[1], position[0][1] - room[1], position[0][1]],
             color='pink')
    position = [[position[0][0], position[0][1] - room[1]],
                [position[0][0] + room[0], position[0][1]],
                [position[0][0] + room[0], position[0][1] - room[1]],
                [position[0][0], position[0][1] - room[1]]
    ]
    return position

controller_y_neg(controller_y_pos(controller_x_pos(controller_x_neg(controller_x_pos(controller_x_pos(pos, a), b), c), c), a), f)

plt.show()
