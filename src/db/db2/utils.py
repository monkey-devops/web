import os
import sys
print('utils模块')
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))		# 需要找到项目主目录和相对上级目录，例如此例我的项目主目录是oldboy_python，相对上级目录是bin
sys.path.append(BASE_DIR)
for item in sys.path:
    print(item)
from lib.jd import show
show()
print(__name__)