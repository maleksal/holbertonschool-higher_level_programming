#!/usr/bin/python3
""" Handle error code """


if __name__ == "__main__":
    import requests

    url = "https://intranet.hbtn.io/status"
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
