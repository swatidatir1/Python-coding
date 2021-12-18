some_list = ['a', 'b', 'c', 'f', 'd', 'a', 'c', 'd']

Duplicates = []
for letter in some_list:
    if some_list.count(letter) > 1:
        if letter not in Duplicates:
            Duplicates.append(letter)
print(Duplicates)
