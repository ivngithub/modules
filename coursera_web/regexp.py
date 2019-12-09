# import test
#
# text = """
# a=1
# a=+1
# a=-1
# a=b
# a=b+100
# a=b-100
#
# b+=10
# b+=+10
# b+=-10
# b+=b
# b+=b+100
# b+=b-100
#
# c-=101
# c-=+101
# c-=-101
# c-=b
# c-=b+101
# c-=b-101
# """
def calculate(data, findall):

    # matches = findall(r"(([abc])([-+]?=)([abc]?)([-+]?\d*))")
    matches = findall(r"([abc])([-+]?=)([abc]?)([-+]?\d*)")
    for v1, s, v2, n in matches:

        tmp_result = data.get(v2, 0) + int(n or 0)
        r = \
        """
        y+=y+100a=+1x-=y+101a=b+100y+=y-100y+=yx-=101x=1a=bx=y-expected0
        Начальные значения переменных: {'a': 10, 'b': 20, 'c': 30}
                  Ожидаемый вывод: {'a': 20, 'b': 20, 'c': 30}
        """

        if s == '-=':
            data[v1] = data[v1] - tmp_result
        elif s == '+=':
            data[v1] = data[v1] + tmp_result
        else:
            data[v1] = tmp_result

    return data

# if __name__ == '__main__':
#     result = calculate({'a': 10, 'b': 20, 'c': 30}, test.findall)
#     print(result)
