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

    try:
        api_respoonse = response.json()
    except ValueError:
        # no JSON returned
        print("Not a Valid JSON")

    if api_respoonse:
        try:
            print("[{}] {}".format(api_respoonse["id"], api_respoonse["name"]))
        except (IndexError, KeyError, TypeError):
            print("No Result")
