#User function Template for python3

def getMinMax( a, n):
    mini = maxi = a[0]
    for i in a:
        if i<mini:
            mini=i
        if i>maxi:
            maxi = i
    return mini, maxi
        
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        
        product = getMinMax(a, n)
        print(product[0], end=" ")
        print(product[1])

        T -= 1


if __name__ == "__main__":
    main()



# } Driver Code Ends