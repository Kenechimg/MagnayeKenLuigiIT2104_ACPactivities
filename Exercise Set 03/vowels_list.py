vowels = "aeiouAEIOU"  
string = input("Enter a string: ") 
list = [char for char in string if char in vowels]

print(list)