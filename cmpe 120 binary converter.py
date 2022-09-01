
#function accepts decimal as param returns binary

def to_binary( decimal):
    binary=""
    while True:
        #get remainder and accumulate result
        binary = str(decimal%2) + binary
        
        #set number we need to use for next iteration
        decimal = decimal//2

        #break loop when hits 0
        if(decimal <= 0):
            break
        
    return "0b"+binary

#definining variables for test cases
testcase1= 5
testcase2=8
testcase3 = 12
testcase4= 16

#printing test cases
print("testcase1 decimal 5= "+to_binary(testcase1))
print("testcase1 decimal 8= " +to_binary(testcase2))
print("testcase1 decimal 12= " +to_binary(testcase3))
print("testcase1 decimal 16= " +to_binary(testcase4))
