'''sudoku = [[3, 1, 6, 5, 7, 8, 4, 9, 2 ], 
        [5, 2, 9, 1, 3, 4, 7, 6, 8 ], 
        [ 4, 8, 7, 6, 2, 9, 5, 3, 1 ], 
        [ 2, 6, 3, 0, 1, 5, 9, 8, 7 ], 
        [ 9, 7, 4, 8, 6, 0, 1, 2, 5 ], 
        [ 8, 5, 1, 7, 9, 2, 6, 4, 3 ], 
        [ 1, 3, 8, 0, 4, 7, 2, 0, 6 ], 
        [ 6, 9, 2, 3, 5, 1, 8, 7, 4 ], 
        [ 7, 4, 5, 0, 8, 6, 3, 1, 0 ] ]

#check whether it will be legal to
#assign num to the given row, col
def is_Safe(sudoku):
    #Hashmap for row column and boxes
    for col in range(len(sudoku)):
        for row in sudoku:
            #mark the element in row column and box
            if row[col] == 
            

    #for col in range(len(sudoku)):
        #for row in sudoku:
            #row[col]

#Find the zeros's
for col in range(len(sudoku)):
    for row in sudoku:
        if row[col] == 0:
            row[col] = 'x'


#function to print grid
def print_grid():
    for row in sudoku:
        print(row)

print_grid()
is_Safe(sudoku)'''

#--------------working out a hash fucntion--------
sudoku = [[3, 1, 6, 5, 7, 8, 4, 9, 2 ], 
        [5, 2, 9, 1, 3, 4, 7, 6, 8 ], 
        [ 4, 8, 7, 6, 2, 9, 5, 3, 1 ], 
        [ 2, 6, 3, 0, 1, 5, 9, 8, 7 ], 
        [ 9, 7, 4, 8, 6, 0, 1, 2, 5 ], 
        [ 8, 5, 1, 7, 9, 2, 6, 4, 3 ], 
        [ 1, 3, 8, 0, 4, 7, 2, 0, 6 ], 
        [ 6, 9, 2, 3, 5, 1, 8, 7, 4 ], 
        [ 7, 4, 5, 0, 8, 6, 3, 1, 0 ] ]

#first_row = sudoku[0]
two_similar_elements = False

#for col in range(len(sudoku)):
def Test_Horizontal():
    for row in sudoku:
        if len(set(row)) < (len(row)):
            print(row)
            print(set(row))
            two_similar_elements = True
            print(two_similar_elements)
            
        else:
            two_similar_elements = False


'''if len(set(sudoku[col])) < len(row[col]):
two_similar_elements = True
print(row[col])
print(two_similar_elements)
else:
two_similar_elements = False'''

#print(first_row)
Test_Horizontal()
print(two_similar_elements)

