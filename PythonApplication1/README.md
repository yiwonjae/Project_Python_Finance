
### �ʼ� Package

pip install pandas


### �ؼ� 1

> yahoo���� �ֽ� Data�� Pandas�� �̿��Ͽ� ���� ����
> 
> �ѱ� ������ **�����ڵ�.KS** ���ϸ� �ȴ�.


### Code 1

~~~python
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt

start   = datetime.datetime(2010,1,1)
end     = datetime.datetime(2017,10,9)

# CODE: GS - A078930
# CODE: SK HINIX - A000660
# CODE: TESNA - A131970 ERROR Because SMALL Coperation
data = web.DataReader("000660.KS", "yahoo", start, end)

print(data)

~~~



### ��� 1

![](output01.PNG)

### �ؼ� 2


pandas�� DataReader�� Argument�� Start, End�� �������̸�
�ش� Value�� ���� ���� ��� Default Value�� ����ȴ�.


### Code 2

~~~python
# start, end�� ���� �ʴ� ��� default
# start : 2010-01-01
# end   : Function ���� �ð�
data = web.DataReader("000660.KS", "yahoo")

print(data.info())

~~~



### ��� 2

![](output02.png)