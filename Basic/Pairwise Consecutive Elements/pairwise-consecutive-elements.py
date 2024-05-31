#User function Template for python3

# Function to check if elements are 
# pairwise consecutive in stack 
def pairWiseConsecutive(l):
    #add code here
    #first lets check if the stack is even or odd numbered:
    if len(l) % 2 == 0:
        #even
        #Now there will be two cases: the case where len is 2 and case where len != 2:
        #case1: len == 2:
        if len(l) == 2:
            if abs(l[1] - l[0]) != 1:
                return False
        else:
            for i in range(len(l)-2):
                if abs(l[i+1] - l[i]) != 1:
                    return False
                else:
                    if l[i+1] - l[i] == 1:
                        if l[i+2] - l[i+1] != 1:
                            return False
                    if l[i+1] - l[i] == -1:
                        if l[i+2] - l[i+1] != -1:
                            return False
    else:
        #odd
        #first we need to pop the last element from the stack which is head for it actually.
        l.pop()
        #if len == 2:
        if len(l) == 2:
            if abs(l[1] - l[0]) != 1:
                return False
        else:
            for i in range(len(l)-2):
                if abs(l[i+1] - l[i]) != 1:
                    return False
                else:
                    if l[i+1] - l[i] == 1:
                        if l[i+2] - l[i+1] != 1:
                            return False
                    if l[i+1] - l[i] == -1:
                        if l[i+2] - l[i+1] != -1:
                            return False
    return True
            
                            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n=int(input())
        l=list(map(int,input().split()))
        if(pairWiseConsecutive(l)==True):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends