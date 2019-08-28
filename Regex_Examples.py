# Python Regex
import re
reg=r"ab*"  #matches with a, ab, or 'a' followed by any number of 'b's.
stringToBeMatched = "abajdabbbjdea"
print("1.  -- reg=ab* --- " + str(re.findall(reg, stringToBeMatched)))


# use of ?
reg=r"ab?"  #matches with a or ab.
stringToBeMatched = "abajdabbbjdea"
print("1.  -- reg=ab?  --- " + str(re.findall(reg, stringToBeMatched)))

reg=r"^-[0-9]+"
integerStrToBeMatched = "-8788--8999-uhhu"
print("1.  -- reg= ^-[0-9]+ --- " + str(re.findall(reg, integerStrToBeMatched)))


reg=r"-[0-9a-z]+"
integerStrToBeMatched = "-8788--8999-uhhu"
print("2.  -- reg= -[0-9]+ --- " + str(re.findall(reg, integerStrToBeMatched)))


## ? means 0 or 1 occurance
reg=r"-[0-9]+?"
integerStrToBeMatched = "-8788--1999-uhhu- -"
print("3.  -- reg= -[0-9]+?--- " + str(re.findall(reg, integerStrToBeMatched)))


reg=r"-[0-9]*"
integerStrToBeMatched = "-8788--8999-uhhu"
print("4.  -- reg= -[0-9]*--- " + str(re.findall(reg, integerStrToBeMatched)))

strToBematched = '<> b <cas>'
reg=r"<.*?>"
print("5.  -- reg= <.*?> --- " + str(re.findall(reg, strToBematched)))


## To return first word of a sentence
lineToBeMatched = 'AV is 9largest Analytics community of India'
reg = r'^\w+'       #'\w' will match digits too
print("6. To return first word of a sentence --- "
      + str(re.findall(reg, lineToBeMatched)))

## To return first two characters of each word
lineToBeMatched = 'AV is   9largest Analytics community of India'
reg = r'\b\w\w' # or r'\b\w.'   # '\b' is for boundary between word and non-word
print("7. To return first two characters of each word --- "
      + str(re.findall(reg, lineToBeMatched)))

## To return the domain type of given email-id
emailId = 'swati.sharma@st.com yz@test.in, test.first@analyticsvidhya.com,'
#reg = r'@(.*)'      #.matches anything except new line
#i.e., it will also match with space
reg = r'@\w+.\w+'
print("8. To return whole word after @ --- "
      + str(re.findall(reg, emailId)))
reg = r'@\w+.(\w+)'
print("9. To return domain type of given email-Id --- " + str(re.findall(reg,emailId)))


print('10. To get the content between {} --- ' + str(re.findall(r'{(\w+)}', '{duhdhe}{jjnd} {djed}')))

# To return date from a given string
strToFindDateFrom = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'
reg = r'\d{2}-\d{2}-\d{4}'
print('11. To return date from a given string --- ' + str(re.findall(reg, strToFindDateFrom)))
reg =r'\d{2}-\d{2}-(\d{4})'
print('11. To extract only year --- ' + str(re.findall(reg, strToFindDateFrom)))


# To find all words that start with a vowel
strForVowel = 'AV  is  largest Analytics community of India I'
reg = r'\b[aeiouAEIOU]\w+'
print('12. To find all words that start with vowel --- ', re.findall(reg, strForVowel))

# To find all the words starting with consonents
strForConsonents = 'AV  is  largest Analytics community of India I'
reg = r'\b[^aeiouAEIOU]\w+'
print('13.a. To find all words that start with consonents Step 1 --- ', re.findall(reg, strForConsonents))

reg = r'\b[^aeiouAEIOU ]\w+'
print('13.b. To find all words that start with consonents Step 2 --- ', re.findall(reg, strForConsonents))


# Validate a phone number (phone number must be of 10 digits and starts with 8 or 9)
li=['9999999999','999999-999','99999x9999', '83736657785342', '8123456790']
for val in li:
    reg = r'[89]\d{9}'
    print('Out of findall for ', val, ' is ' , re.findall(reg, val))
    if re.match(reg, val) and len(val) == 10:
        print(val,' is a phone number')
    else:
        print(val, ' is not a phone')

