#!/usr/bin/python3
""" Send request """


if __name__ == "__main__":
    import requests
    import sys

    response = requests.post(sys.argv[1], {"email": sys.argv[2]})
    print(response.text)
