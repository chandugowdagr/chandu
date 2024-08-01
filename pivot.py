import pandas as p
t={'cource':["py","jv","dbms","cn","se"],"fee":[300,600,21,350,67],"complexity":[100,56,32,10,67]}
d=p.DataFrame(t)
print(d)
print("\n",d.pivot(columns="cource",values="complexity"))
print("\n",d.melt())