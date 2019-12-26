import json, pprint


def main():
    # keys = []
    max_dict = dict()
    with open('items.jl') as f:
        for i, string in enumerate(f, start=1):
            item = json.loads(string)
            data = json.loads(item['company'])

            for key in data:
                if key in max_dict:
                    # print(i)
                    if type(data[key]) != type(max_dict[key]):
                        raise Exception('{} is in {}'.format(key, max_dict))

            max_dict.update(data)

            # keys.extend([key for key in data])
            # print(i)
            # print('NEW KEYS', len(data))
            #
            # print('AFTER keys.extend', len(keys))
            #
            # keys = set(keys)
            # print('AFTER set(keys)', len(keys))
            #
            # keys = list(keys)
            # # print('AFTER list(keys)', len(keys))
            # print('*'*10)
            # print(i, type(data), len(data))
    # print(len(keys), keys)

    return max_dict

def gen_pattern_dict(d):

    pattern_dict = dict()
    for key, value in d.items():
        pattern_dict[key] = type(value)

    return pattern_dict

if __name__ == '__main__':
    result = main()
    print(result, len(result))

    result = gen_pattern_dict(result)
    pprint.pprint(result)
