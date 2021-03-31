# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 00:07:25 2021

@author: Raiyaan Abdullah
"""

from word_generate import train_data_generate 
import pandas as pd
import csv
import numpy as np
from sklearn.utils import shuffle

medicine_list=[]
companies=["square.csv","beximco.csv"]
for company in companies:
    with open(company) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            medicine_list.append(row[0].lower())

letter_list = [' ', 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','w','x','y','z','1','2','3','4','5','6','7','8','9','0','+','(',')',',','-','[',']','%','/']

letter_to_index = {x: i for i, x in enumerate(letter_list)}
medicine_to_index = {x: i for i, x in enumerate(medicine_list)}
   
#turn characters to numbers
X=np.zeros((130000, 80, len(letter_list)))   
Y=np.zeros((130000, len(letter_list)))        

for i, sentence in enumerate(sequences):
    for t, word in enumerate(sentence):
        X[i, t, vocab[word]] = 1
    y[i, vocab[next_words[i]]] = 1

'''
def bidirectional_lstm_model(seq_length, vocab_size):
    print('Build LSTM model.')
    model = Sequential()
    model.add(Bidirectional(LSTM(rnn_size, activation="relu"),input_shape=(seq_length, vocab_size)))
    model.add(Dropout(0.6))
    model.add(Dense(vocab_size))
    model.add(Activation('softmax'))
    
    optimizer = Adam(lr=learning_rate)
    callbacks=[EarlyStopping(patience=2, monitor='val_loss')]
    model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=[categorical_accuracy])
    print("model built!")
    return model
'''
