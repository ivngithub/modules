
# здесь идет упаковка входящий аргументов в list, dict
def foo(required, *args, **kwargs):
    print(required)
    print(args)
    print(kwargs)

    # здесь идет распаковка
    bar(*args)
    bar2(*args)


def bar(a, b, c):
    print(a, b, c)

# здесь идет упаковка'
def bar2(*args):
    # здесь идет распаковка
    print(*args)

if __name__ == '__main__':
    foo('r', 1, 2, 3)
