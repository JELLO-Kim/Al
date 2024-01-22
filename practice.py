def add_more(list):
    # list.append(50)
    list=list.pop()
    print("Inside Function:", list)

# Driver's code
mylist = [10,20,30,40]
 
# add_more(mylist)
print("Outside Function:", mylist)


string = "Geeks"
 
def test(string):
     
    string = "GeeksforGeeks"
    print("Inside Function:", string)
     
# Driver's code
# test(string)
print("Outside Function:", string)


def check():
    first_input, second_input = map(int, input().split(","))
    print(first_input)
    print(type(first_input))
    print(second_input)
    print(type(second_input))
check()