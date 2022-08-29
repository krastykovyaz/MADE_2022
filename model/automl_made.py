import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
from sklearn.metrics import roc_auc_score, f1_score

df_train = pd.read_csv('../input/train.csv')
df_test = pd.read_csv('../input/test.csv')

from lightautoml.automl.presets.tabular_presets import TabularAutoML
from lightautoml.tasks import Task

N_THREADS = 1
N_FOLDS = 5
RANDOM_STATE = 21
TEST_SIZE = 0.2
TIMEOUT = 600 # equal to 10 minutes
TARGET_NAME = 'target'

task = Task('binary')
roles = {
    'target': 'target',
    'drop': ['5']
}
automl = TabularAutoML(
    task = task,
    timeout = TIMEOUT,
    cpu_limit = N_THREADS,
    reader_params = {'n_jobs': N_THREADS, 'cv': N_FOLDS, 'random_state': RANDOM_STATE}
)

oof_pred = automl.fit_predict(df_train, roles = roles, verbose = 1)
