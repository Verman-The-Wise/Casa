import os
import shutil

I = "element/chronicle.kv"
O = "to-world"

os.makedirs(O, exist_ok=True) # creates the output DIR.
shutil.copy("style.css", O)   # copies the style.css to output DIR.

def parse_taia():
    glossary = []
    with open(I, "r") as FILE:
        BLOK = {}
        for line in FILE:
            line = line.strip()
            if line:
                key, val = line.split(" : ", 1)
                BLOK[key] = val
            else:
                glossary.append(BLOK)
                BLOK = {}
        if BLOK:
            glossary.append(BLOK)

        return glossary
        
data = parse_taia()

def write_data(glossary):
    for BLOK in glossary:
        title = BLOK.get("TITL", "Untitled")
        description = BLOK.get("BODY", "No content available.")
        html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title}</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
<h2>{title}</h2>
<main>
{description}
<footer><p>Aenwyn</p></footer>
</main>
</body>
</html>
"""
        url = title.replace(' ', '-').lower() + ".html"
        with open(os.path.join(O, url), "w", encoding='utf-8') as h:
            h.write(html)
        print(url)
    
def main():
    write_data(data)
    
main()
