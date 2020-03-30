from bs4 import BeautifulSoup
import re
import os


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path):
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
    files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
    # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start

    filenames = {file for file in files.keys()}

    for file_name in files:
        with open("{}{}".format(path, file_name)) as f:
            contents = f.read()
            link_names = set(re.findall(link_re, contents))

            children = filenames.intersection(link_names).difference({file_name})
            files[file_name] = children

    return files


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_bridge(start, end, path):
    files = build_tree(start, end, path)
    bridge = []
    # TODO Добавить нужные страницы в bridge
    return bridge


def parse(start, end, path):
    """
    Если не получается найти список страниц bridge, через ссылки на которых можно добраться от start до end, то,
    по крайней мере, известны сами start и end, и можно распарсить хотя бы их: bridge = [end, start]. Оценка за тест,
    в этом случае, будет сильно снижена, но на минимальный проходной балл наберется, и тест будет пройден.
    Чтобы получить максимальный балл, придется искать все страницы. Удачи!
    """

    bridge = build_bridge(start, end, path)  # Искать список страниц можно как угодно, даже так: bridge = [end, start]

    # Когда есть список страниц, из них нужно вытащить данные и вернуть их
    out = {}
    for file in bridge:
        with open("{}{}".format(path, file)) as data:
            soup = BeautifulSoup(data, "lxml")

        body = soup.find(id="bodyContent")

        # TODO посчитать реальные значения
        imgs = 5  # Количество картинок (img) с шириной (width) не меньше 200
        headers = 10  # Количество заголовков, первая буква текста внутри которого: E, T или C
        linkslen = 15  # Длина максимальной последовательности ссылок, между которыми нет других тегов
        lists = 20  # Количество списков, не вложенных в другие списки

        out[file] = [imgs, headers, linkslen, lists]

    return out


if __name__ == '__main__':
    print('start ...')
    r = build_tree('Stone_Age', 'Python_(programming_language)', 'wiki/')
    print('next ...')
    # for key, item in r.items():
    #     print(key, ':', item)


    import collections


    def bfs(graph, root):
        visited, queue = set(), collections.deque([root])
        visited.add(root)

        Point = collections.namedtuple('Point', ['iam', 'parent'])
        steps = []

        while queue:
            vertex = queue.popleft()
            for neighbour in graph[vertex]:

                p = Point(iam=neighbour, parent=vertex)
                steps.append(p)

                if neighbour not in visited:
                    visited.add(neighbour)
                    queue.append(neighbour)

        return steps

    v = bfs(r, 'Stone_Age')
    end_list = filter(lambda x: x.iam == 'Python_(programming_language)', v)

    for el in end_list:
        pass