# -*- coding: utf-8 -*-

import copy
import csv

import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.patches as patches

graph = {
    'a': ['b', 'c'],
    'b': ['d', 'f'],
    'c': [],
    'd': [],
    'e': [],
    'f': [],
}
'''
r_0_a,r_0_b,
r_1_a,r_1_b,
r_2_a,r_2_b,
r_3_a,r_3_b,
r_4_a,r_4_b,
r_5_a,r_5_b

3.3,4.3,
3.0,1.5,
3.5,4.5,
2.4,1.4,
1.7,1.2,
0,0
'''
rooms = {
    'a': [2.4, 1.4],
    'b': [1.7, 1.2],
    'c': [3.5, 4.5],
    'd': [3.0, 1.5],
    'f': [3.3, 4.3],
}

#
#   Start point
#

pos = [[0, 0], [0, 0], [0, 0], [0, 0]]


#
#   Drawing functions
#


def draw_x_pos_up(room, position=[[0, 0], [0, 0], [0, 0], [0, 0]]):
    ''' Append placement in upstream direction '''

    # plt.plot([position[1][0], position[1][0] + room[0], position[1][0] + room[0], position[1][0], position[1][0]],
    #          [position[1][1], position[1][1], position[1][1] + room[1], position[1][1] + room[1], position[1][1]],
    #          color='red')
    position = [[position[1][0], position[1][1]],
                [position[1][0] + room[0], position[1][1]],
                [position[1][0] + room[0], position[1][1] + room[1]],
                [position[1][0], position[1][1] + room[1]]
    ]
    return position


def draw_x_pos_down(room, position=[[0, 0], [0, 0], [0, 0], [0, 0]]):
    ''' Append placement in downstream direction '''

    # plt.plot([position[2][0], position[2][0] + room[0], position[2][0] + room[0], position[2][0], position[2][0]],
    #          [position[2][1], position[2][1], position[2][1] - room[1], position[2][1] - room[1], position[2][1]],
    #          color='red')
    position = [[position[2][0], position[2][1] - room[1]],
                [position[2][0] + room[0], position[2][1] - room[1]],
                [position[2][0] + room[0], position[2][1]],
                [position[2][0], position[1][1]]
    ]
    return position


def draw_x_neg_up(room, position=[[0, 0], [0, 0], [0, 0], [0, 0]]):
    ''' Append placement in upstream direction '''

    # plt.plot([position[0][0], position[0][0] - room[0], position[0][0] - room[0], position[0][0], position[0][0]],
    #          [position[0][1], position[0][1], position[0][1] + room[1], position[0][1] + room[1], position[0][1]],
    #          color='blue')
    position = [[position[0][0] - room[0], position[0][1]],
                [position[0][0], position[0][1]],
                [position[0][0], position[0][1] + room[1]],
                [position[0][0] - room[0], position[0][1] + room[1]]
    ]
    return position


def draw_x_neg_down(room, position=[[0, 0], [0, 0], [0, 0], [0, 0]]):
    ''' Append placement in downstream direction '''

    # plt.plot([position[3][0], position[3][0] - room[0], position[3][0] - room[0], position[3][0], position[3][0]],
    #          [position[3][1], position[3][1], position[3][1] - room[1], position[3][1] - room[1], position[3][1]],
    #          color='blue')
    position = [[position[3][0] - room[0], position[3][1] - room[1]],
                [position[3][0], position[3][1] - room[1]],
                [position[3][0], position[3][1]],
                [position[3][0] - room[0], position[3][1]]
    ]
    return position


def draw_y_pos_fw(room, position=[[0, 0], [0, 0], [0, 0], [0, 0]]):
    ''' Append placement in forward direction '''

    # plt.plot([position[3][0], position[3][0] + room[0], position[3][0] + room[0], position[3][0], position[3][0]],
    #          [position[3][1], position[3][1], position[3][1] + room[1], position[3][1] + room[1], position[3][1]],
    #          color='green')
    position = [[position[3][0], position[3][1]],
                [position[3][0] + room[0], position[3][1]],
                [position[3][0] + room[0], position[3][1] + room[1]],
                [position[3][0], position[3][1] + room[1]]
    ]
    return position


