#!/usr/bin/python3
""" Send request """


if __name__ == "__main__":
    import requests
    import sys

    url = " http://0.0.0.0:5000/search_user"

    # take argument
    data = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}
    response = requests.post(url, data=data)

    try:
        if not response.json():
            print("No Result")
        else:
            api_r = response.json()
            print("[{}] {}".format(api_r.get("id"), api_r.get("name")))
    except ValueError:
            print("Not a Valid JSON")
