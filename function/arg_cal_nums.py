def cal_num(*args):
    return sum(args), sum(args)/len(args)

Sum , Mean = cal_num(10,20,30)
print("3개의 인자 (10,20,30)")
print(f"합계 : {Sum}, 평균 : {Mean}")


Sum , Mean = cal_num(10,20,30,40,50)
print("5개의 인자 (10,20,30,40,50)")
print(f"합계 : {Sum}, 평균 : {Mean}")