def draw_y_pos_rv(room, position=[[0, 0], [0, 0], [0, 0], [0, 0]]):
    ''' Append placement in reverse direction '''

    # plt.plot([position[2][0], position[2][0] - room[0], position[2][0] - room[0], position[2][0], position[2][0]],
    #          [position[2][1], position[2][1], position[2][1] + room[1], position[2][1] + room[1], position[2][1]],
    #          color='green')
    position = [[position[2][0] - room[0], position[2][1]],
                [position[2][0], position[2][1]],
                [position[2][0], position[2][1] + room[1]],
                [position[2][0] - room[0], position[2][1] + room[1]]
    ]
    return position


def draw_y_neg_fw(room, position=[[0, 0], [0, 0], [0, 0], [0, 0]]):
    ''' Append placement in forward direction '''

    # plt.plot([position[0][0], position[0][0] + room[0], position[0][0] + room[0], position[0][0], position[0][0]],
    #          [position[0][1], position[0][1], position[0][1] - room[1], position[0][1] - room[1], position[0][1]],
    #          color='pink')
    position = [[position[0][0], position[0][1] - room[1]],
                [position[0][0] + room[0], position[0][1]],
                [position[0][0] + room[0], position[0][1] - room[1]],
                [position[0][0], position[0][1] - room[1]]
    ]
    return position


def draw_y_neg_rv(room, position=[[0, 0], [0, 0], [0, 0], [0, 0]]):
    ''' Append placement in reverse direction '''

    # plt.plot([position[1][0], position[1][0] - room[0], position[1][0] - room[0], position[1][0], position[1][0]],
    #          [position[1][1], position[1][1], position[1][1] - room[1], position[1][1] - room[1], position[1][1]],
    #          color='pink')
    position = [[position[1][0] - room[0], position[1][1] - room[1]],
                [position[1][0], position[1][1] - room[1]],
                [position[1][0], position[1][1]],
                [position[1][0] - room[0], position[1][1]]
    ]
    return position


#
#   Surround allocating functions
#

def surround_me_n(neighbors_list, built_dict, previous_room):
    '''
    Allocates adjacent rooms. Form North.
    Fill around Previous Room by the Neighbours.
    :return: DICT of the built rooms coordinates.
    '''
    main_room = built_dict[previous_room]
    count = 0
    for i in neighbors_list:

        if i not in built_dict:

            if count == 0:
                built_dict['{}'.format(i)] = draw_x_pos_down(rooms[i], built_dict[previous_room]) + ['n']

            if count == 1:
                if built_dict[previous_room][1][0] > main_room[1][0] and \
                                built_dict[previous_room][0][1] > main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_y_neg_fw(rooms[i], built_dict[previous_room]) + ['n']
                else:
                    built_dict['{}'.format(i)] = draw_y_neg_rv(rooms[i], main_room) + ['n']

            if count == 2:
                if built_dict[previous_room][1][0] > main_room[1][0] and \
                                built_dict[previous_room][0][1] > main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_y_neg_fw(rooms[i], built_dict[previous_room]) + ['n']
                elif built_dict[previous_room][0][0] == main_room[1][0] and \
                                built_dict[previous_room][0][1] <= main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_y_neg_rv(rooms[i], main_room) + ['n']
                elif built_dict[previous_room][0][1] < main_room[0][1] and \
                                built_dict[previous_room][0][0] > main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_x_neg_down(rooms[i], built_dict[previous_room]) + ['n']
                else:
                    built_dict['{}'.format(i)] = draw_x_neg_up(rooms[i], main_room) + ['e']

            if count == 3:
                if built_dict[previous_room][1][0] > main_room[1][0] and \
                                built_dict[previous_room][0][1] > main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_y_neg_fw(rooms[i], built_dict[previous_room]) + ['n']
                elif built_dict[previous_room][0][0] == main_room[1][0] and \
                                built_dict[previous_room][0][1] <= main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_y_neg_rv(rooms[i], main_room) + ['n']
                elif built_dict[previous_room][0][1] < main_room[0][1] and \
                                built_dict[previous_room][0][0] > main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_x_neg_down(rooms[i], built_dict[previous_room]) + ['n']
                elif built_dict[previous_room][2][1] == main_room[0][1] and \
                                built_dict[previous_room][0][0] <= main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_x_neg_up(rooms[i], main_room) + ['e']
                else:
                    built_dict['{}'.format(i)] = draw_y_pos_rv(rooms[i], built_dict[previous_room]) + ['s']

            if count == 4:
                if built_dict[previous_room][1][0] > main_room[1][0] and \
                                built_dict[previous_room][0][1] > main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_y_neg_fw(rooms[i], built_dict[previous_room]) + ['n']
                elif built_dict[previous_room][0][0] == main_room[1][0] and \
                                built_dict[previous_room][0][1] <= main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_y_neg_rv(rooms[i], main_room) + ['n']
                elif built_dict[previous_room][0][1] < main_room[0][1] and \
                                built_dict[previous_room][0][0] > main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_x_neg_down(rooms[i], built_dict[previous_room]) + ['n']
                elif built_dict[previous_room][2][1] == main_room[0][1] and \
                                built_dict[previous_room][0][0] <= main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_x_neg_up(rooms[i], main_room) + ['e']
                else:
                    built_dict['{}'.format(i)] = draw_y_pos_rv(rooms[i], built_dict[previous_room]) + ['s']

        previous_room = i
        count += 1

        if built_dict[previous_room][2][1] > main_room[2][1]:
            return False

    return built_dict