# To split a string with multiple delimiter
lineWithDelimeter = 'asdf fjdk;afed,fjek,asdf,foo, test' # String has multiple delimiters (";" , "," , " ").
resultList = re.split(r',\s|[,;\s]', lineWithDelimeter)
print('14. Split with multiple delimeter --- ', resultList)

# To extract information between <td> and </td>
htmlStr = '<tr align="center"><td>1</td> <td>Noah</td> <td>Emma</td></tr>'
reg = r'<td>(\w+)</td>'
print('15. To extract information between <td> and </td> --- ', re.findall(reg, htmlStr))
# To avoid columnn number (1) from output
reg = r'<td>\w+</td>\s<td>(\w+)</td>\s<td>(\w+)</td>'
print('15. To extract information from each column except serial number (1) --- ', re.findall(reg, htmlStr))

###################################################################################
#### Extract the user id, domain name and suffix from the following email addresses
print('#'*75)
print("#### Extract the user id, domain name and suffix from the following email addresses ####")
emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""

reg = r'(\w+)@(\w+)\.(\w+)'     ##\w matches with '_' also
print(re.findall(reg, emails))
## This result can also be obtained by
## reg = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})' 
## re.findall(reg, emails, flags=re.IGNORECASE)


###################################################################################
#### Retrieve all the words starting with ‘b’ or ‘B’ from the following text ####
print('#'*75)
print("#### Retrieve all the words starting with ‘b’ or ‘B’ from the following text ####")
text = """Betty bought a bit of butter,
But the butter was so bitter, So she bought some better butter,
To make the bitter butter better."""

reg = r'\b[Bb]\w*'
print(re.findall(reg, text))

###################################################################################
#### Split the following irregular sentence into words ####
print('#'*75)
print("#### Split the following irregular sentence into words ####")
sentence = """A, very   very; irregular_sentence"""
## desired_output = "A very very irregular sentence"
reg = r'[,;_\s]+'
print(" ".join(re.split(reg, sentence)))


###################################################################################
#### Clean up the following tweet so that it contains only the user’s message.
###That is, remove all URLs, hashtags, mentions, punctuations, RTs and CCs.

print('#'*75)
print("#### Clean up the tweet ###")
## tweet = '''Good advice! RT @TheNextWeb: What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

## desired_output = 'Good advice What I would do differently if I was learning to code today'

tweet = '''Good advice!  RT @TheNextWeb:
What I would do differently if I was learning to code today
http://t.co/lbwej0pxOd cc: @garybernhardt #rstats'''

tweet = re.sub(r'cc\S+', '', tweet)
tweet = re.sub(r'[!,]', '', tweet)
tweet = re.sub(r'http\S+\s*', '', tweet)
tweet = re.sub(r'#\S+\s*', '', tweet)
tweet = re.sub(r'@\S+\s*', '', tweet)
tweet = re.sub(r'RT\s*', '', tweet)
tweet = re.sub(r'\s+', ' ', tweet)

print(tweet)

###############################################################################
### Extract all the text portions between the tags
### from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html
print('#'*75)
print('### Extract all the text portions between the HTML tags ###')
import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
text = r.text
reg = r'<.*?>(.*)</.*?>'    ## r'<.*?>(\w*)</.*?>' is not working here.??
print(re.findall(reg, text))

##############################################################################################
### Grouping by Number using match.group ###
print('#'*75)
print('### Grouping by number using match.group ###')
contactInfo = 'Doe, John: 555-1212'
match = re.search(r'(\w+), (\w+): (\S+)', contactInfo)
print(match.group(1),"---",match.group(2),'---', match.group(3),'---' )

print('### Grouping by NAME using match.group ###')
match = re.search(r'(?P<last>\w+), (?P<first>\w+): (?P<phone>\S+)', contactInfo)
print(match.group('last'),"---",match.group('first'),'---', match.group('phone'),'---' )


