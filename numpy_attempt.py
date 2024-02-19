import numpy as np
import time

z1 = time.time()
liste = np.arange(1_000_000)**100
z2 = time.time()

print(z2-z1)