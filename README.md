# PythonSparkMachineLearningTest

本项目为BUPT SCSS 大三上小学期作业，建构了一个基于机器学习的恶意加密流量检测工具。

## 数据集特征

来源:[CSE-CIC-IDS2018 on AWS](https://www.unb.ca/cic/datasets/ids-2018.html)

总共80个特征，含义如下所示

```
0 Dst Port 目的端口
1 Protocol 协议
2 Timestamp 时间戳
3 Flow Duration 流动持续时间
4 Tot Fwd Pkts 前向总包数
5 Tot Bwd Pkts 反向总包数
6 TotLen Fwd Pkts 正向报文总大小
7 TotLen Bwd Pkts 反向报文总大小
8 Fwd Pkt Len Max 正向报文的最大大小
9 Fwd Pkt Len Min 报文转发的最小尺寸
10 Fwd Pkt Len Mean 正向报文的平均大小
11 Fwd Pkt Len Std 数据包的标准偏差大小（正向）
12 Bwd Pkt Len Max 反向最大包数
13 Bwd Pkt Len Min 反向最小包数
14 Bwd Pkt Len Mean 数据包在后向的平均大小
15 Bwd Pkt Len Std 数据包向后的标准偏差大小
16 Flow Byts/s 流字节率，即每秒传输的数据包数
17 Flow Pkts/s 流数据包速率，即每秒传输的数据包数
18 Flow IAT Mean 两次流动之间的平均时间
19 Flow IAT Std 标准偏差时间两流
20 Flow IAT Max 两次流动之间的最大时间
21 Flow IAT Min 两次流动之间的最短时间
22 Fwd IAT Tot 正向发送的两个数据包之间的总时间
23 Fwd IAT Mean 正向发送的两个数据包之间的平均时间
24 Fwd IAT Std 向前发送的两个数据包之间的标准偏差时间
25 Fwd IAT Max 正向发送两个数据包之间的最长时间
26 Fwd IAT Min 正向发送两个数据包之间的最短时间
27 Bwd IAT Tot 反向发送两个数据包之间的总时间
28 Bwd IAT Mean 向后发送两个数据包之间的平均时间
29 Bwd IAT Std 反向发送的两个数据包之间的标准偏差时间
30 Bwd IAT Max 反向发送两个数据包之间的最长时间
31 Bwd IAT Min 向后发送两个数据包之间的最短时间
32 Fwd PSH Flags 在正向传输的数据包中设置PSH标志的次数（UDP为0）
33 Bwd PSH Flags 在向后传播的数据包中设置PSH标志的次数（UDP为0）
34 Fwd URG Flags 在正向传输的数据包中设置URG标志的次数（UDP为0）
35 Bwd URG Flags 在反向传输的数据包中设置URG标志的次数（UDP为0）
36 Fwd Header Len 正向用于标头的总字节数
37 Bwd Header Len 正向用于标头的总字节数
38 Fwd Pkts/s 每秒转发报文数
39 Bwd Pkts/s 每秒反向包数
40 Pkt Len Min 最小流长
41 Pkt Len Max 最大流长
42 Pkt Len Mean 平均流长
43 Pkt Len Std 流量的标准偏差长度
44 Pkt Len Var 数据包的最小到达时间
45 FIN Flag Cnt FIN的报文数
46 SYN Flag Cnt SYN报文数
47 RST Flag Cnt RST报文数
48 PSH Flag Cnt PUSH的数据包数
49 ACK Flag Cnt ACK报文数
50 URG Flag Cnt URG的数据包数
51 CWE Flag Count CWE的数据包数
52 ECE Flag Cnt 带有ECE的数据包数量
53 Down/Up Ratio 上载比例
54 Pkt Size Avg 包平均大小
55 Fwd Seg Size Avg 向前观察到的平均尺寸
56 Bwd Seg Size Avg 向后观察到的平均尺寸
57 Fwd Byts/b Avg 正向的平均字节批量率
58 Fwd Pkts/b Avg 正向平均报文散装率
59 Fwd Blk Rate Avg 前进方向的平均散货数量
60 Bwd Byts/b Avg 向后平均字节数批量速率
61 Bwd Pkts/b Avg 反向平均包数散装率
62 Bwd Blk Rate Avg 反向平均散货数量
63 Subflow Fwd Pkts 子流中转发方向的平均包数
64 Subflow Fwd Byts 子流中正向的平均字节数
65 Subflow Bwd Pkts 子流反向平均包数
66 Subflow Bwd Byts 子流中反向的平均字节数
67 Init Fwd Win Byts 在初始窗口中向前发送的字节数
68 Init Bwd Win Byts 在初始窗口中向后发送的字节数
69 Fwd Act Data Pkts 在正向方向上具有至少1个字节的TCP数据有效载荷的数据包数量
70 Fwd Seg Size Min 向前观察到的最小片段大小
71 Active Mean 流空闲之前的平均时间
72 Active Std 流量在变为空闲之前处于活动状态的标准偏差时间
73 Active Max 流量在空闲之前处于活动状态的最长时间
74 Active Min 空闲之前流处于活动状态的最短时间
75 Idle Mean 流在变为活动状态之前处于空闲状态的平均时间
76 Idle Std 流量在变为活动状态之前处于空闲状态的标准偏差时间
77 Idle Max 流量变为活动状态之前空闲的最长时间
78 Idle Min 流量变为活动状态之前的最短空闲时间
79 label 标签
```

总共十四个标签，对应的编号如下所示

```python
labels = {'Benign':0,
	'Brute Force -Web':1,
	'Bot':2,
	'FTP-BruteForce':3,
	'DoS attacks-SlowHTTPTest':4,
	'DDOS attack-HOIC':5,
	'DDOS attack-LOIC-UDP':6,
	'Infilteration':7,
	'DoS attacks-Slowloris':8,
	'DoS attacks-Hulk':9,
	'DoS attacks-GoldenEye':10,
	'SSH-Bruteforce':11,
	'Brute Force -XSS':12,
	'SQL Injection':13
	}
```

数据集使用CICFlowMeter进行处理，参考教程如下

https://www.anquanke.com/post/id/207835



## 脚本功能

全局变量说明

```
os.environ['PYSPARK_PYTHON'] 你的计算机上python路径
TEST_DATA_PATH 用于训练模型的数据的位置
TEST_MODEL_PATH 模型的存放位置
NUM_OF_FUTURE 特征数量
NUM_OF_CLASSES 分类数量
NUM_OF_TREES 随机森林的决策树数量
MAXDEPTH 随机森林的决策树最大递归层数
MAXBINS 随机森林的决策树最大分支数量
TEST_PREDICT_PATH 使用模型进行预测后结果存放位置
INPUT_DATA_PATH 使用模型进行预测时输入的数据位置
```

### csv2libsvm.py

将数据集的csv文件转为libsvm格式，方便读入模型。

脚本去除了不合规则的数据行，并且将时间字符串转换为了时间戳格式。

使用方法

```bash
python3 csv2libsvm.py input_file output_file 79
其中79是label的列号（第80列）
```

### analyse_dataset.py

用于分析、提取数据集关键特征的脚本。

get_all_headers()用于提取所有字段名称

get_all_labels()用于统计所有标签字段的值

### dataset_cleaning.py

用于将目标文件夹下所有数据集进行清洗，以libsvm格式存入新的文件夹中。

用法

```bash
python3 dataset_cleaning.py src_dir target_dir
```

### vis.py

用于将生成的随机森林模型转换为json。这是可视化模型的第一步，接下来会通过D3.js和web应用进行呈现。

转化后的json会放入`/vis/data`中，名称为`structure.json`，同时会生成原始模型的Debug String，同样在`/vis/data`中，名称为`debugString`

用法

```
python3 vis.py MAX_DEPTH TREE_TO_CONVERT
MAX_DEPTH：生成的树的最大深度，建议为5-8左右。如果深度过大会导致显示问题
TREE_TO_CONVERT：希望生成的树的编号。随机森林模型包含多颗决策树，使用此参数选择你希望转换的树
```

### LearningTest.py

用于训练模型的脚本