import pandas as pd
import numpy as np
from statsmodels.stats.weightstats import ztest

chat_id = 285100540 # Ваш chat ID, не меняйте название переменной

def solution( x: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    p = 0.06
    stat, pval = ztest(x, value = 300, alternative='smaller')
    if pval >= p:
        return False
    else:
        return True
