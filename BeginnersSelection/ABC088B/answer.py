n = int(input())
a_list = list(map(int, input().split()))

a_list = sorted(a_list, reverse=True)
Alice = []
Bob = []

while(len(a_list) != 0):
    if len(a_list) != 0:
        Alice.append(a_list.pop(0))
    if len(a_list) != 0:
        Bob.append(a_list.pop(0))

print(sum(Alice) - sum(Bob))
