#!/usr/bin/env python
#coding=utf-8

#python3.6.5
import sys

res=[]
for line in sys.stdin: #sys.stdin.readline() get all standard input including '\n',input() get all standard input without '\n'
    if line.strip()=='':  #str.strip([chars]) return a new string generated by removing the characters specified at the beginning and end of the string.
        break
    res.extend(line.split()) #str.split(str="",num=string.count(str)) return the list of split strings.
    #list.extend(seq) add the element sequence to a known list

#print(set(res))
print(len(set(res))) 
