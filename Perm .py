from itertools import permutations
import enchant
def convert2String(tup):
    return_value=''
    for i in tup:
        return_value+=i
    return return_value
global dic
dic=enchant.Dict("en_US")
value=permutations(input('Enter word:'))

for itr in value:
    if dic.check(convert2String(itr)):
        print(convert2String(itr) )
    


