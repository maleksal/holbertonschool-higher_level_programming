#!/usr/bin/python3
""" Send request """


if __name__ == "__main__":
    from urllib import parse, request
    import sys

    data = parse.urlencode({'email': sys.argv[2]})
    data = data.encode()

    with request.urlopen(sys.argv[1], data) as response:
        print(response.read().decode("utf-8"))
