Because it requires combinations, we will use backtracking in it. We will miantin a stack that will add ( if no. of open brackets are less than n and it will add ) if no. of close brackets are less than open brackets. Base case is if no. of open brackets is equal to no. of closed brackets, which is equal to n. 

General template of backtracking:

def backtrack(candidate):
    if find_solution(candidate):
        output(candidate)
        return
    
    # iterate all possible candidates.
    for next_candidate in list_of_candidates:
        if is_valid(next_candidate):
            # try this partial candidate solution
            place(next_candidate)
            # given the candidate, explore further.
            backtrack(next_candidate)
            # backtrack
            remove(next_candidate)
            
            
            
To recognize when backtracking could be used and when to involve a stack, look for the following characteristics in the problem:
1)Combinations/Permutations: Problems that involve generating all possible combinations or permutations of a certain structure (e.g., parentheses, subsets, permutations).
2)Choices at Each Step: Problems where you have multiple choices at each step and need to explore all possible combinations of those choices.
3)Valid Solutions: Situations where you need to generate valid solutions that satisfy certain conditions or constraints.
4)Decision Tree Structure: Problems that can be visualized as a decision tree, where each branch represents a choice leading to more choices.
5)Backtracking with State: Problems where backtracking involves maintaining a certain state or using auxiliary data structures (like a stack) to keep track of choices and current progress
​
