#!/usr/bin/env python2
# FILE			: word_count.py
# AUTHOR		: K.Supasan
# CREATE ON		: 2019, August 18 (UTC+0)
# MAINTAINER	: K.Supasan

# README

# REFERENCE
# ref01 : https://docs.python.org/2/library/sys.html#sys.argv
# ref02 : https://docs.python.org/2/tutorial/inputoutput.html#reading-and-writing-files
# ref03 : https://www.tutorialspoint.com/python/python_command_line_arguments.htm
# ref04 : https://www.geeksforgeeks.org/python-extract-words-from-given-string/
# ref05 : https://www.programiz.com/python-programming/methods/list/count
# ref06 : https://www.programiz.com/python-programming/methods/list/index

from __future__ import print_function

import sys
import numpy as np
import re   # for regular expressions
import string

class WordCount:

    def __init__( self , file_name ):
        self.error_type = 0         # Error type 0 is mean non error
        self.error_message = ""
        try:
            self.file = open( file_name , 'r' )
        except:
            self.error_type = 1 # Mean can't open file
            self.error_message = "  <INIT FUNCTION> Can't open file name \"" + file_name + "\""
            raise ValueError

    def start_count( self ):

        self.word_list = [] # Use this variable to collect not same word
        self.count_list = [] # Use this to count not same word        

        for line in self.file : # This will read line for you
            # temp_list is array of word
            temp_list = self.get_word_line( line )
            for word in temp_list :
                try:
                    temp_index = self.word_list.index( word.lower() )
                    self.count_list[ temp_index ] += 1
                except:
                    self.word_list.append( word.lower() )
                    self.count_list.append( 1 )

        # After above loop you will get answer of count of word_list and count_list

    # Use below function to show you result
    def show_result( self ):
        print( "Result is : " )

#        for run in range( len( self.word_list ) ):
#            print( "  {:20s}  : {:d}".format( self.word_list[run] , self.count_list[ run ] ) )

        array_word = np.array( [self.word_list] )
        array_count = np.array( [self.count_list] )
        array_result = np.concatenate( ( array_word.T , array_count.T) , axis=1 )
        print( repr( array_result ) ) 

    def get_word_line( self , line_data ):
        return re.sub( '[' + string.punctuation+']',' ', line_data ).split()

    def close_file( self ):
        self.file.close()
            
    def __del__( self ):
        if self.error_type != 0 :
            print( "Error in Object WordCount number : " + str( self.error_type ) )
            print( self.error_message )
        

if __name__=="__main__":

    num_arg = len(sys.argv)
    list_argv = sys.argv

    print( "Number of argument is " + str( num_arg) + " : " + repr( list_argv ) )

    if( num_arg == 1 ):
        print( "Please input you file name")
    else:
        word_count = WordCount( list_argv[1] )

        word_count.start_count()

        word_count.show_result()

        word_count.close_file()
