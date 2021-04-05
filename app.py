#!/usr/bin/python3
import json
import random
import expressions as e

with open("cb_library.json", "r") as file:
    db = json.load(file)

cb_words = db["words"]
units = db["units"]
op_words = {}
op_units = {}

for word in cb_words:
    i = random.randint(0, len( cb_words[word] ) -1 )
    component = cb_words[word][i]
    op_words[word] = component

for word in units:
    i = random.randint(0, len( units[word] ) -1 )
    component = units[word][i]
    op_units[word] = component

e.shitpost(
    op_words['person'],
    op_words['verb'],
    op_words['object'],
    op_words['content'],
    op_units['time'],
    op_words['human part']
)

e.butthurt(
    op_words['human part'],
    op_words['verb'],
    op_words['content']
)