def surround_me_e(neighbors_list, built_dict, previous_room):
    '''
    Allocates adjacent rooms. Form East.
    Fill around Previous Room by the Neighbours.
    :return: DICT of the built rooms coordinates.
    '''
    main_room = built_dict[previous_room]
    count = 0
    for i in neighbors_list:

        if i not in built_dict:

            if count == 0:
                built_dict['{}'.format(i)] = draw_y_neg_rv(rooms[i], built_dict[previous_room]) + ['n']

            if count == 1:
                if built_dict[previous_room][0][0] > main_room[0][0] and \
                                built_dict[previous_room][0][1] < main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_x_neg_down(rooms[i], built_dict[previous_room]) + ['e']
                else:
                    built_dict['{}'.format(i)] = draw_x_neg_up(rooms[i], main_room) + ['s']

            if count == 2:
                if built_dict[previous_room][0][0] > main_room[0][0] and \
                                built_dict[previous_room][0][1] < main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_x_neg_down(rooms[i], built_dict[previous_room]) + ['e']
                elif built_dict[previous_room][3][0] <= main_room[0][0] and \
                                built_dict[previous_room][2][0] > main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_x_neg_up(rooms[i], main_room) + ['s']
                elif built_dict[previous_room][2][1] < main_room[3][1] and \
                                built_dict[previous_room][3][0] < main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_y_pos_rv(rooms[i], built_dict[previous_room]) + ['s']
                else:
                    built_dict['{}'.format(i)] = draw_y_pos_fw(rooms[i], main_room) + ['w']

            if count == 3:
                if built_dict[previous_room][0][0] > main_room[0][0] and \
                                built_dict[previous_room][0][1] < main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_x_neg_down(rooms[i], built_dict[previous_room]) + ['e']
                elif built_dict[previous_room][3][0] <= main_room[0][0] and \
                                built_dict[previous_room][2][0] > main_room[0][0] and \
                        built_dict[previous_room][0][1] < main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_x_neg_up(rooms[i], main_room) + ['s']
                elif built_dict[previous_room][2][1] < main_room[3][1] and \
                                built_dict[previous_room][3][0] < main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_y_pos_rv(rooms[i], built_dict[previous_room]) + ['s']
                elif built_dict[previous_room][2][1] > main_room[3][1] and \
                        built_dict[previous_room][2][0] > main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_x_pos_up(rooms[i], built_dict[previous_room]) + ['s']
                else:
                    built_dict['{}'.format(i)] = draw_y_pos_fw(rooms[i], main_room) + ['w']

            if count == 4:
                if built_dict[previous_room][0][0] > main_room[0][0] and \
                                built_dict[previous_room][0][1] < main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_x_neg_down(rooms[i], built_dict[previous_room]) + ['e']
                elif built_dict[previous_room][3][0] <= main_room[0][0] and \
                                built_dict[previous_room][2][0] > main_room[0][0] and \
                        built_dict[previous_room][0][1] < main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_x_neg_up(rooms[i], main_room) + ['s']
                elif built_dict[previous_room][2][1] < main_room[3][1] and \
                                built_dict[previous_room][3][0] < main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_y_pos_rv(rooms[i], built_dict[previous_room]) + ['s']
                elif built_dict[previous_room][2][1] > main_room[3][1] and \
                                built_dict[previous_room][2][0] > main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_x_pos_up(rooms[i], built_dict[previous_room]) + ['s']
                else:
                    built_dict['{}'.format(i)] = draw_y_pos_fw(rooms[i], main_room) + ['w']

        previous_room = i
        count += 1

        if built_dict[previous_room][2][0] > main_room[1][0]:
            return False

    return built_dict


