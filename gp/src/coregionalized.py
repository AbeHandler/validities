from numpy import ndarray
from GPy.util.multioutput import build_XY
import pandas as pd
import numpy as np
import GPy

from dataclasses import dataclass
from src.plotter import Plotter
from src.generator import DataGenerator

import pandas as pd
import altair as alt
import GPy
import numpy as np


class Coregionalized(object):


    def __init__(self, num_tasks: int, num_feats: int):
        '''
        num_tasks is the total number of categories of Y observations
        num_feats is the total number of features per X
        '''
        self.num_feats = num_feats
        self.num_tasks=num_tasks
        ## ** denotes kronneker product here
        self.kernel = GPy.kern.RBF(input_dim=n_feats) ** GPy.kern.Coregionalize(input_dim=1, output_dim=num_tasks, rank=1)

    def fit(self, X, Y, task_indexes):
        '''
        X is array of input observations, of shape (n_obs, n_feats)
        Y is array of output observations, of shape (n_obs,)
        tasks is array of tasks indexes, of shape (n_obs,)
        '''

        # X has a a special input format where the last column is the task
        _X = self._prepare_X(X, task_indexes)

        self._validate_fit(X, Y, task_indexes)

        m = GPy.models.GPRegression(_X, Y, self.kernel)
        m.optimize()
        self.m = m

    def predict(self, X: ndarray, tasks: ndarray):
        _X = self._prepare_X(X, tasks)
        self._validate_predict(tasks)
        means, variances = self.m.predict(_X)
        return (means, variances)

    def _prepare_X(self, X,  tasks):
        # X has a a special input format where the last column is the task
        # This method gets the data into that format
        return np.hstack([X, tasks])

    def _validate_fit(self, X, Y, tasks):
        assert len(X) == len(Y), 'must have n_obs (X--Y) pairs so len(X) should equal len(Y)'
        assert np.unique(tasks).size == self.num_tasks, "tasks must be "

    def _validate_predict(self, tasks):
        assert np.unique(tasks).size == self.num_tasks, f"expecting {self.num_tasks} tasks"



if __name__ == "__main__":

    num_obs=100
    n_feats=1
    spread=2
    generator = DataGenerator()
    X, Y, task_indexes = generator.generate(num_obs, n_feats, spread=2)
    coregionalized = Coregionalized(num_tasks=3, num_feats=n_feats)
    coregionalized.fit(X, Y, task_indexes)
    coregionalized.predict(X, task_indexes)