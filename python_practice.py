#Finds the maximum of '3' numbers
def max_num(*arg):
    max = 0
    for i in arg:
        if i > max:
            max = i
    print(max)
    return max

##########################################################################        

#Multiply all numbers in a list by a given number
def mult_list(factor, list=[]):
    
    for i in range(len(list)):
        list[i] *= factor
    print(list)
    return list

##########################################################################        

#Reverse a string
def rev_string(word):
    list = []
    length = len(word)

    for i in range(length):
        list.append(word[length-i-1])

    print("".join(list))

##########################################################################        

#Checks if an number fall within the interval of [lower_bound, upper_bound]
#---checks that lower_bound and upper_bound are in the correct order
def num_within(number, lower_bound, upper_bound):
    if lower_bound <= upper_bound:
        lower = lower_bound
        upper = upper_bound
    else: 
        lower = upper_bound
        upper = lower_bound

    if (lower <= number) and (number <= upper): 
        print(True)
        return(True)
    else:
        print(False)
        return(False)

##########################################################################        

#prints the first n rows of pascal's triangle
def pascal(integer):

    #Error handling for non-natural numbers
    if integer < 1 or not isinstance(integer, int):
        print("Not a valid number")
        return

    def find_value_at_coord(i, j):

        #Top of triangle
        if j == 1:
            return 1
        #Left side of triangle
        elif i==1:
            return find_value_at_coord(i,j-1)
        #Right side of triangle
        elif i==j:
            return find_value_at_coord(i-1,j-1)
        #Interior of triangle
        else:
            return find_value_at_coord(i-1,j-1) + find_value_at_coord(i, j-1)
    

    #Uses the function find_value_at_coord to generate the pascal triangle of given size 'integer'
    #This prints out each row, starting as the top, once said row is completed
    def generate_triangle():
        for row in range(1,integer+1):
            temp_string = ""
            for col in range(1, row+1):
                temp_string += str(find_value_at_coord(col,row))+" "
            print(temp_string)
       
    generate_triangle()
    
    return



#Tests
#max_num:
print("max_num tests")
print("----------------")
max_num(1,2,3)
max_num(3,2,1)
max_num(1,3,2)
print("----------------")


#mult_list:
print("mult_list tests")
print("----------------")
mult_list(2)
mult_list(2,[1,2,3,4])
mult_list(5,[1,2,3,4])
print("----------------")

#rev_string:
print("rev_string tests")
print("----------------")
rev_string("")
rev_string("word")
print("----------------")

#num_within:
print("num_within test")
print("----------------")
num_within(1,0,2)
num_within(1,2,0)
num_within(-1,2,4)
print("----------------")

#pascal:
print("pascal test")
print("----------------")
# pascal(0.23)
# pascal(1)
pascal(5)
print("----------------")