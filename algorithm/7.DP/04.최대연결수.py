import sys
import heapq as hq
from collections import deque
sys.setrecursionlimit(10**6)

n=int(input())
arr=list(map(int, input().split()))
arr.insert(0,0)
dy=[0]*(n+1) #각원소를 마지막이라고 쳤을때 길이
dy[1]=1
res=0
for i in range(2, n+1):
    max=0
    for j in range(i-1, 0, -1): #i-1 ~1까지
        if arr[j]<arr[i] and dy[j]>max: #자기보다 아래 인덱스의 원소보다 크고 , 아래인덱스값중에 최대값 찾기
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res: #최종결과(최대길이)
        res=dy[i]
print(res)


#최대부분 증가수열
#각 원소를 자기가 마지막항이라고 가정하고 수를 세줌



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
#이진트리순회 //재귀 이용해서 dfs
# #부왼오: 전위
# #왼부오: 중위
# #왼오중: 후위int(a)

#병합정렬:mid를 기준으로 두개의 영역으로 나눈후, 그 두개의 영역이 정렬되면, 두 영역을 정렬해서 합침 (리스트 길이가 1일때까지 나눔)(후위방식)
# def dsort(lt,rt):
#     if lt<rt:
#         mid = (lt+rt)//2
#         dsort(lt,mid)
#         dsort(mid+1,rt) #두개의 영역으로 나누고
#         p1=lt #두 영역을 정렬해서 합침
#         p2=mid+1
#         tmp=[]
#         while p1<=mid and p2<=rt:
#             if arr[p1]<arr[p2]:
#                 tmp.append(arr[p1])
#                 p1+=1
#             else:
#                 tmp.append(arr[p2])
#                 p2+=1
#         if p1<=mid: #p1이 남음
#             tmp=tmp+arr[p1:mid+1]
#         if p2<=rt:
#             tmp=tmp+arr[p2:rt+1]
#         for x in range(len(tmp)): #주의 합칠때 i부터가 아닌 lt+i 부터임
#             arr[lt+x]=tmp[x]
# arr = [4,1,2,5]
# dsort(0,3)
# print(arr)


#퀵정렬:피벗값을 정하고,pos는 시작점//pos값이 피벗값보다 크면 i증가,//작으면 arr[i]와 arr[pos]값을 교환(교환이 일어나면 pos 증가)
#for문이 다끝나고 pivot값과 pos 값을 교환 // 그후 피벗값 왼쪽,오른쪽으로 구분
# def qsort(lt,rt):
#     if lt<rt:
#         pos=lt
#         pivot=arr[rt]
#         for i in range(lt,rt):
#             if arr[i]<=pivot:
#                 arr[i],arr[pos]=arr[pos],arr[i]
#                 pos+=1
#         arr[rt], arr[pos] = arr[pos], arr[rt]
#         qsort(lt,pos-1)#pos지금 축
#         qsort(pos+1,rt)
# arr = [4,1,2,5]
# qsort(0,3)
# print(arr)

#재귀,메모이제이션:top-down -> dfs이용
#dy[n] = dy[n-1]+dy[n-2]
#dfs(7) = dfs(6)+dfs(5) -> 재귀로 내려가면 이미구한 dfs를 또 구해야되는점이 중복됨 ->dfs로 구한값 기록후 재사용
#단순 dfs만 하면 그냥재귀 // 메모이제이션까지해야 dp