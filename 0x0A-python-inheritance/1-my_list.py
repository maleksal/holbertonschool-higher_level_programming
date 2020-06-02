#!/usr/bin/python3


""" MyList Module """


class MyList(list):
    ''' Mylist class, inherts from list '''

    def print_sorted(self):
        '''
        prints the list, but sorted (ascending sort)

        Args:
            self: list

        '''
        print(sorted(self))
