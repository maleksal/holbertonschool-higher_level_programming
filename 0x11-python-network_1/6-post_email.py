#!/usr/bin/python3
""" Send request """


if __name__ == "__main__":
    import requests
    import sys

    response = requests.post({"email": sys.argv[1]})
    print(response.text)
