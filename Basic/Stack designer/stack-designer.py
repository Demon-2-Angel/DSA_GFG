#User function Template for python3

#_push function to insert elements of array to stack
def _push(arr):
    #return a stack with all elements of arr inserted in it
    stack = []
    for i in range(len(arr)):
        stack.append(arr[i])
    return stack    

#_pop function to print elements of the stack remove as well
def _pop(stack):
    #print top and pop for each element until it becomes empty
    while len(stack) > 0:
        
        print(stack.pop(), end=" ")



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr=[int(i) for i in input().split()]
        stack = _push(arr)
        _pop(stack)
        print()

# } Driver Code Ends