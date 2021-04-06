#!/usr/bin/python3
import expressions as e

db = e.dict_gen("cb_library.json")
print(e.clickbaits(db))