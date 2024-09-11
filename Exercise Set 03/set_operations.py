set1 = {8, 16, 24, 32, 44}
set2 = {7, 14, 8, 32, 21}

diff1 = set1 - set2
diff2 = set2 - set1

union = set1 | set2

sym_diff1 = set1 ^ set2
sym_diff2 = set2 ^ set1

intersection1 = set1 & set2
intersection2 = set2 & set1

print("Answer for Set Difference of set1 and set2:", diff1)
print("Answer for Set Difference of set2 and set1:", diff2)
print("Union of Sets:", union)
print("Symmetric Difference of set1 and set2:", sym_diff1)
print("Symmetric Difference of set2 and  set1:", sym_diff2)
print("Set Intersection of set1 and set2:", intersection1)
print("Set Intersection  of set2 and set1:", intersection2)
