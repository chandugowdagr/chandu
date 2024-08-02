import matplotlib.pyplot as p
Q=["Q1","Q2","Q3","Q4"]
ssd=[200,230,350,400]
hdd=[250,240,320,250]
p.plot(Q,ssd,"^-",color="black")
p.plot(Q,hdd,"o-.r")
p.xlabel("Quarters is 2022"),p.ylabel("sales units")
p.title("ssd and hdd sales in store")
p.legend(["ssd","hdd"])
p.show()