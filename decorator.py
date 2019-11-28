def time_in(func):
    def wrapper(*args, **kwargs):
        print(time_in.__name__)

        result = func(*args, **kwargs)
        return result

    return wrapper

def time_in_2(arg):
    def arg_from_decorator(func):

        def wrapper(*args, **kwargs):
            print(arg)
            print(time_in.__name__)
            x = 1, *args
            result = func(x[-1][0])
            return result

        return wrapper

    return arg_from_decorator

@time_in
def g_list(n):

    return [el for el in range(n)]

def g_list_2(n):

    return [el for el in range(n+10)]

if __name__ == '__main__':

    print(g_list(10))

    t = time_in_2
    print(t('arg_from_decorator')(g_list_2)(10, (3,4)))
