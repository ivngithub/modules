from pickletools import pickle

data = {'a': [1,2,3],'b': False, 'c': ("character string", b"byte string")}

def main():
    global data

    with open('data.pickle', 'wb') as f:
        pickle.dump(data, f)

    with open('data.pickle', 'rb') as f:
        data_new = pickle.load(f)

    print('from file', data_new)
    data = pickle.dumps(data)
    print(data)
    data = pickle.loads(data)
    print(data)

if __name__ == '__main__':
    main()
