import heapq
from itertools import product
from itertools import combinations
from collections import deque
from collections import defaultdict
from math import gcd
from math import lcm
import sys
sys.setrecursionlimit(100000)
dx=[-1, 0, 1, 0]
dy=[0, 1, 0, -1]
# def dfs(y,x):
#     global cnt
#     cnt += 1
#     visit[y][x]=Truea
#     for i in range(4):
#         ny = y+dy[i]
#         nx = x+dx[i]
#         if 0<=ny<n and 0<=nx<m and graph[ny][nx] and visit[ny][nx]==False:
#             dfs(ny,nx)
Max=100001
n,m = map(int,input().split())
q = deque()
q.append(n)
graph = [-1]*Max
graph[n]=0

while q:
    current = q.popleft()
    if current==m:
        print(graph[m])
        break
    if 0<=current*2 < Max and graph[current*2] == -1:  # 순간이동
        graph[current*2] = graph[current]
        q.appendleft(current * 2) #곱하기는 더높은 우선순위를 가지므로
    if 0<=current + 1 < Max and graph[current+1] == -1: # x+1이동
        graph[current+1] = graph[current] + 1
        q.append(current + 1)
    if Max>current - 1 >= 0 and graph[current-1] == -1: # x-1이동
        graph[current-1] = graph[current] + 1
        q.append(current - 1)
































# maps.get(typ, 0) => typ이 없으면 0을 반환
# maps.get(type) =>typ이 없으면 none반환


# ''.join['a', 'b', 'c'] =>"abc"
# '_'.join(['a', 'b', 'c']) => "a_b_c"


# zip:
# print(list(zip([1,2,3], (4,5,6), "abcd")))
# [[1, 4, 'a'], [2, 5, 'b'], [3, 6, 'c']]

# startswith
# print("dfagd".startswith("abcd"))
# print("abcde".startswith("abcd"))
# False
# True


# heapq.heapify(list) #기존의 리스트를 오름차순 heapQ로 변환
# heapq.heappop(list) #list의 가장 작은 값을 return하며 삭
# heapq.heappush(list, value) #list에 value를 삽입, 자동으로 정렬한다

# def solution(scoville, K):
#     answer = 0

#     while min(scoville)<K:
#         scoville.sort()
#         a = scoville.pop(0)
#         b = scoville.pop(0)
#         scoville.append(a+b*2)
#         answer+=1
#     return answer

#bin: 10진수->2진수 '0b1010'

# numbers = [1, 2, 3]
# letters = ["A", "B", "C"]
# for pair in zip(numbers, letters):
#     print(pair)
# (1, 'A')
# (2, 'B')
# (3, 'C')

# zip() 함수는 iterable 자료형의 각각의 요소를 나눈 후
#순서대로 묶어서 요소 개수만큼 새로운 iterable 자료형을 생성

#rjust
# 오른쪽으로 정렬하도록 도와준다.
# rjust를 통해 공백의 수, 공백을 메워줄 문자를 넣어준다.

# val = "77".rjust(5, "0")
# print(val) 00077

# val = "77777".rjust(5, "0")
# print(val) 77777

# val = "123".rjust(5, "a")
# print(val) aa123

# val = "123".rjust(3, "a")
# print(val) 123


# ljust
# 왼쪽으로 정렬하도록 도와준다
# ljust를 통해 공백의 수, 공백을 메워줄 문자를 넣어준다.

# val = "222".ljust(3, "0")
# print(val) 222

# val = "222".ljust(15, "a")
# print(val) 222aaaaaaaaaaaa
# 222
# 222aaaaaaaaaaaa



# print(a//b) //5를 2로 나눈 몫
# print(a%b) //a를 b로 나눈 나머지
# print(a/b) //a를 b로 나눈값 (나눈값 = 몫+나머지)
# print(a**b) //a를 b번 거듭제곱 2**3 = 8

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

# r.shuffle(a) // a 순서가 뒤죽박죽
# a.sort() //오름차순정렬
# a.sort(reverse=True)//내림차순정렬
# a.clear() //리스트값 없어짐 -> 빈리스트

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

# product : 중복순열
# https://hinos.tistory.com/94