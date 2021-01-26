#!/usr/bin/python3
"""recive a str and identify if is palindrome or not"""
import re

def identify_palindrome(str):
    forwards = ''.join(re.findall(r'[a-z]+', str.lower()))
    backwards = forwards[::-1]
    return (forwards == backwards)

print(identify_palindrome("hola mundo primer program"))