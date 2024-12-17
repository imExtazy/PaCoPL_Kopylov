import main
from operator import itemgetter
import unittest


class TestMainMethods(unittest.TestCase):

    def setUp(self):
        # Инициализация данных
        self.browsers = [
            main.Browser(1, "Chrome"),
            main.Browser(2, "Firefox"),
            main.Browser(3, "Safari"),
        ]

        self.computers = [
            main.Computer(1, "Dell", 2.5, 1),
            main.Computer(2, "HP", 3.0, 2),
            main.Computer(3, "MacBook", 2.7, 3),
            main.Computer(4, "Lenovo", 2.3, 3),
            main.Computer(5, "Acer", 2.9, 1),
            main.Computer(6, "Asus", 3.2, 1),
        ]

        self.browser_computers = [
            main.BrowserComputer(1, 1),
            main.BrowserComputer(2, 2),
            main.BrowserComputer(3, 3),
            main.BrowserComputer(3, 4),
            main.BrowserComputer(1, 5),
        ]

        # Преобразования для тестирования
        self.one_to_many = [
            ('Dell', 2.5, 'Chrome'),
            ('HP', 3.0, 'Firefox'),
            ('MacBook', 2.7, 'Safari'),
            ('Lenovo', 2.3, 'Safari'),
            ('Acer', 2.9, 'Chrome'),
            ('Asus', 3.2, 'Chrome'),
        ]

        self.many_to_many = [
            ('Chrome', 1, 1),
            ('Firefox', 2, 2),
            ('Safari', 3, 3),
            ('Safari', 3, 4),
            ('Chrome', 1, 5),
        ]

    def test_first_task_method(self):
        # Проверка первого задания
        result = main.first_task(self.one_to_many)
        reference = sorted(self.one_to_many, key=itemgetter(0))
        self.assertEqual(result, reference)

    def test_second_task_method(self):
        # Проверка второго задания
        result = main.second_task(self.one_to_many)
        reference = [('Chrome', 3), ('Safari', 2), ('Firefox', 1)]
        self.assertEqual(result, reference)

    def test_third_task_method_with_k(self):
        # Проверка третьего задания для символа 'k', который встречается в "MacBook"
        result = main.third_task(self.one_to_many, 'k')
        reference = [('MacBook', 'Safari')]  # Ожидаем, что только MacBook имеет имя, заканчивающееся на 'k'
        self.assertEqual(sorted(result), sorted(reference))  # Сравниваем отсортированные списки

    def test_third_task_method_with_x(self):
        # Проверка третьего задания для символа 'x', которого нет в именах
        result = main.third_task(self.one_to_many, 'x')
        reference = []  # Ожидаем пустой список
        self.assertEqual(sorted(result), sorted(reference))  # Сравниваем отсортированные списки


if __name__ == '__main__':
    unittest.main()
