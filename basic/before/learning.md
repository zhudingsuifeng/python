- numpy函数库中存在两种不同的数据类型（矩阵matrix和数组array）,都可以用于处理行列表示的数字元素。
- 调用mat()函数可以将数组转化为矩阵。
- random.rand(3,3)#构造一个3*3的随机数组
- mat(random.rand(3,3))#将3*3的随机数组转化为一个3*3的矩阵
- shape函数是numpy.core.fromnumeric中的函数，他的功能是读取矩阵的长度，比如shape[0]就是读取矩阵第一维度的长度。
- matDemo=mat(random.rand(3,5))
- matDemo.shape[0]#获取矩阵第一维的长度，输入参数是一个整数表示维度
- matDemo.shape[1]#获取矩阵第二维的长度
- shape(matDemo)#获取矩阵的各个维度的大小，输入参数是一个矩阵
- shape(matDemo)[i]#这样写也可以获取矩阵的第i个维度的大小
- random.uniform(x,y)方法将随机生成下一个实数，它在[x,y]范围内。
- mean()方法为求均值的方法
- numpy.mean(a,axis=None,dtype=None,out=None,skipna=False,keepdims=False)
- axis=None时计算数组中所有值的平均值
- axis=0时以列为单位计算数组的每列的所有值的平均值
- axis=1时计算数组的每行为单位的所有值的平均值
- dtype为指定数组中元素的类型，默认为float64
- transpose()方法用于矩阵的转置。
- y=transpose(x)#转置
###python读取文本文件内容
- read()每次读取整个文件，它通常用于将文件内容放到一个字符串变量中。
- read()生成文件内容最直接的字符串表示，但对于连续的面向行的处理，它却是不必要的，而且如果文件大于可用内存，则不可能是先这种处理。
- readlines()一次读取整个文件，自动将文件内容分析成一个行的列表，该列表可以由Python的for...in...结构并行处理。
- readline()每次只读取一行，通常比readlines()慢得多。
- python的str类有split方法，但是这个split方法只能根据指定的某个字符分隔字符串。
- 如果要同时指定多个字符来分割字符串，可以使用python的re模块中提供的split方法来做这件事请。
- list是python的内置数据类型，list中的数据类不必相同，而array中的类型必须全部相同。
- 在list中的数据类型保存的是数据的存放地址，简单地说就是指针，并非数据。