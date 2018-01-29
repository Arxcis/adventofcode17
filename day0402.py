#!python
# -*- coding:utf-8 -*-
# --- Day 4: High-Entropy Passphrases ---

# --- Part Two ---

SMALL_LETTERS_ASCII_OFFSET = 97

def passphrase_has_anagram(passphrase):

    words = passphrase.split()

    signatures = dict()
    for word in words:

        letter_counter = [0 for x in range(26)]

        for letter in word:
            ordletter = ord(letter) - SMALL_LETTERS_ASCII_OFFSET
            letter_counter[ordletter] += 1

        signature = ""
        for counter in letter_counter:
            signature += str(counter) + "-"

        if signature in signatures:
            return True

        signatures[signature] = 1
    return False
    
    

if __name__ == "__main__":
    count = 0
    with open('day04.data','r') as file:
        for passphrase in file: 
            if not passphrase_has_anagram(passphrase):
                count += 1

    print(count)