def surround_me_s(neighbors_list, built_dict, previous_room):
    '''
    Allocates adjacent rooms. Form South.
    Fill around Previous Room by the Neighbours.
    :return: DICT of the built rooms coordinates.
    '''
    main_room = built_dict[previous_room]
    count = 0
    for i in neighbors_list:

        if i not in built_dict:

            if built_dict[previous_room][0][1] <= main_room[0][1] and count > 1:
                return False

            if count == 0:
                built_dict['{}'.format(i)] = draw_x_neg_up(rooms[i], built_dict[previous_room]) + ['e']

            if count == 1:
                if built_dict[previous_room][2][1] < main_room[2][1] and \
                        built_dict[previous_room][1][0] == main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_y_pos_rv(rooms[i], built_dict[previous_room]) + ['s']
                else:
                    built_dict['{}'.format(i)] = draw_y_pos_fw(rooms[i], main_room) + ['s']

            if count == 2:
                if built_dict[previous_room][2][1] < main_room[2][1] and \
                        built_dict[previous_room][1][0] == main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_y_pos_rv(rooms[i], built_dict[previous_room]) + ['s']
                elif built_dict[previous_room][1][0] == main_room[0][0] and \
                        built_dict[previous_room][0][1] >= main_room[2][1]:
                    built_dict['{}'.format(i)] = draw_y_pos_fw(rooms[i], main_room) + ['s']
                elif main_room[0][0] < built_dict[previous_room][1][0] < main_room[1][0] and \
                        built_dict[previous_room][0][1] >= main_room[2][1]:
                    built_dict['{}'.format(i)] = draw_x_pos_up(rooms[i], built_dict[previous_room]) + ['n']
                elif built_dict[previous_room][2][1] >= main_room[3][1] and \
                        built_dict[previous_room][1][0] < main_room[2][0]:
                    built_dict['{}'.format(i)] = draw_y_pos_fw(rooms[i], main_room) + ['s']
                else:
                    built_dict['{}'.format(i)] = draw_x_pos_down(rooms[i], main_room) + ['s']

            if count == 3:
                if built_dict[previous_room][2][1] < main_room[2][1] and \
                        built_dict[previous_room][1][0] == main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_y_pos_rv(rooms[i], built_dict[previous_room]) + ['s']
                elif built_dict[previous_room][1][0] == main_room[0][0] and \
                        built_dict[previous_room][0][1] >= main_room[2][1]:
                    built_dict['{}'.format(i)] = draw_y_pos_fw(rooms[i], main_room) + ['s']
                elif main_room[0][0] < built_dict[previous_room][1][0] < main_room[1][0] and \
                        built_dict[previous_room][0][1] >= main_room[2][1]:
                    built_dict['{}'.format(i)] = draw_x_pos_up(rooms[i], built_dict[previous_room]) + ['s']
                elif built_dict[previous_room][0][1] < main_room[2][1] and \
                        built_dict[previous_room][0][0] == main_room[1][0]:
                    built_dict['{}'.format(i)] = draw_y_neg_fw(rooms[i], built_dict[previous_room]) + ['n']
                elif built_dict[previous_room][1][0] == main_room[0][0] and \
                        built_dict[previous_room][2][1] > main_room[3][1] and \
                        built_dict[previous_room][1][0] != main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_x_pos_up(rooms[i], main_room) + ['s']
                elif built_dict[previous_room][2][1] >= main_room[3][1] and \
                        built_dict[previous_room][1][1] != main_room[2][1]:
                    built_dict['{}'.format(i)] = draw_y_pos_fw(rooms[i], main_room) + ['s']
                else:
                    built_dict['{}'.format(i)] = draw_x_pos_down(rooms[i], main_room) + ['s']

            if count == 4:
                if built_dict[previous_room][2][1] < main_room[2][1] and \
                        built_dict[previous_room][1][0] == main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_y_pos_rv(rooms[i], built_dict[previous_room]) + ['s']
                elif built_dict[previous_room][1][0] == main_room[0][0] and \
                        built_dict[previous_room][0][1] >= main_room[2][1]:
                    built_dict['{}'.format(i)] = draw_y_pos_fw(rooms[i], main_room) + ['s']
                elif main_room[0][0] < built_dict[previous_room][1][0] < main_room[1][0] and \
                        built_dict[previous_room][0][1] >= main_room[2][1]:
                    built_dict['{}'.format(i)] = draw_x_pos_up(rooms[i], built_dict[previous_room]) + ['s']
                elif built_dict[previous_room][0][1] < main_room[2][1] and \
                        built_dict[previous_room][0][0] == main_room[1][0]:
                    built_dict['{}'.format(i)] = draw_y_neg_fw(rooms[i], built_dict[previous_room]) + ['n']
                elif built_dict[previous_room][1][0] == main_room[0][0] and \
                        built_dict[previous_room][2][1] > main_room[3][1] and \
                        built_dict[previous_room][1][0] != main_room[0][0]:
                    built_dict['{}'.format(i)] = draw_x_pos_up(rooms[i], main_room) + ['s']
                elif built_dict[previous_room][2][1] >= main_room[3][1] and \
                        built_dict[previous_room][1][1] != main_room[2][1]:
                    built_dict['{}'.format(i)] = draw_y_pos_fw(rooms[i], main_room) + ['s']
                else:
                    built_dict['{}'.format(i)] = draw_x_pos_down(rooms[i], main_room) + ['s']

        previous_room = i
        count += 1

        if built_dict[previous_room][0][1] < main_room[0][1]:
            return False

    return built_dict


