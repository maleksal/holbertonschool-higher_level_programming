#!/usr/bin/python3
""" Handle error code """


if __name__ == "__main__":
    from urllib import error, request
    import sys

    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
