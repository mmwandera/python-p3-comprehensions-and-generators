#!/usr/bin/env python3

#Using a list comprehension, write a function return_evens() that returns a list of all of the even elements of a sequence of integers.
def return_evens(num_list):
    return [num for num in num_list if num % 2 == 0]

#Using a list comprehension, write a function make_exclamation() that takes a list of strings and returns a list of strings with an exclamation mark after each string.
def make_exclamation(sentence_list):
    return [sentence + "!" for sentence in sentence_list]