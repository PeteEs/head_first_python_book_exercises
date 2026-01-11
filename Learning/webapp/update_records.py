import gazpacho
import json

URL = "https://en.wikipedia.org/wiki/List_of_world_records_in_swimming"
RECORDS = (0, 1, 3, 4)
COURSES = ("LC Men", "LC Women", "SC Men", "SC Women")
WHERE = ""
JSONDATA = "records.json"

html = gazpacho.get(URL)
soup = gazpacho.Soup(html)

tables = soup.find("table")

records = {}

for table_idx, course in zip(RECORDS, COURSES):
    records[course] = {}

    for row in tables[table_idx].find("tr")[1:]:
        columns = row.find("td")
        event = columns[0].text.strip()
        time = columns[1].text.strip()

        if "relay" not in event.lower():
            records[course][event] = time

with open(WHERE + JSONDATA, "w", encoding="utf-8") as jf:
    json.dump(records, jf, ensure_ascii=False, indent=2)