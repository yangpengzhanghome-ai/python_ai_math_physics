my_name = "yangpeng"  # print out my name
print(my_name)
##### ==========================================================================
my_age = 20
print(my_age)

print("My name is",my_name,"and my age is", my_age)

year = 2025
stundets_in_class = 0
pi = 3.1415926
temperature = 42

message = "Hello AI comin on the way"
language = 'python or matlab'

is_raining = False
is_sunny = True # Las Vegas is always in this case lol

print(type(year))
print(type(pi))
print(type(is_sunny))

# practice math
a = 10
b = 3
print("a =",a,"b=",b)
# 加法
sum_result = a + b
print("a + b =", sum_result)

# 减法
difference = a - b
print("a - b =", difference)

# 乘法
product = a * b
print("a * b =", product)

# 除法 (总是返回浮点数)
quotient = a / b
print("a / b =", quotient)

# 取整除法 (丢弃小数部分)
floor_division = a // b
print("a // b =", floor_division)

# 取余数 (模运算)
remainder = a % b
print("a % b =", remainder)

# 指数运算 (幂)
power = a ** b
print("a ** b =", power)

# practice string list
first_name = "章"
last_name = "羊盆"

# connect stings
full_name = first_name + last_name
print("全名:", full_name)

# repeat character
laugh = "哈"
big_laugh = laugh * 10
print(big_laugh)  # 输出: 哈哈哈哈哈哈哈哈哈哈lol

# remember that string and numbers cannot be added directly
age = 25
#print("我今年" + age + "岁")  # 这行会报错
print("我今年" + str(age) + "岁")  # 正确写法: 使用str()函数将数字转为字符串

# user input
# ==============================================================================
# 获取用户输入
user_name = input("Type in your name: ")
fav_lang = input("Your favorite languages among C, python, Java, matlab: ")

# 注意: input() 总是返回字符串，即使输入的是数字
print("Hey,",user_name)
print("My favorite language is:",fav_lang)  # 输出: <class 'str'>
