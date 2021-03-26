print("Hi") 
'''
print( "Задание№ 1") 
print("You are given a string with words and numbers\
        separated by whitespaces (one space).\
        The words contains only letters.\
        You should check if the string contains three words in succession.\
        For example, the string\
        'start 5 one two three 7 end' contains three words in succession.\
        ")      
def checkio(words: str) -> bool:
    import re
    b= words
    #
    pattern = r"[a-zA-Z]"
    b = re.sub(pattern, "@", b, count=0)
    b = b.split()
    #print(b)
    c =[]
    i =0
    count =0 
    while i< len(b ):
        

        if "@" in b[i]:
            count = count +1
            if count>=3:
                break
                return True
        else:
            count = 0
        i =i +1
    if count>=3:
        return True
    else:
        return False

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(checkio("Hello World hello"))
    
    assert checkio("one two 3 four five six 7 eight 9 ten eleven 12") == True, "Hello"
    assert checkio("He is 123 man") == False, "123 man"
    assert checkio("1 2 3 4") == False, "Digits"
    assert checkio("bla bla bla bla") == True, "Bla Bla"
    assert checkio("ww w .  1w ") == False, "Hi"
    #print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
print("Успешно")


print( "Задание№ 2") 
print("You are given a string where you have to find its first word.\
When solving a task pay attention to the following points:\
There can be dots and commas in a string.\
A string can start with a letter or, for example, a dot or space.\
A word can contain an apostrophe and it's a part of a word.\
The whole text can be represented with one word and that's it.\
Input: A string.\
Output: A string.")

import re
def first_word(text: str) -> str:
    
    pattern = r"[a-zA-Z']+"
    b = re.search(pattern, text)   
      
    
    return b[0]


if __name__ == '__main__':
    print("Example:")
    print(first_word("Hello world"))
   
    # These "asserts" are used for self-checking and not for an auto-testing
    assert first_word("Hello world") == "Hello"
    assert first_word(" a word ") == "a"
    assert first_word("don't touch it") == "don't"
    assert first_word("greetings, friends") == "greetings"
    assert first_word("... and so on ...") == "and"
    assert first_word("hi") == "hi"
    assert first_word("Hello.World") == "Hello"
    print("Coding complete? Click 'Check' to earn cool rewards!")
    
print( "Задание№ 3")
print("How old are you in a number of days?\
    It's easy to calculate - just subtract your birthday from today.\
     We could make this a real challenge though and count the difference between any dates.\
You are given two dates as an array with three numbers - a year, month and day.\
 For example: 19 April 1982 will be (1982, 4, 19).\
  You should find the difference in days between the given dates.\
   For example between today and tomorrow = 1 day.\
    The difference will always be either a positive number or zero,\
     so don't forget about the absolute value.\
Input: Two dates as tuples of integers.\
Output: The difference between the dates in days as an integer.")

def days_diff(a, b):
    # your code here
    import datetime
    
    s = list(a)
    c = list(b)
    r = datetime.datetime(*s)
    k = datetime.datetime(*c)
    #
    # Вычисляем разницу между датами
    difference = k - r
    #print(difference, type(difference))
    #print(difference.days)
    #print(s, r)
    return abs(difference.days)
    
    

if __name__ == '__main__':
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

   

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")

print( "Задание№ 4")
print("You need to count the number of digits in a given string.")
def count_digits(text: str) -> int:
    # your code here
    

    l = list(text)
    #print(l)
    i=0
    c =[]
    pattern = [str(x) for  x in range(10)]
    while i <len(l):
        if l[i] in pattern:

            c.append(l[i])
        i = i +1

    return len(c)   


if __name__ == '__main__':
    print("Example:")
    print(count_digits('hi'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_digits('hi') == 0
    assert count_digits('who is 1st here') == 1
    assert count_digits('my numbers is 2') == 1
    assert count_digits('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 8
    assert count_digits('5 plus 6 is') == 2
    assert count_digits('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")



print( "Задание№ 4")
print("In a given string you should reverse every word, \
    but the words should stay in their places.")
def backward_string_by_word(text: str) -> str:
    # your code herereturn None
    
    
    a  = text.split(" ")
    
    b =[]
    for each in a:
        c = each[::-1]
        
        b.append(c)
        d = (" ").join(b)
    return d


if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'


print( "Задание№ 5")
print ("You have a table with all available goods in the store. \
    The data is represented as a list of dicts \
    Your mission here is to find the TOP most expensive goods. \
    The amount we are looking for will be given as a first argument \
    and the whole data as the second one")

def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    # your code here
    b = []
    for x in data:
        b.append(x["price"])

    с = 0
    b.sort()
    b.reverse()
    #print(b)

    f =[] 
    i=0
    while i < len(b):
        for x in data:
            if x["price"] == b[i]:
                f.append(x)
        i= i +1

    
    return f[0:limit]


if __name__ == '__main__':
    from pprint import pprint
    print('Example:')
    pprint(bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]))

    # These "asserts" using for self-checking and not for auto-testing
    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ], "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}], "Second"

    print('Done! Looks like it is fine. Go and check it')
    
limit = 2
data = [
    {"name": "bread", "price": 100},
    {"name": "wine", "price": 138},
    {"name": "meat", "price": 15},
    {"name": "water", "price": 1}
]

b = []
for x in data:
    b.append(x["price"])

с = 0
b.sort()
b.reverse()
print(b)

f =[] 
i=0
while i < len(b):
    for x in data:
        if x["price"] == b[i]:
            f.append(x)
    i= i +1

print(f[0:limit])


print( "Задание№ 6")
print ("You are given a string and two markers (the initial and final).\
 You have to find a substring enclosed between these two markers. But there are a few important conditions:\
The initial and final markers are always different.\
If there is no initial marker, then the first character should be considered the beginning of a string.\
If there is no final marker, then the last character should be considered the ending of a string.\
If the initial and final markers are missing then simply return the whole string.\
If the final marker comes before the initial marker, then return an empty string.")
def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    # your code here
    
    if  begin in text and end in text:
        a = text.split(begin)
        if end in a[1]:
            b = a[1].split(end)
            return b[0]
        else:
            return ""
    
    elif  begin in text and end not in text  :
        a = text.split(begin)
        return  a[1] 
    
    elif  begin not in text and end  in text  :
        a = text.split(end)
        return  a[0]
    
    elif  begin not in text and end  not in text  :
        return  text  



if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')



print( "Задание№ 7")
print ("You are given a non-empty list of integers (X). For this task, \
    you should return a list consisting of only the non-unique elements\
     in this list. To do so you will need to remove all unique elements \
     (elements which are contained in a given list only once). When solving \
     this task, do not change the order of the list. Example: [1, 2, 3, 1, 3]\
      1 and 3 non-unique elements and result will be [1, 3, 1, 3].")
def checkio(data: list) -> list:
    #Your code here
    #It's main function. Don't remove this function
    #It's used for auto-testing and must return a result for check.  

    #replace this for solution
    i = 0
    while i < len(data):
        f = data.count(data[i])
        

        if f == 1:
            
            data.remove(data[i])
            i= 0
            
        else:
            i = i+1
    return data

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list

if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")


print( "Задание№ 8")
print ("In this mission your task is to determine the popularity of certain words in the text.\
At the input of your function are given 2 arguments: the text and the array of words the popularity \
of which you need to determine.\
When solving this task pay attention to the following points:\
The words should be sought in all registers. This means that if you need to find a word \"one\" then\
words like \"one\", \"One\", \"oNe\", \"ONE\" etc. will do.\
The search words are always indicated in the lowercase.\
If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value. \
")

def popular_words(text: str, words: list) -> dict:
    # your code here
    text = text.lower()
    text_list = text.split("\n")
    #print(text_list)
    text = (" ").join(text_list)
    data  = text.split(" ")

    #print(data)
    c ={}
    
    for each in words:
        f = data.count(each)
        c[each] = f
      
    return c



if __name__ == '__main__':
    print("Example:")
    print(popular_words(\'''
When I was One
I had just begun
When I was Two
I was nearly new
\''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words(\'''
When I was One
I had just begun
When I was Two
I was nearly new
\''', ['i', 'was', 'three', 'near']) == {
        'i': 4,
        'was': 3,
        'three': 0,
        'near': 0
    }
    print("Coding complete? Click 'Check' to earn cool rewards!")
'''
print( "Задание№ 9")
print("You are given two strings and you have to find an index of the second\
 occurrence of the second string in the first one.\
Let's go through the first example where you need to find the second \
occurrence of 's' in a word 'sims'. Its easy to find its first occurrence\
 with a function index or find which will point out that 's' is the first \
   symbol in a word 'sims' and therefore the index of the first occurrence is 0.\
   But we have to find the second 's' which is 4th in a row and that means that the \
index of the second occurrence (and the answer to a question) is 3.")

def second_index(text: str, symbol: str) -> [int, None]:
    """
        returns the second index of a symbol in a given text
    """
    # your code herelist.index(x[, start[, end]])
    #print(text.index(symbol))

    a = list(enumerate(text))
    b =[]
    for each in a:
        if symbol in each:
            b.append(each)
    if len(b)>1:
        return b[1][0]
    else:
        return None


if __name__ == '__main__':
    print('Example:')
    print(second_index("hi", " "))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert second_index("sims", "s") == 3, "First"
    assert second_index("find the river", "e") == 12, "Second"
    assert second_index("hi", " ") is None, "Third"
    assert second_index("hi mayor", " ") is None, "Fourth"
    assert second_index("hi mr Mayor", " ") == 5, "Fifth"
    print('You are awesome! All tests are done! Go Check it!')

print("Успешно")

