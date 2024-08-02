#pie chart
import matplotlib.pyplot as p
us=[12,32,16,45]
la=["Asus","Dell","Lenova","HP"]
e=[0,0,0,0.04]
c=["RED","CYAN","BLUE","YELLOW"]
p.pie(us,labels=la,startangle=270,explode=e,colors=c,autopct="%1.2g%%")
p.show()