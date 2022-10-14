''' An OR Gate is a logic gate in boolean algebra which results to True(1) if any of the input is
   1, OR False(0) if  both the inputs are 0.
   Following is the truth table of an OR Gate:
   | Input 1 | Input 2 |  Output |
   |      0      |     0      |      0      |
   |      0      |     1      |      1      |
   |      1      |     0      |      1      |
   |      1      |     1      |      1      |
'''
'''Following is the code implementation of the OR Gate'''

def  OR_Gate(input_1,input_2):
    if input_1 == input_2 == 0:
        return 0
    else:
        return 1
if __name__== '__main__':
    print('Truth Table of OR Gate:')
    print('| Input 1 |',' Input 2 |',' Output |')
    print('|      0      |','     0      |     ',OR_Gate(0,0),'     |')
    print('|      0      |','     1      |     ',OR_Gate(0,1),'     |')
    print('|      1      |','     0      |     ',OR_Gate(1,0),'     |')
    print('|      1      |','     1      |     ',OR_Gate(1,1),'     |')

'''Code provided by Akshaj Vishwanathan'''  
