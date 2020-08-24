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
        api_r = response.json()
        if not api_r:
            print("No result")
        else:
            print("[{}] {}".format(api_r.get("id"), api_r.get("name")))
    except ValueError:
            print("Not a valid JSON")
