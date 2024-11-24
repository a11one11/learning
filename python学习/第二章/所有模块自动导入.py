# pyforest库可以实现所有模块的自动导入
#1.pip install pyforest -i https://pypi.tuna.tsinghua.edu.cn/simple
#2  python -m pyforest install_extensions 在使用时引用该模块，会根据你需要的模块自行加载
#3.如果想知道自动加载了那些模块，使用active_imports()
#因为这个是别人创造的可能没有那个模块，
from pyforest import *#只是需要引入pyforest模块即可
op=os.getcwd()
print("当前路径：",op)
print("py版本信息：",sys.version_info)
active_imports()

