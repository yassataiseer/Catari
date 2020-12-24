from difflib import SequenceMatcher


hashtags = {"pic_one":["#cat","#water"]}
def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_key(val):
    for key, value in hashtags.items():
        for components in value:
            if similar(val,components)>=0.5:
                return key
            else:
                return "no"
                
            


#print(similar("curcatsast","cat")) 

#for i in hashtags:
#    for x in hashtags[i]:
#        x = str(x)
#        print(get_key('#cat'))

query("")
a = "#hastag#youtube#funguy"
a = a.split("#")
for i in a:
    i = "#"+i
print(a)

