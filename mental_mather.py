#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 13:37:56 2019

@author: glenhigh
"""


import os
os.chdir('/Users/glenhigh/Scrapping/MentalMaths')

import time
from selenium import webdriver
from bs4 import BeautifulSoup
from sympy.parsing.sympy_parser import parse_expr
from sympy.solvers import solve
from sympy import Symbol
from selenium.webdriver.common.by import By

#List to store name of the product
#List to store price of the product
IN_GAME=False

x=Symbol('x')
string="2*x+1=2"
left, right = string.split('=')
string = left + "-(" + right + ")";
print(parse_expr(string))


if IN_GAME==False:
    driver = webdriver.Chrome(executable_path='/Users/glenhigh/Scrapping/MentalMaths/chromedriver')
    #driver = webdriver.PhantomJS(executable_path='/Users/glenhigh/Scrapping/GoogleTrends/phantomjs') #Same without window opening
    #print("Accessing...")
    driver.get("https://rankyourbrain.com/mental-math/mental-math-test-expert")
    time.sleep(20)

# =============================================================================
#     Login time
# =============================================================================

    driver.get("https://rankyourbrain.com/mental-math/mental-math-test-expert/play")
    time.sleep(2)#Load all JS parallel stuff
    #print("On page...")
    content = driver.page_source
    soup = BeautifulSoup(content,features="lxml")
    #TEST WITH LOCAL HTML INSTEAD

    tictac=soup.find('div', attrs={'class':'clock'}).string
    #print(tictac)
    if(soup.find('span', attrs={'id':'beforeAnswer'}).string!=None):
        left =soup.find('span', attrs={'id':'beforeAnswer'}).string
    else:
        left=""
    if(soup.find('span', attrs={'id':'afterAnswer'}).string!=None):
        right =soup.find('span', attrs={'id':'afterAnswer'}).string
    else:
        right=""
    while(1):
        content = driver.page_source
        soup = BeautifulSoup(content,features="lxml")
        """
        if(soup.find('span', attrs={'id':'counterScore'}).string=="830"):
            break
        """
        while(left=="" and right ==""):
            content = driver.page_source
            soup = BeautifulSoup(content,features="lxml")
            if(soup.find('span', attrs={'id':'beforeAnswer'}).string!=None):
                left =soup.find('span', attrs={'id':'beforeAnswer'}).string
            else:
                left=""
            if(soup.find('span', attrs={'id':'afterAnswer'}).string!=None):
                right =soup.find('span', attrs={'id':'afterAnswer'}).string
            else:
                right=""

        if(soup.find('span', attrs={'id':'beforeAnswer'}).string!=left or soup.find('span', attrs={'id':'afterAnswer'}).string!=right):
            tictac=soup.find('div', attrs={'class':'clock'}).string
            if(soup.find('span', attrs={'id':'beforeAnswer'}).string!=None):
                left =soup.find('span', attrs={'id':'beforeAnswer'}).string
            else:
                left=""
            if(soup.find('span', attrs={'id':'afterAnswer'}).string!=None):
                right =soup.find('span', attrs={'id':'afterAnswer'}).string
            else:
                right=""
            eq= str(left)+" x "+str(right)
            if(eq[1]!='x'):
                eq=' '+eq
            if(eq[len(eq)-2]!='x'):
                eq=eq+' '
            eq=eq.replace('  ',' ')
            while(' ' in eq):
                eq=eq.replace(' ','(',1)
                eq=eq.replace(' ',')',1)


            #print("EQ : "+eq)
            left_eq, right_eq = eq.split('=')
            solvable_eq = left_eq + "-(" + right_eq + ")";
            #print("New time : "+str(tictac))
            #print("New EQ : "+solvable_eq)
            solution=solve(parse_expr(solvable_eq),x)
            #print(solution[0])

            sbox = driver.find_element(By.ID,"answer")
            sbox.clear()
            sbox.send_keys(str(solution[0]))






print("Closing driver...")
#driver.close
print("Driver closed")
