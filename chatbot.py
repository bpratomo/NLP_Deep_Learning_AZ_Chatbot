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
    _conversation = conversation.split(' +++$+++ ')[-1][1:-1].replace("'","").split(',')
    conversation_list.append(_conversation)

print(conversation_list[:3])


#separate questions and answers
