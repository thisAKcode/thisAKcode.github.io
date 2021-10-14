title: Namedtuple Can Become a Json
date: 2021-10-14 22:27
author: Alex

#  How Once I Needed To Converte namedtuple

### Shrotly about problem

I once needed to make a json of following form from list of strings ["lorem", "ipsum"]
```json
lorem_fields = [{
  "tag": "input",
  "name": "lorem",
  "type": "text",
  "human_label": "Lorem"
}, {
  "tag": "input",
  "name": "ipsum",
  "type": "text",
	"human_label": "ipsum"
}]
```
### Code:
```python

from collections import namedtuple
import json


LociFormNt = namedtuple("LociFormNt",("tag", "name", "type", "human_label"))
def field_populator(list_of_str):
    
    listofnt = [LociFormNt("input", f"{thing}", "text", f"{thing}".title()) for thing in list_of_str]
    # json.dumps(fb._asdict())
    dict_list = [json.dumps(i._asdict()) for i in listofnt]
    return dict_list

if __name__ == "__main__":
    
    lista = [ "Magnit", "Rospechat", "Over railroad bridge", "Records booth", "Buss station", "Farm marknad", "Household stuff store", "Thousand little things", "Clothing market", "Fruit stall"]
    print(field_populator(lista))

```