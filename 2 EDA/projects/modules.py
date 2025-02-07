import numpy as np
import pandas as pd

def mad(series):
    if not isinstance(series, pd.Series):
        return np.nan  # проверка данных

    if series.empty:
        return np.nan

    # рассчитываем среднее значение
    mean = series.mean()

    # рассчитывает абсолютное отклонение
    absolute_deviations = np.abs(series - mean)

    # рассчитываем среднее значение абсолютного отклонения
    mad = absolute_deviations.mean()

    return mad