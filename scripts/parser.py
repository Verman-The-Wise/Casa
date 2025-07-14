import os
import shutil
from var import O, I_b, I_p

os.makedirs(O, exist_ok=True) # creates the output DIR.

def parse_kv():

    glossary = []
    BLOK = {}
    last_key = None
    for I in [I_b, I_p]:
        with open(I, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    if BLOK:
                        glossary.append(BLOK)
                        BLOK = {}
                        last_key = None
                    continue
                if ' : ' in line:
                    key, value = line.split(" : ", 1)
                    BLOK[key] = value
                    last_key = key
                else:
                    if last_key:
                        BLOK[last_key] = f"{BLOK[last_key]}\n{line}"
            if BLOK:
                glossary.append(BLOK)
                BLOK = {}
                last_key = None

    return glossary
        
base_data = parse_kv()

# in future (as enteries in both project and chronicle increases i might have to create a new list instead of just using glossary, or maybe i might find a better way to parse which isn't a memory eater.)

