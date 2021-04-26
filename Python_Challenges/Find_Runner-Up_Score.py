"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score.
You are given  scores. Store them in a list and find the score of the runner-up.

Input Format
The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Constraints
2<=n<=10
-100<=A[i]<=100

Output Format
Print the runner-up score.

Sample Input 0
5
2 3 6 6 5

Sample Output 0
5

Explanation 0
Given list is [2,3,6,6,5]. The maximum score is 6, second maximum is 5. Hence, we print 5 as the runner-up score.
"""

if __name__ == '__main__':
    python_students = []
    score_list = []
    sl_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name,score])
        score_list.append(score)
    second_last = list(sorted(set(score_list)))[1]
    for i in range(len(python_students)):
        if python_students[i][1] == second_last:
            sl_list.append(python_students[i][0])
    for i in range(len(sl_list)):
        print(sorted(sl_list)[i])