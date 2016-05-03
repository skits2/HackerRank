"""How many different ways can you make change for an amount, given a list of coins? In this problem, your code will need to efficiently compute the answer.

Task

Write a program that, given

    The amount NN to make change for and the number of types MM of infinitely available coins
    A list of MM coins - C={C1,C2,C3,..,CM}C={C1,C2,C3,..,CM}

Prints out how many different ways you can make change from the coins to STDOUT.

The problem can be formally stated:

Given a value NN, if we want to make change for NN cents, and we have infinite supply of each of C={C1,C2,,CM}C={C1,C2,,CM} valued coins, how many ways can we make the change

Constraints

    1=Ci=501=Ci=50
    1=N=2501=N=250
    1=M=501=M=50
    The list of coins will contain distinct integers.

Solving the overlapping subproblems using dynamic programming

You can solve this problem recursively, but not all the tests will pass unless you optimise your solution to eliminate the overlapping subproblems using a dynamic programming solution

Or more specifically;

    If you can think of a way to store the checked solutions, then this store can be used to avoid checking the same solution again and again.

Input Format

First line will contain 2 integer N and M respectively.
Second line contain M integer that represent list of distinct coins that are available in infinite amount.

Output Format

One integer which is the number of ways in which we can get a sum of N from the given infinite supply of M types of coins.

Sample Input

4 3
1 2 3 

Sample Output

4

Sample Input #02

10 4
2 5 3 6

Sample Output #02

5

Explanation

    Example 1: For N=4N=4 and C={1,2,3}C={1,2,3} there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}{1,1,1,1},{1,1,2},{2,2},{1,3}

    Example 2: For N=10N=10 and C={2,5,3,6}C={2,5,3,6} there are five solutions: {2,2,2,2,2},{2,2,3,3},{2,2,6},{2,3,5},{5,5}{2,2,2,2,2},{2,2,3,3},{2,2,6},{2,3,5},{5,5}.
"""





# get the data for each potential trading set
def get_data():
    amount, num_coins = [int(data) for data in raw_input().split()]
    coin_list = [int(coin) for coin in raw_input().split()]

    return amount, coin_list
    
    
memoization = {}
# recursively start finding the number of possiblities to get to smaller change amounts
def possibilities(amount,coin_list,used):
   
   memo_string = str(amount) +"coins "+ " ".join([str(coin) for coin in coin_list])
   if (memo_string in memoization):
       return memoization[memo_string]
   
   # we have successfully gotten to 0, return 1
   if (amount == 0):
       return 1

   # this was not a successful change
   if (amount < 0 or len(coin_list) == 0):
       return 0

   coin_list_smaller = coin_list[:]
   coin_list_smaller.pop(0)
   used2 = used[:]
   used2.append(coin_list[0])

   # there are 2 possibilities for a given amount, 
   #  - subtract the largest coin, don't pop it from the list, and find the lower amount
   #  - don't subtract the larget coin, pop it from the list, and find the lower amount
   number_possible = possibilities(amount-coin_list[0],coin_list,used2) + \
                     possibilities(amount,coin_list_smaller,used)

   memoization[memo_string] = number_possible

   return number_possible


    


# get the input data    
amount, coin_list = get_data()

# sort the coin list from largest to smallest
coin_list.sort(reverse=True)

if (amount == 0 or len(coin_list) == 0):
    print 0
else:
    used=[]
    number_possible = possibilities(amount,coin_list,used)
    print number_possible



