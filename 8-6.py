engkor_dict={}
eng=""
kor=""
a=0
while a==0:
    eng=input("영어 단어 : ")
    kor=input("한글 단어 : ")
    engkor_dict[eng]=kor
    if eng=="" and kor=="":
        del engkor_dict[kor]
        break
print(engkor_dict)
