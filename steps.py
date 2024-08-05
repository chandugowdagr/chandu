import pandas as pd
import numpy as np
d={"Day":[1,2,3,4,5,6,7,8,9,10],
   "steps":[6012,4079,6386,5230,4598,5564,6971,7763,8032,8569]}
dp=pd.DataFrame(d)
dp["+1000 steps"]=dp["steps"]+1000
fi=dp[dp["+1000 steps"]>7000]["Day"]
print("Dataframe:",dp)
print("Day on which steps were >7000\n",fi)