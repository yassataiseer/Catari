#### search algrothim to find images

from difflib import SequenceMatcher
import sqlite3
conn = sqlite3.connect('images.db',check_same_thread=False)
c = conn.cursor()

class find:
    def get_value(val):
        hashtags = find.dictionary()
        answer = []
        for key, value in hashtags.items():
            for components in value:
                if find.similar(val,components)>=0.6:
                    if key+".jpg" in answer:
                        pass
                    else:
                        a = key+".jpg"
                        answer.append(a)
                else:
                    pass
        return answer              
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

  
            
#print(search.get_key("cute cat"))


