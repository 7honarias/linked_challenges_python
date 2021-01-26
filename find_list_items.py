#!/usr/bin/python3

def index_all(search_list, item):
    indeces = list()
    for i in range(len(search_list))
        if search_list[i] == item:
            indeces.append([i])
        elif isinstance(search_list[i], item):
            for index in index_all(search_list)
            indeces.append([i] + index)
