#### search algrothim to find images

from difflib import SequenceMatcher
import sqlite3
conn = sqlite3.connect('images.db')
c = conn.cursor()


def dictionary():
    hastags = {}
    values_images = c.execute("SELECT * FROM stuffToPlot")
    data = c.fetchall()
    for i in data:
        a = i[1].split("#")
        del a[0]
        for x in a:
            if len(x)==0:
                pass
            else:
                x = "#"+x
                hastags[i[0]] = a
        #print(i[0])
        #print(i[1])
    return hastags


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_key(val):
    hashtags = dictionary()
    answer = []
    for key, value in hashtags.items():
        for components in value:
            if similar(val,components)>=0.5:
                if key in answer:
                    pass
                else:
                    answer.append(key)
            else:
                pass
    return answer                
            
#print(get_key("baby"))


