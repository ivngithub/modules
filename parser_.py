import json


def main():
    with open('items.jl') as f:
        for i, string in enumerate(f, start=1):
            item = json.loads(string)
            data = json.loads(item['company'])

            print(i, type(data), len(data))


if __name__ == '__main__':
    main()