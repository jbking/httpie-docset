import sqlite3

from bs4 import BeautifulSoup

bs = BeautifulSoup(
    open("HTTPie.docset/Contents/Resources/Documents/README.html").read(),
    features="html.parser")

with sqlite3.connect("HTTPie.docset/Contents/Resources/docSet.dsidx") as db:
    db.execute("DROP INDEX IF EXISTS anchor;")
    db.execute("DROP TABLE IF EXISTS searchIndex;")
    db.execute("CREATE TABLE searchIndex(id INTEGER PRIMARY KEY, name TEXT, type TEXT, path TEXT);")
    db.execute("CREATE UNIQUE INDEX anchor ON searchIndex(name, type, path);")
    for section_div in bs.find_all("div", attrs={"class": "section"}):
        name = None
        for i in range(1, 7):
            try:
                name = section_div.find("h%d" % i).text
                break
            except AttributeError:
                pass
        else:
            raise ValueError("Unexpected: " + str(section_div))
        section_id = section_div.attrs["id"]
        path = "README.html#" + section_id
        db.execute("INSERT OR IGNORE INTO searchIndex(name, type, path) VALUES(?, 'Section', ?);", (name, path))
