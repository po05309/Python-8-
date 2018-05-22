items={"라면":650,"우유":1100,"콜라":1200,"캔커피":500,"과자":700}
a=0
sum=0
while a==0:
    it=input("제품명 : ")
    if it=="":
        break
    if it!="" and it in items:
        sum+=items.get(it)
        print("[",it,":",items.get(it),"] >", sum)
    if not it in items:
        print(it,"는 미등록 제품입니다.")
print("총 금액 :", sum)
