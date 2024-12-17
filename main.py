from operator import itemgetter
import math


class Browser:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Computer:
    def __init__(self, id, name, speed, browser_id):
        self.id = id
        self.name = name
        self.speed = speed
        self.browser_id = browser_id


class BrowserComputer:
    def __init__(self, browser_id, comp_id):
        self.browser_id = browser_id
        self.comp_id = comp_id


def first_task(comp_list):
    return sorted(comp_list, key=itemgetter(0))


def second_task(comp_list):
    temp_dict = {}
    for i in comp_list:
        if i[2] in temp_dict:
            temp_dict[i[2]] += 1
        else:
            temp_dict[i[2]] = 1
    res_2 = [(i, temp_dict[i]) for i in temp_dict.keys()]
    res_2.sort(key=itemgetter(1), reverse=True)
    return res_2


def third_task(comp_list, end_ch):
    return [(i[0], i[2]) for i in comp_list if i[0].endswith(end_ch)]
