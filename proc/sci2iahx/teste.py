#! /usr/bin/python

# To change this template, choose Tools | Templates
# and open the template in the editor.

__author__="jamil"
__date__ ="$Jul 4, 2011 3:40:44 PM$"

import configparser

if __name__ == "__main__":
    

    #Get config file
    config = configparser.ConfigParser()
    config.read('config/config.ini')


    print('jamil'[0].upper())

    
    
    