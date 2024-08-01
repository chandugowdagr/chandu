import pandas as p
d=p.DataFrame([[2,5,6],[4,5,3],[5,7,8]],columns=["maths","java","py"])
print(d)
c=d.agg(["sum","min","max","count","mean","median","std","size"])
print()
print(c)