def surround_me_w(neighbors_list, built_dict, previous_room):
    '''
    Allocates adjacent rooms. Form West.
    Fill around Previous Room by the Neighbours.
    :return: DICT of the built rooms coordinates.
    '''
    main_room = built_dict[previous_room]
    count = 0
    for i in neighbors_list:

        if i not in built_dict:

            if count == 0:
                built_dict['{}'.format(i)] = draw_y_pos_fw(rooms[i], built_dict[previous_room]) + ['w']

            if count == 1:
                if built_dict[previous_room][0][1] == main_room[2][1] and \
                                built_dict[previous_room][1][0] < main_room[1][0]:
                    built_dict['{}'.format(i)] = draw_x_pos_up(rooms[i], built_dict[previous_room]) + ['w']
                else:
                    built_dict['{}'.format(i)] = draw_x_pos_down(rooms[i], main_room) + ['w']

            if count == 2:
                if built_dict[previous_room][0][1] == main_room[2][1] and \
                                built_dict[previous_room][1][0] < main_room[1][0]:
                    built_dict['{}'.format(i)] = draw_x_pos_up(rooms[i], built_dict[previous_room]) + ['w']
                elif built_dict[previous_room][0][1] == main_room[2][1] and \
                                built_dict[previous_room][1][0] >= main_room[1][0]:
                    built_dict['{}'.format(i)] = draw_x_pos_down(rooms[i], main_room) + ['w']
                elif built_dict[previous_room][0][0] == main_room[1][0] and \
                                built_dict[previous_room][0][1] > main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_y_neg_fw(rooms[i], built_dict[previous_room]) + ['n']
                else:
                    built_dict['{}'.format(i)] = draw_y_neg_rv(rooms[i], main_room) + ['e']

            if count == 3:
                if built_dict[previous_room][0][1] == main_room[2][1] and \
                                built_dict[previous_room][1][0] < main_room[1][0]:
                    built_dict['{}'.format(i)] = draw_x_pos_up(rooms[i], built_dict[previous_room]) + ['w']
                elif built_dict[previous_room][0][1] == main_room[2][1] and \
                                built_dict[previous_room][1][0] >= main_room[1][0]:
                    built_dict['{}'.format(i)] = draw_x_pos_down(rooms[i], main_room) + ['w']
                elif built_dict[previous_room][0][0] == main_room[1][0] and \
                                built_dict[previous_room][0][1] > main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_y_neg_fw(rooms[i], built_dict[previous_room]) + ['n']
                elif built_dict[previous_room][0][0] == main_room[1][0] and \
                                built_dict[previous_room][0][1] <= main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_y_neg_rv(rooms[i], main_room) + ['e']
                else:
                    built_dict['{}'.format(i)] = draw_x_neg_down(rooms[i], built_dict[previous_room]) + ['e']

            if count == 4:
                if built_dict[previous_room][0][1] == main_room[2][1] and \
                                built_dict[previous_room][1][0] < main_room[1][0]:
                    built_dict['{}'.format(i)] = draw_x_pos_up(rooms[i], built_dict[previous_room]) + ['w']
                elif built_dict[previous_room][0][1] == main_room[2][1] and \
                                built_dict[previous_room][1][0] >= main_room[1][0]:
                    built_dict['{}'.format(i)] = draw_x_pos_down(rooms[i], main_room) + ['w']
                elif built_dict[previous_room][0][0] == main_room[1][0] and \
                                built_dict[previous_room][0][1] > main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_y_neg_fw(rooms[i], built_dict[previous_room]) + ['n']
                elif built_dict[previous_room][0][0] == main_room[1][0] and \
                                built_dict[previous_room][0][1] <= main_room[0][1]:
                    built_dict['{}'.format(i)] = draw_y_neg_rv(rooms[i], main_room) + ['e']
                else:
                    built_dict['{}'.format(i)] = draw_x_neg_down(rooms[i], built_dict[previous_room]) + ['e']

        previous_room = i
        count += 1

        if built_dict[previous_room][0][0] < main_room[0][0]:
            return False

    return built_dict


