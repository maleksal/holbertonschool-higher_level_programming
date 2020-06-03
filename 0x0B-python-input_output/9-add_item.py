#!/usr/bin/python3
''' python script '''
import sys

save_to_json_file = __import__('7-save_to_json_file.py').save_to_json_file
load_json_file = __import__('8-load_from_json_file').load_from_json_file
save_to = "add_item.json"

old_json = []
if sys.argv > 0:
    try:
        old_json = load_json_file(save_to)
    except FileNotFoundError:
        pass
    save_to_json_file(old_json + sys.argv[1:], save_to)
