from bs4 import BeautifulSoup

import re
import os
import pprint


# Вспомогательная функция, её наличие не обязательно и не будет проверяться
def build_tree(start, end, path):
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")  # Искать ссылки можно как угодно, не обязательно через re
    files = dict.fromkeys(os.listdir(path))  # Словарь вида {"filename1": None, "filename2": None, ...}
    # TODO Проставить всем ключам в files правильного родителя в значение, начиная от start

    filenames = {file for file in files.keys()}

    for i, file_name in enumerate(files, start=1):

        with open("{}{}".format(path, file_name)) as f:
            contents = f.read()
            link_names = set(re.findall(link_re, contents))

            children = filenames.intersection(link_names).difference({file_name})
            files[file_name] = children

            # print(i, file_name, files[file_name])

    # print('Stone_Age', files['Stone_Age'])
    # print('*'*10)
    # print('Brain', files['Brain'])
    # print('*'*10)
    # print('Artificial_intelligence', files['Artificial_intelligence'])

    from collections import deque

    def bfs(graph, root, end):
        distances = {}
        distances[root] = 0
        q = deque([root])
        while q:
            # The oldest seen (but not yet visited) node will be the left most one.
            current = q.popleft()
            for neighbor in graph[current]:
                print(q)
                if neighbor == end:
                    print('good', 'start:', root, 'end:', end)
                    pprint.pprint(graph[current])
                    pprint.pprint(distances)
                    return

                if neighbor not in distances:
                    distances[neighbor] = distances[current] + 1
                    # When we see a new node, we add it to the right side of the queue.
                    q.append(neighbor)
        return distances

    bfs(files, start, end)



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


def debug_fun():
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")
    with open('wiki/14th_Chess_Olympiad') as data:
        soup = BeautifulSoup(data, "lxml")
        links = soup.find_all('a', href=link_re)
        s = {link.text for link in links if link.text == 'Agnostic'}
        l = [link.text for link in links if link.text]

    print(s)


if __name__ == '__main__':
    # debug_fun()
    r = build_tree('Stone_Age', 'Python_(programming_language)', 'wiki/')
    # print(r)