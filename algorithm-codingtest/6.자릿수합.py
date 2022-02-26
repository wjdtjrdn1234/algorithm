# import sys
# sys.stdin=open("input.txt","rt")


#정통적인 아닌 문자열로 자릿수 구하기
def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum

n = int(input())
arr = list(map(int,input().split()))
max = -100000
for x in arr:
    total = digit_sum(x)
    if total>max:    #total값이 같다고 가정하에 똑같은경우는 if처리를 안했기떄문에 고려할필요가없음
        max=total
        res=x
print(res)



# 각자릿수합 최대값문제 (문자열,while 둘중하나로 해결)
# 답이여러개인경우 입력이 먼저온값이 정답이면 , if문에서 해결이 가능

# 아얘 배열로 담지않고 if문으로 해결,정통적은 자릿수 해결문제
# def digit_sum(x):
#     sum=0
#     while x>0:
#         sum+=x%10 #x를 10으로 나눈 나머지
#         x=x//10 #x는 10으로 나눈 몫      (몫+나머지) = 나눈값 / ( 나눈값은 /)
#     return sum
#
# n = int(input())
# arr = list(map(int,input().split()))
# max = -100000
# for x in arr:
#     total = digit_sum(x)
#     if total>max:    #total값이 같다고 가정하에 똑같은경우는 if처리를 안했기떄문에 고려할필요가없음
#         max=total
#         res=x
# print(res)


# 내코드 :각 자릿수합 비교 -> 문자열로 받아서 각자리를 int로 배열로 치환한후 합 반환
# def digit_sum(x):
#     N = [int(i) for i in x ]
#     return sum(N)
# n = int(input())
# list = list(input().split())
# max = 0
# answer = []
# for i in range(n):
#     result = digit_sum(list[i])
#     if max<result:           # 새로 max값이나오면 결과배열 비우고 추가하고, 똑같다면 추가하고
#         answer = []
#         max = result
#         answer.append(list[i])
#     elif max==result:
#         answer.append(list[i])
#
# print(answer[0])


# //변수: 특수문자x,키워드사용x,대소문자구분,
# a=1,b=2,c=3
# (a, b, c) //1 2 3
# //교환
# a,b=1,2
# a,b=b,a
# print("number:",a,b,c)//number:123
# print("number:",a,b,,sep=',')//number:1,2,3
#
#
# //입력
# a = input()
# print(a)
#
# a,b = input().split()// 문자열2개 입력
# print(type(a+b))
#
# a,b = map(int, input().split())//정수형2개 입력
# print(type(a+b))
# print(a//b) //5를 2로 나눈 몫
# print(a%b) //a를 b로 나눈 나머지
# print(a/b) //a를 b로 나눈값 (나눈값 = 몫+나머지)
# print(a**b) //a를 b번 거듭제곱 2**3 = 8
#
# // 반복문
# for i in range(1,10,):
#     print(i) //1~9
# for i in range(10,0,-2):
#     print(i) //10 8 6 4 2
#
# while i<=10:
#     print(i,end=' ') //줄바꿈안하고 띄어쓰기
#     if i==10:
#         break,continue
#     i+=1
#
# print('i:',i,sep:'',end=' ')//i:0 부분이 딱붙어서나옴 -> i:0 i:1 i:2 // 이런식
#
# for i in range(5):
#     for j in range(5-i):
#         print("*",end=' ') //별 5->4->3->2->1
#     print()
#
# //문자열,내장함수
# msg = 'ab aCc'
# print(msg.upper())//대문자
# print(msg.lower())//소문자 -> msg자체가 변하진x
# print(msg.find('a'))//0
# print(msg.count('a'))//2
# print(msg[:2]) //2번인덱스 전까지 출력 ->ab //2번인덱스: 빈칸
# print(msg[3:5]) //aC
# print(len(msg)) //6
# for i in msg:
#     print(i)
# for i in range(len(msg)):
#     print(msg[i])
# for i in msg:
#     if i.isupper():  //islower()
#         print(i)
# for i in msg://공백없이 쭉붙여쓸때
#     if i.isalpha(): //알파벳일떄
#         print(i,end='')
# ord(x) //ord: 아스키코드 A:65 ~ Z:90 // a:97 ~ z:122
# print(chr(65))//A
#
# //리스트,내장함수
# import random as r
# a=[] , b=list() //둘이 똑같음
# a=[1,2,3] , b=list(range(1,4))
# print(a+b) //리스트끼리 합침 , 순서유지
# a.append(4) //3뒤에 4추가
# a.insert(3,10)//3인덱스에 7추가
# a.pop() //맨뒤에 제거
# a.pop(3)//3인덱스 제거
# a.remove(4)//4라는 값 제거
# a.index(3) //3의 인덱스값 출력 = 2
# sum(a)
# max(a)
# min(a)
# min(2,3,4,11)
# r.shuffle(a) // a 순서가 뒤죽박죽
# a.sort() //오름차순정렬
# a.sort(reverse=True)//내림차순정렬
# a.clear() //리스트값 없어짐 -> 빈리스트
#
# a=[1,2,3,4,5]
# print(a[:3]) //[1,2,3]
# print(a[1,4]) //[2,3,4]
#
# //enumerate : 인덱스 번호까지 출력하고싶을떄:
# for x in enumerate(a):
#     print(x) // 튜플형태로 출력: (0,1) (1,2) (2,3)  ~ (index,value)

# for x in enumerate(a):
#     print(x[0],x[1]) // 0 1 // 1 2 //

# for index,value in enumerate(a):
#     print(index,value) // 0 1 // 1 2 //
#
# b = (1,2,3,4,5) //튜플
# print(b[0]) //1
# b[0]=7 //튜플값 변경x
#
# //all,any
# if all(5>x for x in a): //조건이 전부만족하면 true를 리턴,하나라도 거짓이면 false
#     print("yes")
# else:
#     print("no")
#
# if any(5>x for x in a): //조건이 한번이라도 만족하면 true를 리턴, 전부거짓이면 false
#     print("yes")
# else:
#     print("no")
#
# //2차원 리스트
#
# a=[0]*10 //10개의 리스트값이 생김(인덱스0~9)
#
# a=[[0]*3 for _ in range(4)] //안쪽에 인덱스3개짜리 1차원리스트 //[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
#
# a[1][1] =2
# for x in a:
#     print(x) //[0,0,0] //[0,2,0]//[0,0,0]
# for x in a:
#     for y in x:
#         print(y,end=' ') //0 0 0 // 0 2 0 // 0 0 0
#     print()
#
# //함수 람다함수(익명함수: 내장함수의 인자로 사용될떄 편함)
#
# def plus1(x):
#     return x+1
#
# plus2 = lambda x:x+2   //x: 매개변수 // x+2: 리턴값
# print(plus2(3)) //5
#
# a = [1,2,3]
# print(list(map(plus1,a))) // map(함수,자료) // [2,3,4]
# print(list(map(lambda x:x+2 ,a))) // [3,4,5] //sort할떄 정렬기준으로 lamda표현식을 씀


# //최소값구하기
# arr = [11,22,3,4]
# arrMin=float('inf') #파이썬에서 가장큰값
# for i in range(len(arr)):
#     if arr[i]<arrMin:
#         arrMin=arr[i]
# print(arrMin)


# 반올림
# round(2.500) 또는
# a=66.4
# a=a+0.5
# a=int(a)