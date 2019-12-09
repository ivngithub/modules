import test

text = """
a=1
a=+1
a=-1
a=b
a=b+100
a=b-100

b+=10
b+=+10
b+=-10
b+=b
b+=b+100
b+=b-100

c-=101
c-=+101
c-=-101
c-=b
c-=b+101
c-=b-101
"""
def calculate(data, findall):

    return findall(r"[abc][-+]?=[abc]?[-+]?\d*")

    # matches = findall(r"")  # Если придумать хорошую регулярку, будет просто
    # for v1, s, v2, n in matches:  # Если кортеж такой структуры: var1, [sign]=, [var2], [[+-]number]
    #     # Если бы могло быть только =, вообще одной строкой все считалось бы, вот так:
    #     data[v1] = data.get(v2, 0) + int(n or 0)
    #
    # return data


if __name__ == '__main__':
    result = calculate({'a': 1, 'b': 2, 'c': 3}, test.findall)
    print(result)
    print(len(result))
