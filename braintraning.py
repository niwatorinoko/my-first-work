import random

methods = input("１，加法２,減法３，乘法４，除法:")
methods = methods.replace("1", "+")
methods = methods.replace("2", "-")
methods = methods.replace("3", "×")
methods = methods.replace("4", "÷")

split_list = methods.split(" ")

times = int(input("問題數："))
types = int(input("１，簡單２，普通３，很難:"))
result = 0
print("<注意>\n如果用除的除不盡有剩的話,請只有回答整數的部分。")
print("------------------------開始------------------------")

a_list = []
b_list = []
m_list = []

for i in range(times):
    if types == 1:
        a_list.append(random.randint(1,10))
        b_list.append(random.randint(1,10))
    elif types == 2:
        a_list.append(random.randint(1,100))
        b_list.append(random.randint(1,100))
    else:
        a_list.append(random.randint(1,1000))
        b_list.append(random.randint(1,1000))
    m_list.append(split_list[random.randint(0, len(split_list)-1)])
    
for j in range(times): 
    a = a_list[j]
    b = b_list[j]
    m = m_list[j]
    if m == "+":
        answer = a+b
    elif m == "-":
        answer = a-b
    elif m == "×":
        answer = a*b
    else:
        answer = a//b
    user_answer = int(input("{} {} {} = ".format(a,m,b)))
    if answer == user_answer:
        result+=1
print("------------------------結束------------------------")
print("答對率：{:.2f}%".format(result/times*100))