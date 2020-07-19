import requests as req


def func_a(arg):
    return arg + 1


def func_b(name: str) -> str:
    return name


def get_uuid():
    resp = req.get('http://httpbin.org/uuid')
    return resp.json()['uuid']


def main():
    print(func_a(0))
    print(func_b('narcissus'))
    print(get_uuid())


if __name__ == '__main__':
    main()
