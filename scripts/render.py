from var import O, I_b, I_p
from parser import base_data
import os

def write_data(glossary):
    for BLOK in glossary:
        title = BLOK.get("TITL", "Untitled")
        description = BLOK.get("BODY", "No content available.")
        if "RELI" in BLOK:
            reli = BLOK.get("RELI", "Link not given")
            with open("layout/project.html") as proj_file:
                template_proj = proj_file.read()
                html_proj = template_proj.format(title = title, description = description, reli = reli)
                
                url = title.replace(' ', '-').lower() + ".html"
                with open(os.path.join(O, url), "w", encoding='utf-8') as h:
                    h.write(html_proj)

        else:
            with open("layout/base.html", "r") as file:
                template_base = file.read()
            
            html_base = template_base.format(title = title, description = description) 

            url = title.replace(' ', '-').lower() + ".html"
            with open(os.path.join(O, url), "w", encoding='utf-8') as h:
                h.write(html_base)
        print(url)

def main():
    write_data(base_data)
    
main()