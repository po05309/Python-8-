engkor_dict={}
eng=""
kor=""
a=0
while a==0:
    eng=input("영어 단어 : ")
    if len(engkor_dict)==0 and eng!="":
        print("사전이 비어 있습니다.")
        print("단어를 추가합니다.")
        kor=input("한글 단어 : ")
        engkor_dict[eng]=kor
    if eng in engkor_dict:
        print(engkor_dict.get(eng))
    if not eng in engkor_dict and eng!="":
        print(eng,"단어가 등록되어 있지 않습니다.")
        print("단어를 추가합니다.")
        kor=input("한글 단어 : ")
        engkor_dict[eng]=kor
    if eng=="":
        break
print(engkor_dict)
