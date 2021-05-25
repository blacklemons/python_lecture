import random

selected = None
winplan = random.choice(['가위','바위','보'])
print('winplan = ',winplan)
while selected != winplan:
    selected = input('가위, 바위, 보 중에서 선택하세요 : ')
    
    if selected not in ['가위','바위', '보']:
        print('잘못된 값을 입력하였습니다.\n')
    elif selected == winplan:
        break
    else:
        print('패배하였습니다.\n')
    
print('승리하셨습니다.')