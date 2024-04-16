lucky_number = [4, 8, 114, 16, 23, 43]
friends = ["Kevin", "Michael", "Jin", "Oscar", "Tyler"]

# append list
friends.append("Nicole")

# insert value into a list
friends.insert(1, "Lex")

# remove value from list
friends.remove("Tyler")

# clean list
# friends.clear()

# remove last element from list
friends.pop()

# find element in list
print(friends.index("Jin"))

# sort list
friends.sort()

# reverse list
lucky_number.reverse()

# concatenate lists list
friends.extend(lucky_number)

# copy of a list
friends2 = friends.copy()

print(friends2)