#
# Checking functions
#


def find_all_paths(graph, start, end, path=[]):
    ''' Returns all possible paths from the assigned start to the end '''

    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_key(start):
        return []
    paths = []
    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths


def find_routes(graph, start, path=[], paths=[]):
    ''' Returns all possible paths from the assigned start in every direction '''

    path = path + [start]

    for node in graph[start]:
        if not graph[node]:
            paths.append(path + [node])
        find_routes(graph, node, path, paths)

    return paths


def order_graph_row(graph=graph):
    '''
    Combine rooms
    Didn't compleate!!
    '''
    done = []
    for k, row in graph.items():

        for room in row:

            count = 0
            rooms_list = []

            sub_room = None
            for sub_room in graph[room]:

                if sub_room in row:

                    count += 1
                    rooms_list.append(sub_room)

            if sub_room in done:
                continue
            if count == 1:
                if graph[k].index(room) == 0:
                    graph[k].insert(1, graph[k].pop(graph[k].index(rooms_list[0])))
                else:
                    graph[k].insert(graph[k].index(room) + 1, graph[k].pop(graph[k].index(rooms_list[0])))
            elif count == 2:
                if graph[k].index(room) == 0:
                    graph[k].insert(0, graph[k].pop(graph[k].index(rooms_list[0])))
                    graph[k].insert(2, graph[k].pop(graph[k].index(rooms_list[1])))
                else:
                    graph[k].insert(graph[k].index(rooms_list[0]) - 1, graph[k].pop(graph[k].index(room)))
                    graph[k].insert(graph[k].index(rooms_list[1]) + 1, graph[k].pop(graph[k].index(room)))
            elif count > 2:
                print "ERROR\tOrder graph row Impossible."
                return False

            done.append(sub_room)


