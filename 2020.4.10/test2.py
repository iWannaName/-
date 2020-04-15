#列表元素反转
temp=['a','b','c','d','e'] #input
left=0
right=len(temp)-1
while(left<right):
    temp[left],temp[right]=temp[right],temp[left]
    left+=1
    right-=1
print(temp)
#['e', 'd', 'c', 'b', 'a']
#，输入输出是序列，不是字符串

#字符串反转
#法1，使用字符串切片
temp="abcde"#input
result=temp[::-1]
print(result)
#法2，使用for循环
result=""
for index,value in enumerate(temp):
    result+=temp[len(temp)-1-index]
print(result)
#法3，使用join方法
result=""
result="".join(temp[::-1])
print(result)