# Two strings are said to be anagram
# if we can form one string by arranging the characters of another string.
# For example, Race and Care.
str1 = input()
str2 = input()

str1, str2 = str1.lower(), str2.lower()

if len(str1) == len(str2):
    if sorted(str1) == sorted(str2):
        print('Anagram')
    else:
        print('Not Anagram')
else:
    print('Not Anagram')
