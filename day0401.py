#!python
# -*- coding:utf-8 -*-
# --- Day 4: High-Entropy Passphrases ---

def passphrase_is_valid(passphrase):

    words = passphrase.split()
    passphrasedict = dict()

    for word in words:
        if word in passphrasedict:
            print("NOTVALID", word, "->", passphrase)
            return False
        passphrasedict[word] = 1

    print("VALID   ", passphrase)
    return True

if __name__ == "__main__":
    count = 0
    with open('day04.data','r') as file:
        for passphrase in file: 
            if passphrase_is_valid(passphrase):
                count += 1

    print(count, length)