def is_intersect(r1, r2):
    ''' Returns True or False, consider to intersection of two rectangles '''

    return not (r1[2][1] < r2[0][1] or
                r1[0][1] > r2[2][1] or
                r1[2][0] < r2[0][0] or
                r1[0][0] > r2[2][0])


def is_overlapped(room, rooms_dict):
    '''
    :param room: Current room coordinates. For all 4 vertexes.
    :param rooms_dict: All built rooms in coordinates.
    :return: True / False. Depends on if at least one vertex of the room belongs to built rooms
    '''
    internal_d = copy.deepcopy(rooms_dict)
    out = False
    for dot in room:

        # for bi in out:
        #     for k, item in bi.items():
        #         _b = {k: bi.pop(k)}
        #         if is_overlapped(item, bi):
        #             b[_b.keys()[0]] = _b.values()[0]
        #             out.pop(b)
        #         b[_b.keys()[0]] = _b.values()[0]

        for k, s_dot in rooms_dict.items():
            _b = {k: internal_d.pop(k)}
            if (s_dot[0][0] < dot[0] < s_dot[2][0]) and (s_dot[0][1] < dot[1] < s_dot[2][1]):
                out = True
            internal_d[_b.keys()[0]] = _b.values()[0]

    return out


def check_route(route, rooms_dict):
    '''
    If adjacent rooms in the sequence of the route from the rooms_dict have an intersection than returns True,
    if not - False
    '''

    out = []
    previous_room = None
    count = 0
    for room in route:
        if not count:
            count += 1
            previous_room = room
            continue
        out.append(is_intersect(rooms_dict[previous_room], rooms_dict[room]))
        previous_room = room
    return all(out)


def go_inside_graph(possible_rooms_dict, start, graph=graph):

    l = []
    for room in graph[start]:

        for sub_rooms in graph[room]:
            l.append(surround_me_w(sub_rooms, possible_rooms_dict, room))

    return l


out = []
route = []
routes = find_routes(graph, 'a')


def controller(built_dict, start, out, graph=graph):

    # print "DEBUG", graph
    order_graph_row()
    # print "DEBUG", graph
    # pdf_pages = PdfPages('variants.pdf')

    own_routes = []
    count = 0
    for _route in routes:
        own_routes.append([])
        for r in _route:
            if r in graph[start]:
                own_routes[count].append(r)
        count += 1

    if not out:
        for _ in graph[start]:
            # fig = plt.figure(figsize=(30, 30), dpi=100)
            # size = 30
            # plt.axis([-size, size, -size, size])
            built_dict[start] = draw_x_pos_up(rooms['a']) + ['s']

            b = copy.deepcopy(built_dict)

            b = surround_me_s(graph[start], b, start)

            graph[start].append(graph[start].pop(0))  # move room from the first position on the last

            for route in own_routes:
                if check_route(route, b) and b.values() not in [x.values() for x in out]:
                    out.append(b)
            # pdf_pages.savefig(fig)

    else:
        for i_rooms in graph[start]:
            for i_room in i_rooms:

                for i_built_dict in out:
                    # fig = plt.figure(figsize=(30, 30), dpi=100)
                    # size = 10
                    # plt.axis([-size, size, -size, size])

                    b = copy.deepcopy(i_built_dict)

                    for sub_i_room in graph[i_room]:
                        if sub_i_room not in i_built_dict.keys():

                            b = surround_me_s(graph[i_room], b, i_room)

                            graph[start].append(graph[start].pop(0))  # move room from the first position on the last

                            for route in own_routes:

                                if check_route(route, b) and b.values() not in [x.values() for x in out]:
                                    # print "DEBUG\t", b
                                    if is_overlapped(sub_i_room, i_built_dict):
                                        out.append(b)
                                # pdf_pages.savefig(fig)
        # pdf_pages.close()
        return [x for x in out if len(x) == max([len(xx) for xx in out])]

    return controller(built_dict, start, out)

