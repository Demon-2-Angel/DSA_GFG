
class Solution:
    def oddEven(self, s : str) -> str:
        # code here
        ans =0 
        freq= [0]*26
        for char in s:
            freq[ord(char) - ord("a")]+=1
        for i in range(26):
            if not i&1:
                if freq[i]&1:
                    ans+=1
            else:
                if freq[i] and (not freq[i]&1):
                    ans +=1
        return "ODD" if ans&1 else "EVEN"



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s = (input())

        obj = Solution()
        res = obj.oddEven(s)

        print(res)

# } Driver Code Ends