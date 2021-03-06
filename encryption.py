problem_notes ='''
This problem deals with a custom encryption scheme that works as follows. 

Given a string like "how are you?" and m * n grid. The characters of the string are filled 
into the grid row wise top to bottom. So for 3 * 5 you get

h o w _ a
r e _ y o
u ? * * *

In the above example _ is shown visually where there is a space character. Unfilled cells are filled with *'s

The encrypted string is found by starting at a top left corner and going clockwise in 
a decreasing spiral till all the cells are covered. So if corner is top left you get "how_ao***?ure_y"

Notes:
1. returns the encrypted string as specified above.

'''
                    
def encrypt(text,r,c):     
    row=r                                                        
    column=c                                 
    k=0                                                      
    main_list=[]
    for i in range(0,row):
        li=[]
        if k + column > len(text):                           '''checking wheather (k + column) exist if not fill with '*' '''
            for i in range(0,column):
                li.append('*')
            for j in range(0,len(text)-k):
                li[j]=text[k] 
                k+=1                   
        else:
            for j in range(k , k + column):                   '''if text[j] is space fill with '_' '''
                if text[j]==' ':
                    li.append('_')
                    k+=1
                else:    
                    li.append(text[j])
                    k+=1
        main_list.append(li)  

    for i in range(0,len(main_list)):                          ''' printing the matrix form'''
        print(* main_list[i]) 

    Top_left(row,column,main_list)   

def Top_left(row,column,main_list):
    last_column=column
    last_row=row
    final_string=''
    k=0
    l=0
    while (k < last_row) and (l < last_column):
        for i in range(l,last_column):
             final_string+=main_list[k][i]
        k+=1     

        for j in range(k,last_row):
            final_string+=main_list[j][last_column-1]
        last_column-=1

        if k < last_row:
            for i in range(last_column-1,l-1,-1):
                final_string+=main_list[last_row-1][i]
            last_row-=1 

        if l < last_column:
            for j in range(last_row-1,k-1,-1):
                final_string+=main_list[j][l]
            l+=1  
    print(final_string)         

def test_encrypt():
    encrypt("how are you?",3,5)

test_encrypt()
