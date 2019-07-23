import os
# abspath：
print(os.path.abspath(__file__))        # 文件的绝对路径
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIR)

print('分割线'.center(40, '-'))

# __file__：
print(__file__)         # pycharm的输出是当前运行脚本的所在路径，python命令输出的则是文件名
v = os.path.dirname(os.path.dirname(__file__))
print(v)                # pycharm输出的是上级目录。python命令则输出的是空行，因为上面的命令python输出的是run.py
