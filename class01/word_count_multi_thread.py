#!/usr/bin/env python2
# FILE			: word_count_multi_thread.py
# AUTHOR		: K.Supasan
# CREATE ON		: 2019, August 19 (UTC+0)
# MAINTAINER	: K.Supasan

# README

# REFERENCE
# ref01 : https://docs.python.org/2/library/sys.html#sys.argv
# ref02 : https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
# ref03 : https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# ref04 : https://www.geeksforgeeks.org/python-extract-words-from-given-string/
# ref05 : https://www.programiz.com/python-programming/methods/list/count
# ref06 : https://www.programiz.com/python-programming/methods/list/index
# ref07 : https://docs.python.org/2/library/threading.html
# ref08 : https://docs.python.org/2/library/thread.html

from __future__ import print_function

import sys
import numpy as np
import re   # for regular expressions
import string
import thread    # For processing about locker and threading
import time


class WordCount:

    def __init__(self, file_name , num_thread = 1 ):
        self.error_type = 0         # Error type 0 is mean non error
        self.error_message = ""
        try:
            self.file = open(file_name, 'r')
            self.num_line = len( self.file.readlines() )
            self.close_file()
            self.file = open(file_name, 'r')
            self.num_thread = num_thread
        except:
            self.error_type = 1  # Mean can't open file
            self.error_message = "  <INIT FUNCTION> Can't open file name \"" + file_name + "\""
            raise ValueError

        self.locker = thread.allocate_lock()

    def count_word( self , line_list , num_thread ):
        print( "Number of thread indent 0 : " + str(num_thread) + " start thread" )
        temp_word = []
        temp_count = []
        for line in line_list :
            word_list = self.get_word_line( line )
            for word in word_list:
                try:
                    temp_index = temp_word.index(word.lower())
                    temp_count[ temp_index ] += 1
                except:
                    temp_word.append( word.lower() )
                    temp_count.append( 1 )

        with self.locker:
            print( "Thread number " + str(num_thread) + " now access critical section")
            for run in range( len( temp_word ) ) :
                try:
                    temp_index = self.word_list.index( temp_word[ run ].lower() )
                    self.count_list[ temp_index ] += temp_count[ run ]
                except:
                    self.word_list.append( temp_word[ run ].lower() )
                    self.count_list.append( temp_count[ run ] )
            self.thread_activate -= num_thread
            print( "Thread number " + str(num_thread) + " finish access critical section")
                    

    def start_count(self):

        self.word_list = []  # Use this variable to collect not same word
        self.count_list = []  # Use this to count not same word
 
        limit_count = self.num_line / self.num_thread 
        count = 0
        count_thread = 1
        thread_variable = []

        print( "WordCount detail of processing : " )
        print( "    Number of Thread       : " + str( self.num_thread ) )
        print( "    Number of line         : " + str( self.num_line ) )
        print( "    Number of line/Thread  : " + str( limit_count ) )
        self.thread_activate = 0


        raw_line = []
        for line in self.file:
            raw_line.append( line )
            count += 1
            if count == limit_count :      
                count = 0
                if count_thread < self.num_thread :
                    # start new thread
                    count_thread += 1
                    thread_variable.append( 
                        thread.start_new_thread(
                            self.count_word , ( raw_line , count_thread ) ) )
                    with self.locker :
                        self.thread_activate += count_thread
                    raw_line = []

        while self.thread_activate != 0 :
            time.sleep( 0.1 )

        self.count_word( raw_line , 0 ) 

        # After above loop you will get answer of count of word_list and count_list

    # Use below function to show you result
    def show_result(self):

        # Use numppy to sort list of array and sorting word
        array_word = np.array([self.word_list])
        array_count = np.array([self.count_list])
        array_result = np.concatenate((array_word.T, array_count.T), axis=1)
        array_result = array_result[array_result[:,
                                                 1].astype(int).argsort()][::-1]
        print(repr(array_result))

    def get_word_line(self, line_data):
        return re.sub('[' + string.punctuation+']', ' ', line_data).split()

    def close_file(self):
        self.file.close()

    def __del__(self):
        if self.error_type != 0:
            print("Error in Object WordCount number : " + str(self.error_type))
            print(self.error_message)


if __name__ == "__main__":

    num_arg = len(sys.argv)
    list_argv = sys.argv

    print("Number of argument is " + str(num_arg) + " : " + repr(list_argv))

    if(num_arg == 1):
        print("Please input you file name")
    else:
        word_count = WordCount(list_argv[1] , 4 )

        word_count.start_count( )

        word_count.show_result()

        word_count.close_file()
