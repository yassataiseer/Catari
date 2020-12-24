from difflib import SequenceMatcher


hashtags = {"pic_one":["#cat","#cute"] ,"pic_two":["#baby","#cute"],"pic_three":["#laptop"]}
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_key(val):
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
            
 

#print(similar("curcatsast","cat")) 

for i in hashtags:
    for x in hashtags[i]:
        x = str(x)
        print(get_key('#cute'))





'''
query = []
a = "#hastag#youtube#funguy"
a = a.split("#")
for i in a:
    if len(i) == 0:
        pass
    else:
        i = "#"+i
        query.append(i)
    
print(query)'''

