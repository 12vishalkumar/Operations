# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
S = set(map(int, input().split()))
n = int(input())
for i in range(n):
    op = input().split()
    if(op[0] == 'intersection_update'):
        S1 = set(map(int, input().split()))
        S.intersection_update(S1)
    if(op[0] == 'update'):
        S1 = set(map(int, input().split()))
        S.update(S1)
    if(op[0] == 'symmetric_difference_update'):
        S1 = set(map(int, input().split()))
        S.symmetric_difference_update(S1)
    if(op[0] == 'difference_update'):
        S1 = set(map(int, input().split()))
        S.difference_update(S1)
print(sum(S))
    