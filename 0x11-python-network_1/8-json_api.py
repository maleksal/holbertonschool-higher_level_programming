#!/usr/bin/python3
""" Send request """


if __name__ == "__main__":
    import requests
    import sys

    url = " http://c0a6ac671e05.9790342a.hbtn-cod.io:5000/search_user"

    # take argument
    data = {"q": sys.argv[1] if len(sys.argv) > 1 else ""}
    response = requests.post(url, data=data)

    if not response.json():
        print("No Result")
    else:
        api_response = response.json()
        try:
            print("[{}] {}".format(api_response["id"], api_response["name"]))
        except (IndexError, KeyError, TypeError):
            print("Not a Valid JSON")
