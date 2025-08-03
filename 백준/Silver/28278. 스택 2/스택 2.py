"""
1 X: 정수 X를 스택에 넣는다. (1 ≤ X ≤ 100,000)
2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 대신 출력한다.
3: 스택에 들어있는 정수의 개수를 출력한다.
4: 스택이 비어있으면 1, 아니면 0을 출력한다.
5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 대신 출력한다.
입력
첫째 줄에 명령의 수 N이 주어진다. (1 ≤ N ≤ 1,000,000)

둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.

출력을 요구하는 명령은 하나 이상 주어진다.

출력
출력을 요구하는 명령이 주어질 때마다 명령의 결과를 한 줄에 하나씩 출력한다."""
import sys

stack=[]
try: 
    N=int(sys.stdin.readline())
except ValueErros:
    N=0
for i in range(N):
    line = sys.stdin.readline().split()
    command = line[0]
    
    if command == '1':
        X=int(line[1])
        stack.append(X)
    elif command =='2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command =='3':
        print(len(stack))
    elif command == '4':
        if not stack:
            print(1)
        else:
            print(0)
    elif command == '5':
        if stack:
            print(stack[-1])
        else: 
            print(-1)
    
"""
def instruction(i):
    global stack
    if i == 1:
        stack.append(X)
    if i ==2:
        if stack:
            print(stack[:-1])
        else: 
            print("-1")
    if i ==3:
        print(len(stack))
    if i ==4:
        if not stack:
            print(0)
        else: 
            print(1)
    if i ==5:
        if not stack:
            print(-1)
        else : 
            print(stack[-1])
        
N= int(sys.stdin.readline())"""
"""
for num in range(1,N+1):
    i=int(sys.stdin.readline())
    instruction(i)
"""
