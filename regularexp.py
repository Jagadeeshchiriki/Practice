import re
data='''The power of casta living introduces 
    , ths sience of yogq ! and ... restore  @ 34 apr 20020 well-being to '''

# pattern=re.compile(r'\w')
# result= pattern.finditer(data)
# for i in (list(result)):
#     print(i)



# quantifier *, +, ?,{3}, {2,6}

# functions

# match --> find the staring position with using the re
# to start the matching at intial position , return singel object
# matchobj = re.match(r'.+',data)   # '.' ,'\n' , '\d','\D', '\w', '\W' ,'@', '\s', '\S'
# print(matchobj)
# if matchobj:
#     print("matchobj.group() : ",matchobj.group(0))
# else:
#     print("no match!")


# search - search only one time at any where match
# return singe object
# matchobj=re.search(r' .* \d',data)
# print(matchobj)
# if matchobj:
#     print("matchobj.group() : ",matchobj.group(0))
# else:
#     print("no match!")

# find all -- find how many time the pattern match 
# return multiple object
# matchobj=re.findall(r'\d\d',data)
# print(matchobj)
# print(len(matchobj))


#  replace(old, new)
matchobj=re.findall(r'\S',data)
print(matchobj)
# data =data.replace(r'casta','02')
# print(data)

# data= re.sub('casting','02',data)
# print(data)