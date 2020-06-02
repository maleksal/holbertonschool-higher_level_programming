#!/usr/bin/python3


""" MyList Module """


class MyList(list):
    ''' MyList class, inherts from list '''

    def print_sorted(self):
        '''
        prints the list, but sorted (ascending sort)
        '''
        print(sorted(self))
