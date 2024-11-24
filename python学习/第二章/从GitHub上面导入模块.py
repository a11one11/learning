#正常需要先用pip或conda安装，但是可以使用 import_from_github_com  可以直接运行
#pip install import_from_github_com -i https://pypi.tuna.tsinghua.edu.cn/simple 这个可以通过来导入网站发布的其他模块
from github_com.mozillazg.pypinyin import  lazy_pinyin,Style
print(lazy_pinyin('代码医生',style=Style.TONE))
