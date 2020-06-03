#!/usr/bin/python3
''' python script '''

if __name__ == '__main__':
    import sys
    save_to_json_file = __import__('7-save_to_json_file.py').save_to_json_file
    load_json_file = __import__('8-load_from_json_file').load_from_json_file
    save_to = "add_item.json"

    if sys.argv > 0:
        load_json_file(save_to)
        save_to_json_file(sys.argv[1:], save_to)
