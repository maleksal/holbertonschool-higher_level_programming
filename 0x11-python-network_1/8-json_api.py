#!/usr/bin/python3
""" Send request """


if __name__ == "__main__":
    import requests
    import sys

    url = "http://0.0.0.0:5000/search_user"
    # take argument
    arg = sys.argv[1]

    if not arg:
        arg = ""
    response = requests.post(url, {"q": arg})

    if not response.json():
        print("No Result")
    else:
        try:
            print("[{}] {}".format(api_respoonse["id"], api_respoonse["name"]))
        except (IndexError, KeyError, TypeError):
            print("Not a Valid JSON")
