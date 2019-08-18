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

from __future__ import print_function

import sys
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

    def get_word_line( self ):
        data_line = self.file.readline()

        return re.sub( '[' + string.punctuation+']',' ', data_line ).split()


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

        
