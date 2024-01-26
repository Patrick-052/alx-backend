#!/usr/bin/env python3
""" Determining indexes range for pagination """


def index_range(page, page_size):
    """ Returns a tuple containing a range of indexes """
    return ((page - 1) * page_size, page * page_size)
