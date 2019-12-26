import json, pprint, os
from collections import namedtuple


Value = namedtuple('Value', 'values statistic')
# basedir = os.path.abspath(os.path.dirname(__file__))


class TypeStatistic:
    def __init__(self, item):
        self.statistic = {list: 0, dict: 0, str: 0, bool: 0, float: 0, int: 0, None: 0}
        self.update_statistic(item)

    def update_statistic(self, item):
        if type(item) in (list, dict, str, bool, float, int):
            self.statistic[type(item)] +=1
        else:
            self.statistic[None] +=1


class BuilderDictionary:

    def __init__(self, path_to_file):
        self.max_dict = dict()
        self.file = path_to_file

    def _builder(self, data):
        for key in data:
            value = data[key]
            if key in self.max_dict:
                self.max_dict[key].values.append(value)
                self.max_dict[key].statistic.update_statistic(value)
            else:
                self.max_dict[key] = Value([value], TypeStatistic(value))

    def build(self):
        with open(self.file) as f:
            for i, string in enumerate(f, start=1):
                item = json.loads(string)
                dict_from_string = json.loads(item['company'])
                self._builder(dict_from_string)

    def view(self, type_item, s=None):
        for item in self.max_dict:
            if s:
                i = 0
                for el in self.max_dict[item].statistic.statistic:
                    if self.max_dict[item].statistic.statistic[el] > 0:
                        i += 1
                        if i > 1:
                            print(item)
                            pprint.pprint(self.max_dict[item].values[:3])
                            pprint.pprint(self.max_dict[item].statistic.statistic)
                            print('-' * 10)

            else:

                if type_item:
                    if self.max_dict[item].statistic.statistic[type_item] > 0:
                        print(self.max_dict[item].values[:3])
                        print(type_item)
                        pprint.pprint(self.max_dict[item].statistic.statistic[type_item])
                        print('-'*10)
                else:
                    print(item)
                    pprint.pprint(self.max_dict[item].values[:3])
                    pprint.pprint(self.max_dict[item].statistic.statistic)
                    print('-' * 10)


if __name__ == '__main__':

    r = BuilderDictionary('items1.jl')
    r.build()
    r.view(0, s=1)
