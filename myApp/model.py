"""
This is a template model to implement panel with Numerical Input Objects and sliders.
"""
import panel as pn
import pandas as pd
import numpy as np
import hvplot.pandas
import holoviews as hv
import param as pm
import random
import math

# Importing params
from data.parameters import model_params

class Model(pm.Parameterized):
    supply_A = pm.Number(200, bounds=(0, None), step=0.01)
    supply_B = pm.Number(100, bounds=(0, None), step=0.01)
    percent_A_staked = pm.Number(60, bounds=(0, 100), step=0.01)
    percent_B_staked = pm.Number(100, bounds=(0, 100), step=0.01)
    Boolean =  pm.Boolean(True, doc="A sample Boolean parameter")
    
    def A_supply(self):
        return self.supply_A

    def B_supply(self):
        return self.supply_B

    def A_staked(self):
        return self.supply_A*self.percent_A_staked*0.01

    def B_staked(self):
        return self.supply_B*self.percent_B_staked*0.01

# Creating view object for class Model
def model_view():
    model = Model(**model_params)
    model_view = pn.Column('## Token Supply',
        pn.Row(
        model,      # importing all inputs by default from defined class 
        pn.Column(
            pn.Row("A Supply:", model.A_supply),
            pn.Row("B Supply:",model.B_supply),
            pn.Row("A staked:",model.A_staked),
            pn.Row("B staked:", model.B_staked),
            background = '#a9a9a9'
        )))
    return model_view


