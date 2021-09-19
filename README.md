# 3119009457
# 论文查重
|    这个作业的课程在哪里    |    [计科国际班](https://edu.cnblogs.com/campus/gdgy/Internationalcourseincomputationalscienceandtechnology/join?id=CfDJ8NACB8VE9qlHm6Ujjqxvg5Ayisg__TqvFN0AM6AtU_c_KypnNsqE5fknzqPAYNrCn0O7WZhz0Aix4FonDG9TOlV33NuUS00SAIvr-e7vaJSyDvdlufquf2FCwW5Fe0vtiacNlgZLvMc9_SozgheHEBU)|
| :----                    | :---- |
|    这个作业要求在哪里      |    [作业要求](https://edu.cnblogs.com/campus/gdgy/Internationalcourseincomputationalscienceandtechnology/homework/12187)   |      
|    这个作业的目标          |    完成论文查重算法    | 
### 1.[GitHub地址](https://github.com/xiaotuolu/3119009457)
### 2.PSP表格
|PSP2.1                                |Personal Software Process Stages  |预估耗时（分钟）| 实际耗时（分钟）|    
|                                      -|-                                 |-             |-|
|Planning                              |计划                              |10            |30                |
|Estimate                              |估计这个任务需要多少时间            |10            |10                |
|Development                           |开发                              |420           |300                |
|Analysis                              |需求分析 (包括学习新技术)           |240           |900               |
|Design Spec                           |生成设计文档                       |60            |180                |
|Design Review                         |设计复审                          |30             |60               |
|Coding Standard                       |代码规范(为目前的开发制定合适的规范)|30             |60                |
|Design                                |具体设计                          |420            |300               |
|Coding                                |具体编码                          |300            |300               | 
|Code Review                           |代码复审                          |60             |120               | 
|Test                                  |测试（自我测试，修改代码，提交修改）|60             |180                | 
|Reporting                             |报告                              |30            |180                | 
|Postmortem & Process Improvement Plan |事后总结, 并提出过程改进计划        |30            |30                | 
|                                      |合计                              |1700          |2470                |
### 3.计算模块接口的设计与实现过程
![](https://img2020.cnblogs.com/blog/2526474/202109/2526474-20210919043620032-1406924399.png)

在程序中我就设计了一个函数。输入两个文件，首先判断两个文件是否存在，是否为空。若不存在或为空则相应输出信息并退出。然后创建一个空的字典和一个包含停用词的列表，编译中文正则表达式。读取第一个文件用jieba全模式分词构成一个列表。遍历循环该列表，将不在停用词列表中的中文字词作为键，值是只有两个初始元素为0的列表。如果该字词第一次出现，则这个键对应的值的第一个元素为1，如果不是第一次出现，这个列表值的第一个元素加1。最后关闭文件。对文件二进行类似操作。通过余弦算法计算相似率，结果放在result文件中。
### 4.计算模块接口部分的性能改进
![](https://img2020.cnblogs.com/blog/2526474/202109/2526474-20210919214327323-41503690.png)

![](https://img2020.cnblogs.com/blog/2526474/202109/2526474-20210919215007581-1206480331.png)

![](https://img2020.cnblogs.com/blog/2526474/202109/2526474-20210919215031747-1332023259.png)

![](https://img2020.cnblogs.com/blog/2526474/202109/2526474-20210919215058787-1438172091.png)

相对于命令行输入文件路径所用的时间，函数执行的时间很少。如果不要求命令行输入文件的话，可以将多个测试文本的路径构成列表，每次引用函数选取列表中的两个元素。可以省去命令行输入文件路径的时间。
### 5.计算模块部分单元测试展示
测试代码：

![](https://img2020.cnblogs.com/blog/2526474/202109/2526474-20210919222834065-1268751856.png)

测试了（1）正常输入两个文件（2）文件一不存在（3）文件一为空（4）文件二不存在（5）文件二为空 一共五种情况。
在test文件夹中加入empty.txt空文件。result文件存放输出结果。

![](https://img2020.cnblogs.com/blog/2526474/202109/2526474-20210919223711720-164509536.png)

进行测试

![](https://img2020.cnblogs.com/blog/2526474/202109/2526474-20210919224224318-2122125454.png)

main.py的测试覆盖率为100%

![](https://img2020.cnblogs.com/blog/2526474/202109/2526474-20210919224309413-4795609.png)

对测试文本进行测试

![](https://img2020.cnblogs.com/blog/2526474/202109/2526474-20210919225604688-1091639046.png)

![](https://img2020.cnblogs.com/blog/2526474/202109/2526474-20210919225627593-446141571.png)


### 6.计算模块部分异常处理说明
测试了（1）文件一不存在（2）文件一为空（3）文件二不存在（4）文件二为空 一共四种异常情况。

![](https://img2020.cnblogs.com/blog/2526474/202109/2526474-20210919224744865-1297104344.png)
