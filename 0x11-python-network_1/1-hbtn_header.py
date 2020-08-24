#!/usr/bin/python3
""" Send request """


if __name__ == "__main__":
    import urllib.request
    import sys

    argv = sys.argv[1]
    with urllib.request.urlopen(urllib.request.Request(argv)) as response:
        print(response.headers["X-Request-Id"])
