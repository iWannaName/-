#字符串压缩
#temp = "ssssssssssrrrrrrrrrrrrttttttttt"  #input
#tempRes = "s10r12t9"  output
temp="ssssssssssrrrrrrrrrrrrttttttttt"

# i = 0
# result = []
# while (i < len(temp)):
#     j = 1  # 记住当前的index
#     while (i < len(temp)-1 and temp[i] == temp[i + 1]):
#         i += 1 #刷新相同对象的索引
#         j += 1 #计数器对象
#     result.append(temp[i] + str(j))
#     i = i + 1  # 更新到最新的index索引
# print(result)
#['s10', 'r12', 't9']

#demo1中的for循环的问题
result = []
for i in range(0,len(temp)):
    j = 1  # 记住当前的index
    while (i< len(temp)  and temp[i] == temp[i + 1]):
        j += 1  # 计数器对象
        i +=1
    result.append(temp[i] + str(j))
    i = i +1  # 更新到最新的index索引
print(result)
#['s10', 's9', 's8', 's7', 's6', 's5', 's4', 's3', 's2', 's1', 'r12', 'r11',
# 'r10', 'r9', 'r8', 'r7', 'r6', 'r5', 'r4', 'r3', 'r2', 'r1', 't9', 't8', 't7', 't6', 't5', 't4', 't3', 't2', 't1']
# 当i=0时，执行循环体，i=10,将‘s10’加入到了result中，然后再执行for循环的时候i=1,又执行一遍重复的，44行没用

#另一种解法
# count=1 #记录重复的个数,默认都是1个
# tempRes=[]#输出列表
# temp=temp+"g"#随便给字符串拼接一个字符，为了确保最后一个字符可以加在tempRes中
# for i in range(1,len(temp)):
#     if temp[i]!=temp[i-1]:#当前元素和前一个元素不相同，即不是重复元素
#         tempRes.append(temp[i-1])#将前一个元素加在tempRes中
#         if count>1:#判断count是否大于1
#             tempRes.append(str(count))#将count转为str类型加入tempRes中
#             count=1#前1个元素的数量已经计数完毕，重置count
#     else:#是重复元素时
#         count+=1
# print(tempRes)
#['s', '10', 'r', '12', 't', '9']

# 其中遇到的问题：
# 1. 没有重置count，输出结果为['s', '10', 'r', '21']，解决方法是在13行添加count=1
#2. 最后一个元素添加不进去，输出结果为['s', '10', 'r', '12']，解决方法是给temp拼接一个字符




