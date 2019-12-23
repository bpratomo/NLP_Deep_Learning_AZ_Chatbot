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
question = []
answer = []

for conversation in conversation_list:
    number_of_lines = len(conversation)
    for i in range(0,number_of_lines-1):
        # Get question
        question_text = id2line[conversation[i]]
        question.append(question_text)

        # Get Answer
        answer_text = id2line[conversation[i+1]]
        answer.append(answer_text)

print(question[:3])
print(answer[:3])


