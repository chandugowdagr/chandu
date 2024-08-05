import pandas as pd
a=pd.Series([10,20,30,40,50])
b=pd.Series([40,50,60,70,80])
print("Series A:")
print(a)
print("Series B:")
print(b)
non_com=a[~a.isin(b)].tolist()+b[~b.isin(a)].tolist()
print("Items not commn to both series:")
print(non_com)
print("\nSum od series B:\n",b.sum())
print("\nAverage of series A:\n",a.mean())
print("\nMedian of series A:\n",a.median())
print("\nSmallest element in series A:\n",a.min())
print("\nLargest element in series A:\n",a.max())