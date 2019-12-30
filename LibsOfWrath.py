# LibsOfWrath
Madlibs project based on classic novels
##IMPORT MODULES
import time
import urllib.request
import random
#import nltk
import nltk
import nltk.tokenize as nt
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

booklist_number= {1: "Dracula", 2:"A Tale of Two Cities", 3: "Sherlock Holmes"}

booklist_url_dict= {"Dracula":"http://www.gutenberg.org/cache/epub/345/pg345.txt", 
"A Tale of Two Cities":"https://www.gutenberg.org/files/98/98-0.txt",
"Sherlock Holmes": "https://www.gutenberg.org/files/1661/1661-0.txt"}

booklist_author= {"Dracula": "Stoker", "A Tale of Two Cities": "Dickens", "Sherlock Holmes": "Conan Doyle"}

fake_book_title= {"Dracula": "Madlib-ula", "A Tale of Two Cities": "A Tale of Two Libs", "Sherlock Holmes": "Sherlib Holmes"}

# DEFINE FUNCTIONS
# Function to read files
def readfiletostr(filename):
  with open(filename, 'r') as file:
    file2= file.read()
  return file2

# Function to read a URL text file
def readurltxt(url):
  response = urllib.request.urlopen(url)
  web_content = response.read()
  return web_content

#function to convert bytes type from website to string
def byte_to_str (filenameinbytes):
  filenameinbytes= filenameinbytes.decode("utf-8")
  return filenameinbytes

# Function to convert string to list
def Convert(str): 
    li = list(str.split(", ")) 
    return li

# create empty list of nouns to hold user input
noun_user_list=[]

# create empty list of adjs to hold user input
adj_user_list=[]


print("")
print("")
print ("Welcome to the Libs of Wrath")
print("")
print("")

# wait a few seconds
time.sleep(2)

print("I hope you have been reading up!  This game includes {} books to choose from" .format(len(booklist_url_dict)))
print("")
print("")

# wait a few seconds
time.sleep(2)

# print instructions
print("In this game, you will fill in where the authors left off.  You will fill in adjcectives and nouns to make the original text more (or less) readable")

print("")
time.sleep(3)

#Ask for the name of the player
user_name=input("What is your name?  ").title()
print("")
print("")
time.sleep(2)
print("Thank you", user_name, "!")

time.sleep(2)
# The user chooses a book
print("As I mentioned, this game has {} books for you to choose from.  Please choose a number from the list below of the book that you would like:". format(len(booklist_url_dict)))

print("")
print("")

for book in booklist_number:
  print("{}. {}".format(book, booklist_number[book]))
  # print(book, booklist_number[book])

book_number= int(input("Please choose a book number >  "))
book_title= booklist_number[book_number]

#READ FILES
#  Read the file from the webfile dictionary (web version is working).
read_book_url= readurltxt(booklist_url_dict[book_title])

# converting the file type to string
read_book_url= byte_to_str(read_book_url)

#this is the characters of text that I want read
book_characters={"Dracula": read_book_url[5356:5919], "A Tale of Two Cities": read_book_url[2658:3090], "Sherlock Holmes": read_book_url[2420:3237]}

read_book_url= book_characters[book_title]

#This gives all of the types of words in a different text
text=read_book_url

ss=nt.sent_tokenize(text)
tokenized_sent=[nt.word_tokenize(sent) for sent in ss]
pos_sentences=[nltk.pos_tag(sent) for sent in tokenized_sent]
# print(pos_sentences)

# This gives only nouns
orig_noun_list_pre_random= []
for sentences in pos_sentences:
  for sentence in sentences:
    if (sentence[1]=='NN') or (sentence[1]=="NNS"):
      orig_noun_list_pre_random.append(sentence[0])

#choosing five random nouns (so that the user doesn't need to enter so many)
orig_noun_list=[]
while len(orig_noun_list)<5:
  random_noun=random.choice(orig_noun_list_pre_random)
  if random_noun in orig_noun_list:
    continue
  else:
    orig_noun_list.append(random_noun)

#print (orig_noun_list)

# This gives only adjectives
orig_adj_list_pre_random= []
for sentences in pos_sentences:
  for sentence in sentences:
    if (sentence[1]=='JJ') or (sentence[1]=="JJR") or (sentence[1]=="JJS"):
      orig_adj_list_pre_random.append(sentence[0])

#choosing five random adj (so that the user doesn't need to enter so many)
orig_adj_list=[]
while len(orig_adj_list)<4:
  random_adj=random.choice(orig_adj_list_pre_random)
  if random_adj in orig_adj_list:
    continue
  else:
    orig_adj_list.append(random_adj)


# wait a few seconds
print("")
print("")
time.sleep(3)
# print defination of adjective and noun
print ("I understand that you, "+ user_name+ ", like to read, but I wanted to give you a quick recap.  A noun is an object, such as a dog, a glass of water, or Charles Dickens.")
print("")
print("")
time.sleep(7)

print ("Let's get started!" )
time.sleep(2)
print("""

""")

print("First I am going to ask for a list of several nouns")
time.sleep(2)
print("""

""")

i=0
while i<len(orig_noun_list):
  noun_num= input("Please give me an noun >")
  noun_user_list.append(noun_num)
  i=i+1

print("")
time.sleep(2)
print("Thanks for those excellent nouns!")
print("")
time.sleep(2)

print ("Now its time to enter some adjectives")

print("An adjective is something that is used to describe the noun, such as marshmellowy, grey, or silken." )
# wait a few seconds
print("")
print("")
time.sleep(7)
print("")
print("")

print("I hope you had time to think of an adjective or two!  I am going to ask you for several adjectives")

time.sleep(4)

#create list of adjectives from user input
i=0
while i<len(orig_adj_list):
  adj_num= input("Please give me an adjective >")
  adj_user_list.append(adj_num)
  i=i+1

print("")
print("")
time.sleep(2)
print("Thanks for those adjectivey adjectives!")
print("")
time.sleep(2)

print("")
time.sleep(2)
print("Your writing is goofy!")
print("")
time.sleep(2)

time.sleep(2)
print("I'm ready to read it to you")
print("")
time.sleep(2)

print("")
time.sleep(2)
print("ready?!")
print("")
time.sleep(2)

#Substitute words from the adj lists into the novel text
i=0
for word in orig_adj_list:

  if (i< len(orig_adj_list)) and (word in read_book_url):
    read_book_url = read_book_url.replace(word, adj_user_list[i])
    i=i+1

#Substitute words from the noun lists into novel text
i=0
for word in orig_noun_list:
  if (i< len(orig_noun_list)) and (word in read_book_url):
    read_book_url = read_book_url.replace(word, noun_user_list[i])
    i=i+1

print (fake_book_title[book_title])
time.sleep(4)
print("")

print("by "+ user_name, booklist_author [book_title])
time.sleep(2)
print("""

""")

# print(taleoftwocities_modified)
print (read_book_url)

time.sleep(15)
print("""

""")

print("Thanks for playing!")
