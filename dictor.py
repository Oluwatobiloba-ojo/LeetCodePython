word = "Africa"
dictonary = {n: n + "ace" for n in word}
print(dictonary)
for wrd in word:
    dictonary[wrd] = "ace"
print(dictonary)
dictonary.pop(word[3])
print(dictonary)

# set is not a key value function in which when declare must use built-in function set(1, 2, 3)

value = {1, 2, 3, 4}
for i in value:
    if i % 2 == 0:
        print(i)
print(value)
print(set(dictonary))
lists = [1, 1, 3, 4, 5, 6, 7]
lists = set(lists)
print(lists)
print(value.difference_update(lists))
print(frozenset(value))
value = list(value)
print(value)
