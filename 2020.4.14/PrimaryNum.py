#nums = [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3]  # 主元素问题  3   k:V
nums1 = [1, 1, 2, 3, 3, 3, 4, 4] # 1 2 3 4  作业2

# def majorityNumber(nums):
#     key, count = None, 0
#     for num in nums:
#         if key is None:
#             key, count = num, 1
#         else:
#             if key == num:
#                 count += 1
#             else:  # 最关键的,不执行这句，答案是1
#                 count -= 1
#         if count == 0:
#             key = None
#     return key,count
# print(majorityNumber(nums))
#output:(3,6) count少1，因为1是4，count=4,2是3个，count=1，第一个3时count=0，key=None，下次循环开始才开始计数
#改进，既能找出主元素，又能保证count正确
# 作业2  出现 nums.length/4次 的值返回为 list 可以用字典解决
#法1，利用列表的count函数，while循环
def majorityNumber1(nums):
    i=j=0  #i为nums的下标，j为元素相同的数量
    result = []
    while(i<len(nums)-1):
        j = nums.count(nums[i]) #计算元素nums[i]的数量
        if j == len(nums)/4 : #判断数量是不是等于nums长度的1/4
            result.append(nums[i]) #是则添加在结果列表中
        i += j # 下一次从下一个不同的元素开始判断
    return result

print(majorityNumber1(nums1))
#法2，用字典的方法
def majorityNumber1(nums):
    # s = set(nums)
    # print(s)
    res = {}  #定义空字典
    result=[] #定义结果列表
    for i in nums:
        #print(i)
        res.update({i:nums.count(i)}) #更新字典的值
    for key, value in res.items():#遍历字典，如果value符合要求，则添加到结果列表中
        if value == len(nums)/4:
            result.append(key)

    return result

print(majorityNumber1(nums1))

#快速定位错误代码：ctrl+g








