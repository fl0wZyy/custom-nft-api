import json
import random
data = {}
data['id'] = 2
data["bitmap"] = ''
for i in range(0,100,10):
    for j in range(0, 100, 10):
        r = lambda: random.randint(0, 255)
        color = '#%02X%02X%02X' % (r(), r(), r())
        data["bitmap"]+=color

with open ('data.json', 'w') as f:
    json.dump(data, f, indent = 4)