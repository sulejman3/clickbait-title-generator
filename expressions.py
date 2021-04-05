import random

# My brain hurts! I ate too much shit!
def butthurt(human_part, verb, content):
    print(f"My {human_part} hurts! I {verb} too much {content}.")

# A teacher ate 5 blocks of shit for 5 days. See what happened to their brain!
def shitpost(person, verb, obj, content, time_unit, human_part):
    print(f"A {person} {verb} {str(random.randint(1,10))} {obj} of {content} for {str(random.randint(1,10))} {time_unit}. See what happened to their {human_part}!")

expressions = [
    butthurt, shitpost
]