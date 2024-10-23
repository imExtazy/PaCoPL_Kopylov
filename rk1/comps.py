from operator import itemgetter


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


browsers = [
    Browser(1, "Chrome"),
    Browser(2, "Firefox"),
    Browser(3, "Safari"),
]

computers = [
    Computer(1, "Dell", 2.5, 1),
    Computer(2, "HP", 3.0, 2),
    Computer(3, "MacBook", 2.7, 3),
    Computer(4, "Lenovo", 2.3, 3),
    Computer(5, "Acer", 2.9, 1),
    Computer(6, "Asus", 3.2, 1)
]

browser_computers = [
    BrowserComputer(1, 1),
    BrowserComputer(2, 2),
    BrowserComputer(3, 3),
    BrowserComputer(3, 4),
    BrowserComputer(1, 5),
]


def first_task(comp_list):
    res_1 = sorted(comp_list, key=itemgetter(0))
    return res_1


def second_task(comp_list):
    res_2 = []
    temp_dict = dict()
    for i in comp_list:
        if i[2] in temp_dict:
            temp_dict[i[2]] += 1
        else:
            temp_dict[i[2]] = 1
    for i in temp_dict.keys():
        res_2.append((i, temp_dict[i]))

    res_2.sort(key=itemgetter(1), reverse=True)
    return res_2


def third_task(comp_list, end_ch):
    res_3 = [(i[0], i[2]) for i in comp_list if i[0].endswith(end_ch)]
    return res_3


def main():
    one_to_many = [(comp.name, comp.speed, br.name)
                   for br in browsers
                   for comp in computers
                   if comp.browser_id == br.id]

    many_to_many_temp = [(br.name, bc.browser_id, bc.comp_id)
                         for br in browsers
                         for bc in browser_computers
                         if bc.browser_id == br.id]

    many_to_many = [(comp.name, comp.speed, br_name)
                    for br_name, br_id, comp_id in many_to_many_temp
                    for comp in computers if comp.id == comp_id]

    print('Задание Б1')
    print(first_task(one_to_many))

    print("\nЗадание Б2")
    print(second_task(one_to_many))

    print("\nЗадание Б3")
    print(third_task(many_to_many, 'k'))


if __name__ == '__main__':
    main()