import sys

# 명령의 개수 N을 입력받습니다.
N = int(sys.stdin.readline())

# 스택 역할을 할 빈 리스트를 만듭니다.
stack = []

for _ in range(N):
    command = sys.stdin.readline().split()
    
    # 'push' 명령 처리
    if command[0] == 'push':
        stack.append(int(command[1]))
    
    # 'pop' 명령 처리
    elif command[0] == 'pop':
        if stack:
            print(stack.pop())
        else:
            print(-1)
            
    # 'size' 명령 처리
    elif command[0] == 'size':
        print(len(stack))
        
    # 'empty' 명령 처리
    elif command[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
            
    # 'top' 명령 처리
    elif command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)