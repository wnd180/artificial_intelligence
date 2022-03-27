import numpy as np
import pandas as pd
import math
q1 = [13,15,16,16,19,20,20,21,22,22,25,25,25,25,30,33,33,35,35,35,35,36,40,45,46,52,70]

# df = pd.DataFrame(q1)
# print(df.describe())
a = int(input())
b= int(input())
a2 = a*a
b2 = b*b
print(math.sqrt(a2+b2))
