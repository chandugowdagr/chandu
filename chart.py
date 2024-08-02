#bar chart
from matplotlib import pyplot as p
pro_na=["Intel","amd","Snapdragon","Tensor"]
use=[200,100,250,50]
p.bar(pro_na,use,color="black",width=0.2)
p.xlabel("processors")
p.ylabel("no of users")
p.title("processors users in  community")
p.show() 

#pie chart
import matplotlib.pyplot as p
us=[12,32,16,45]
la=[12,32,16,45]
e=[0,0,0,0.04]
c=["g","c","#8B0000","#473C8B"]
p.pie(us,label=la,startangle=270,explode=e,colors=c,autopct="%1.2g%%")
p.show()