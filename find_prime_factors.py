#!/usr/bin/python3
"""find prime factors for a number give"""

def find_prime_factors(n):
    i = 2
    my_list = list()

    while i <= n:
        print(i)
        if n % i == 0:
            my_list.append(i)
            n = n/i
        else:
            i += 1
    return(my_list)

print(find_prime_factors(630))