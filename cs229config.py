import platform
from pathlib import *
# ====================You SHOULD config path to your assignments-relative materials. ('linux_cs229' or 'windows_cs229')---------
# [machine-learning-ex1.zip](https://github.com/ZhangYikaii/Coursera_AndrewNg_ML_Exercises/blob/master/machine-learning-ex1.zip) 
# ~ [machine-learning-ex8.zip](https://github.com/ZhangYikaii/Coursera_AndrewNg_ML_Exercises/blob/master/machine-learning-ex8.zip) 
# are avaliable on [github](https://github.com/ZhangYikaii/Coursera_AndrewNg_ML_Exercises)

# You can download and unzip these materials under the following Paths.
linux_cs229 = r'/media/curie/Windows7_OS/data/网络资源-吴恩达机器学习课程/编程作业'
windows_cs229 = r'C:/data/网络资源-吴恩达机器学习课程/编程作业/'
def cs229basepath():
    if(platform.system()=='Linux'):
        return linux_cs229
    else:
        return windows_cs229        
# cs229basepath()
# r'C:\\data\\网络资源-吴恩达机器学习课程\\编程作业\\machine-learning-ex1\\ex1\\ex1data1.txt'
# r'/media/curie/Windows7_OS/data/网络资源-吴恩达机器学习课程/编程作业/machine-learning-ex1/ex1/ex1data1.txt'
