
squres_comp = (i**2 for i in range(10))

for i in range(10):
    print(next(squres_comp))
    
    # 0
    # 1
    # 4
    # 9
    # 16
    # 25
    # 36
    # 49
    # 64
    # 81


for i in range(11):
    print(next(squres_comp))

# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# Traceback (most recent call last):
#   File "d:\GoIT\Python Core\Modul_9_Namespaces\3_Practice\9_2_exe_1_generator_2.py", line 19, in <module>
#     print(next(squres_comp))
#           ^^^^^^^^^^^^^^^^^
# StopIteration