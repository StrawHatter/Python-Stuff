lover1 = raw_input('Enter the first person: ')
lover2 = raw_input('Enter the second person: ')

total = 0

s = ''.join([lover1, lover2])

for i in s.upper():
    total += ord(i)

compatibility = total % 100
print "%s and %s have a %d compatibility!" % (lover1, lover2, compatibility)
