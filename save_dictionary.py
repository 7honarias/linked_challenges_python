#!/usr/bin/python3
"""this functions save dictionary and load"""
import pickle

def save_dict(dict_to_save, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(dict_to_save, file)

def load_dict(file_path):
    with open(file_path, 'rb') as file:
        return pickle.load(file)

save_dict({"hola": "hi"}, "saludo.txt")
print(load_dict("saludo.txt"))