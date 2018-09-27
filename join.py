import numpy as np
import pandas as pd

pd.merge(adf, bdf,
         how='left', on='x1')

pd.merge(adf, bdf,
         how='right', on='x1')

pd.merge(adf, bdf,
         how='inner', on='x1')

pd.merge(adf, bdf,
         how='outer', on='x1')