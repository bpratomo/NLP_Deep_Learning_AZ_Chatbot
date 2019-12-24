### Import Libraries 
import numpy 
# import tensorflow as tf 
import re 
import time


##################################################################
#### Part 1 - Data Preprocessing 
#################################################################


# Import the dataset
lines = open('corpus/movie_lines.txt',encoding='utf-8',errors='ignore',mode='r').read().split('\n')
print(type(lines))
conversations = open('corpus/movie_conversations.txt',encoding='utf-8',errors='ignore',mode='r').read().split('\n')
print(type(conversations))


# Create dictionary of id and line
id2line = {}
for line in lines:
    _line = line.split('+++$+++')
    if len(_line) ==5:
        id2line[_line[0].strip()] = _line[4]

print(id2line['L537091'])

# Create list of conversation
conversation_list = []
for conversation in conversations:
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'","").replace(" ","").split(',')
    conversation_list.append(_conversation)

print(conversation_list[:3])


#separate questions and answers
questions = []
answers = []

for conversation in conversation_list:
    number_of_lines = len(conversation)
    for i in range(0,number_of_lines-1):
        # Get question
        question_text = id2line[conversation[i]]
        questions.append(question_text)

        # Get Answer
        answer_text = id2line[conversation[i+1]]
        answers.append(answer_text)

print(questions[:3])
print(answers[:3])

# doing the first cleaning pass of the text
def clean_text(text):
    text = text.lower()
    text = re.sub(r"i'm","i am", text)
    text = re.sub(r"he's","he is", text)
    text = re.sub(r"she's","she is", text)
    text = re.sub(r"that's","that is", text)
    text = re.sub(r"what's","what is", text)
    text = re.sub(r"where's","where is", text)
    text = re.sub(r"\'ll"," will", text)
    text = re.sub(r"\'ve"," have", text)
    text = re.sub(r"\'re"," are", text)
    text = re.sub(r"\'d"," would", text)
    text = re.sub(r"won't","will not", text)
    text = re.sub(r"can't","cannot", text)
    text = re.sub(r"[-()\"#/@;:<>{}+=~|.?,]","", text)
    return text




    

# cleaning the questions
clean_questions = []
for q in questions:
    clean_q = clean_text(q)
    clean_questions.append(clean_q)

print(clean_questions[:3])


# cleaning the answers
clean_answers = []
for a in answers:
    clean_a = clean_text(a)
    clean_answers.append(clean_a)

print(clean_answers[:3])


# Creating a dictionary that maps each word to its number of occurences
word2count = {}

for question in clean_questions:
    for word in question.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] +=1

for answer in clean_answers:
    for word in answer.split():
        if word not in word2count:
            word2count[word] = 1
        else:
            word2count[word] +=1