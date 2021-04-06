#!/usr/bin/python3

import random
import json

def dict_gen(database):
    with open(database, "r") as file:
        db = json.load(file)
    
    op_db = {}
    for family_key, family_values in db.items():
        op_wordtype = {}
        for wordtype_key, wordtype_values in family_values.items():
            i = random.randint(0, len(wordtype_values) -1 )
            rolled_word = wordtype_values[i]
            op_wordtype[wordtype_key] = rolled_word
        op_db[family_key] = op_wordtype
    return op_db


def clickbaits(db):
    words = db['words']
    units = db['units']
    num1 = str(random.randint(1,10))
    num2 = str(random.randint(1,10))

    clickbaits = [
        f"My {words['human part']} hurts! I {words['verb']} too much {words['content']}.",
        f"A {words['person']} {words['verb']} {num1} {words['object']} of {words['content']} for {num2} {units['time']}. See what happened to their {words['human part']}!"
    ]
    clickbait = random.choice(clickbaits)
    return clickbait


# example output:
# My brain hurts! I ate too much shit!
def butthurt(db):
    words = db["words"]
    print(f"My {words['human part']} hurts! I {words['verb']} too much {words['content']}.")


# example output:
# A teacher ate 5 blocks of shit for 5 days. See what happened to their brain!
def shitpost(db):
    words = db['words']
    units = db['units']
    num1 = str(random.randint(1,10))
    num2 = str(random.randint(1,10))
    print(f"A {words['person']} {words['verb']} {num1} {words['object']} of {words['content']} for {num2} {units['time']}. See what happened to their {words['human part']}!")


if __name__ == "__main__":
    for _ in range(20):
        db = dict_gen("cb_library.json")
        print(clickbaits(db))