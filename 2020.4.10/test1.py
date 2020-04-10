#字符串压缩
# temp = "ssssssssssrrrrrrrrrrrrttttttttt"  input
# tempRes = "s10r12t9"  output
temp="ssssssssssrrrrrrrrrrrrttttttttt"
count=1 #记录重复的个数,默认都是1个
tempRes=[]#输出列表
temp=temp+"g"#随便给字符串拼接一个字符，为了确保最后一个字符可以加在tempRes中
for i in range(1,len(temp)):
    if temp[i]!=temp[i-1]:#当前元素和前一个元素不相同，即不是重复元素
        tempRes.append(temp[i-1])#将前一个元素加在tempRes中
        if count>1:#判断count是否大于1
            tempRes.append(str(count))#将count转为str类型加入tempRes中
            count=1#前1个元素的数量已经计数完毕，重置count
    else:#是重复元素时
        count+=1
print(tempRes)
#['s', '10', 'r', '12', 't', '9']

# 其中遇到的问题：
# 1. 没有重置count，输出结果为['s', '10', 'r', '21']，解决方法是在13行添加count=1
#2. 最后一个元素添加不进去，输出结果为['s', '10', 'r', '12']，解决方法是给temp拼接一个字符

#上午demo1中for循环的错误
