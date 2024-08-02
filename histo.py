import matplotlib.pyplot as p
import numpy as n
x=n.random.normal(180,5,200)
p.hist(x,color="k")
p.xlabel("Heightn in cm"),p.ylabel("people")
p.show()