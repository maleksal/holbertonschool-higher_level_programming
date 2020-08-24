#!/usr/bin/python3
""" Send request """


if __name__ == "__main__":
    import requests
    import sys

    response = requests.get(sys.argv[1])
    statusCode = response.status_code

    if statusCode >= 400:
        print("Error code: ", statusCode)
    else:
        print(response.text)
