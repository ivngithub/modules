from bs4 import BeautifulSoup
import re
import os
from collections import deque, namedtuple


def build_tree(path):
    link_re = re.compile(r"(?<=/wiki/)[\w()]+")
    files = dict.fromkeys(os.listdir(path))

    filenames = {file for file in files.keys()}

    for file_name in files:
        with open("{}{}".format(path, file_name)) as f:
            contents = f.read()
            link_names = set(re.findall(link_re, contents))

            children = filenames.intersection(link_names).difference({file_name})
            files[file_name] = children

    return files


def bfs(graph, root):
        visited, queue = set(), deque([[0, root]])
        visited.add(root)

        # graph_after_bfs = {
                                # 0: {'graph_field_name': ['wave_members', ]},
                                # 1: {'graph_field_name1': ['wave_members', ],
                                #     'graph_field_name2': ['wave_members', ]
                                #     },
                           # }

        Point = namedtuple('Point', ['iam', 'parent'])
        points = [Point(iam=root, parent=root)]

        while queue:

            vertexes = queue.popleft()

            wave_number = vertexes[0]
            wave_members = [wave_number + 1]

            for wave_member in vertexes[1:]:

                # if wave_number in graph_after_bfs:
                #     graph_after_bfs[wave_number].update({wave_member: []})
                # else:
                #     graph_after_bfs[wave_number] = {wave_member: []}

                for neighbour in graph[wave_member]:
                    if neighbour not in visited:
                        visited.add(neighbour)
                        wave_members.append(neighbour)

                        # graph_after_bfs[wave_number][wave_member].append(neighbour)

                        p = Point(iam=neighbour, parent=wave_member)
                        points.append(p)

            if len(wave_members) > 1:
                queue.append(wave_members)

        # # clear
        # for key in graph_after_bfs:
        #     for item in set(graph_after_bfs[key]):
        #         if not bool(graph_after_bfs[key][item]):
        #             del graph_after_bfs[key][item]

        # return graph_after_bfs
        return points


def build_bridge(start, end, path):
    bridge = []

    files = build_tree(path)

    try:
        points = bfs(files, start)

        end_point = list(filter(lambda x: x.iam == end, points))
        # print(end_point)
        bridge.append(end_point[0].iam)

        for el in range(len(points)):
            if end_point[0].parent == start and end_point[0].iam == start:
                break
            end_point = list(filter(lambda x: x.iam == end_point[0].parent, points))
            bridge.append(end_point[0].iam)
            # print(end_point)

    except (KeyError, IndexError):
        return bridge

    return bridge[::-1]


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
    print(build_bridge('Stone_Age', 'Python_(programming_language)', 'wiki/'))
    # r = build_tree('Structural_geology', 'Python_(programming_language)', 'wiki/')
    print('finish ...')
    # #TODO
    # # что если не верный старт или конец