with open('rooms_a_b.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)

    pdf_pages = PdfPages('variants.pdf')

    count = 0
    for row in reader:
        d = None
        if count == 0:
            count += 1
            continue
        a = [float(row[6]), float(row[7])]
        b = [float(row[8]), float(row[9])]
        c = [float(row[4]), float(row[5])]
        d = [float(row[2]), float(row[3])]
        e = [float(row[10]), float(row[11])]
        f = [float(row[0]), float(row[1])]
        if not e[0]:
            rooms = {
                'a': a,
                'b': b,
                'c': c,
                'd': d,
                'f': f,
            }
        else:
            rooms = {
                'a': a,
                'b': b,
                'c': c,
                'd': d,
                'e': e,
                'f': f,
            }
        d = controller({}, 'a', [])

        for collection in d:

            pack = {}
            for name, room in collection.items():
                # print "+", room
                pack[name] = patches.Rectangle(
                    (room[0][0], room[0][1]), room[1][0] - room[0][0], room[2][1] - room[1][1],
                    alpha=0.4,)

            fig = plt.figure()
            ax = fig.add_subplot(111, aspect='equal')
            for p in pack:

                size = 10
                plt.axis([-size, size, -size, size])

                ax.add_artist(pack[p])
                rx, ry = pack[p].get_xy()
                cx = rx + pack[p].get_width()/2.0
                cy = ry + pack[p].get_height()/2.0
                if p == 'a':
                    p = 'Enter room'
                if p == 'b':
                    p = 'Corridor'
                if p == 'c':
                    p = 'Living room'
                if p == 'd':
                    p = 'Bathroom'
                if p == 'e':
                    p = 'Wardrobe'
                if p == 'f':
                    p = 'Kitchen'
                ax.annotate(p, (cx, cy), color='w', weight='bold',
                            fontsize=6, ha='center', va='center')
                # ax.add_patch(p)
            pdf_pages.savefig(fig)
        if count == 25:
            break
        count += 1
    pdf_pages.close()


#
# Start Point
#
def main(start="a"):

    order_graph_row()

    # The PDF document
    pdf_pages = PdfPages('variants.pdf')

    '''
    d_main = {}
    d_try = {}
    for _ in range(len(graph[start])):

        fig = plt.figure(figsize=(30, 30), dpi=100)
        size = 30
        plt.axis([-size, size, -size, size])

        # Very first node
        d_main['{}'.format(start)] = draw_x_pos_up(rooms[start]) + ['s']
        d_try = copy.deepcopy(d_main)

        surround_me_s(graph[start], d_try, start)
        graph['a'].append(graph['a'].pop(0))    # move room from the first position on the last

        pdf_pages.savefig(fig)
        print '+', d_try
    '''
    d_main = {}
    fig = plt.figure(figsize=(30, 30), dpi=100)
    size = 30
    plt.axis([-size, size, -size, size])

    # Very first node
    d_main['{}'.format(start)] = draw_x_pos_up(rooms[start]) + ['s']
    d_try = copy.deepcopy(d_main)

    for k, v in surround_me_w(graph[start], d_try, start).items():
        l = go_inside_graph(d_try, k)
        d_main[k] = v
        # print "~\t\t", d_main
    # print "++", l

    if l:
        for k in l[0]:
            # print '#', k, l[0][k]
            d_main[k] = l[0][k]
        # print "--", d_main

    pdf_pages.savefig(fig)

    pdf_pages.close()

    return d_main


#
#   Testing
#

# routes = find_routes(graph, 'a')
# print routes
# for route in routes:
#     print check_route(route, d)


# print "DEBUG: The Graph is:"
# for k, v in graph.items():
#     print k, v
# print '_' * 100


# Functions Lists for sides directions
'''
W = [draw_x_neg_down, draw_x_neg_up]
N = [draw_y_pos_rv, draw_y_pos_fw]
E = [draw_x_pos_down, draw_x_pos_up]
S = [draw_y_neg_fw, draw_y_neg_rv]
DRAW_LIST = [W, N, E, S]
'''
