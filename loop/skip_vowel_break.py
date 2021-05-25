st = 'Programming'
#자음이 나타나는 동안만 출력하는 기능
for ch in st:
    if ch in ['a','e','i','o','u']:
        continue
        #break
    print(ch)
print('The end')
