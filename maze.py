#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 01:08:20 2017

@author: jim
"""


import random

#===create map===
#@param path,depth
#return result_map
def create_map(path,depth):
    result_map = []
    row_list=[]
    print "create main map:"
    
    for row in range(0, int(depth*2+1)):
         for colunm in range(0, int(path*2-1)):
             if(colunm%2==0):
                 number=1
             else:
                 if(row%2!=0):
                     number=random.randint(0,1)
                     #避免一直線
                     if(colunm>2):
                         if(row_list[colunm-2]==number):
                             number=0
                 else:
                     number=0
                     
             row_list.append(number)
         result_map.append(row_list)
         print(row_list)
         row_list=[]
         
    return result_map

#===draw map===
#@param main_map,edge_size
#return 
def draw_map(main_map,edge_size):
    draw_list=[]
    
    draw_list=resize_edge(main_map,edge_size)
    print "draw main map:"

    for row_index, row_val in enumerate(draw_list):
        for colunm_index, colunm_val in enumerate(row_val):
            if(colunm_val==0):
                print " ",
            elif(colunm_val==1):
                print "*",
            else:
                print "O",
        print ""

#===resize_edge===
#@param main_map,edge_size
#return result_list
def resize_edge(main_map,edge_size):
    result_list=[]
    colunm_resize_temp=[]
    print "resize main map:"

    for depth_index, depth_val in enumerate(main_map):

        #colunm resize
        for path_index, path_val in enumerate(depth_val):
            number=path_val
            if(path_index%2!=0):
                for colunm_size in range(0,edge_size):
                    colunm_resize_temp.append(number)
                    
            else:
                colunm_resize_temp.append(number)   
                
        #row resize
        if(depth_index%2==0):
            for row_size in range(0,edge_size):
               result_list.append(colunm_resize_temp) 
               print(colunm_resize_temp)
        else:
            result_list.append(colunm_resize_temp)
            print(colunm_resize_temp)
    
        colunm_resize_temp=[]

    return result_list
    

#check answer
def answer_check(main_map,answer,path,edge_size):
    main_map_temp = [x[:] for x in main_map]
    
    while(True):
        try:
            entrance = raw_input("Enter your choice of entrance:"+"(0~"+str(int(path)-1)+"):")
            if(entrance.isdigit()):
                if(0 <= int(entrance) <= int(path)-1):
                    break
                else:
                    print "entrance input error!"
            else:
                print "entrance input error!"
        except ValueError:
            print "Format of entrance is error!"
         
    #position of pointer
    pointer=int(entrance)*2
    #check main_map answer     
    for depth_index, depth_val in enumerate(main_map_temp):
        depth_val[pointer]=2
        Turn=True
        
        while(Turn):
            #position at 0 path only Turn right
            if(pointer==0):
                if(depth_val[pointer+1]==1):
                    depth_val[pointer+1]=2
                    pointer+=1  
                else:
                   Turn=False 
            #position at last path only Left right
            elif(pointer==len(depth_val)-1):
                if(depth_val[pointer-1]==1):
                    depth_val[pointer-1]=2
                    pointer-=1
                else:
                   Turn=False 
            else:
                if(depth_val[pointer+1]==1):
                    depth_val[pointer+1]=2
                    pointer+=1                               
                elif(depth_val[pointer-1]==1):
                    depth_val[pointer-1]=2
                    pointer-=1    
                else:
                    Turn=False

    #draw map               
    draw_map(main_map_temp,edge_size)
    #print exit position
    exit_path=pointer/2
    print "Your exit path is :",exit_path
    
    #ask try again
    if(answer!=exit_path):
        while(True):
            try:
                response = raw_input("Try again? (1:yes,2:no):")
                if(response.isdigit()):
                    if(int(response)==1):
                        answer_check(main_map,answer,path,edge_size)
                        break
                    else:
                        break
                else:
                    print "answer input error!"
            except ValueError:
                print "Format of answer is error!"
    else:
        print "Bingo!!! The answer is",answer


def main():
    main_map = []
    
    while(True):
        try:
            path = raw_input("Enter your size of path(more than 1):")
            if(path.isdigit()):
                if(int(path)>1):
                    break
                else:
                    print "Path input error!"
            else:
                print "Path input error!"
        except ValueError:
            print "Format of Path is error!"

    while(True):
        try:
            depth = raw_input("Enter your depth:")
            if(depth.isdigit()):
                if(int(depth)>0):
                    break
                else:
                    print "Depth input error!"
            else:
                print "Depth input error!"
        except ValueError:
            print "Format of Depth is error!"
            
    while(True):
        try:
            edge_size = raw_input("Enter your size of edge:")
            if(edge_size.isdigit()):
                if(int(edge_size)>0):
                    break
                else:
                    print "edge size input error!"
            else:
                print "edge size input error!"
        except ValueError:
            print "Format of edge size is error!"
    
    #create answer
    answer=random.randint(0,int(path)-1)
    print "Answer is: ",answer 
    
    #create_map        
    main_map = create_map(int(path),int(depth))
    draw_map(main_map,int(edge_size))
    
    #check answer
    answer_check(main_map,answer,path,int(edge_size))
    
main()

