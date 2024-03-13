import numpy as np
import pandas as pd
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_object_dtype

import matplotlib.pyplot as plt
import seaborn as sns

from IPython.core.display import HTML
sns.set_style("whitegrid")

import warnings
warnings.simplefilter(action='ignore', category=UserWarning)

class FigureLabeler:
    def __init__(self):
        self.fig_num = 1
        self.table_num = 1
    
    def fig_caption(self, title, caption):
        global fig_num
        """Print figure caption on jupyter notebook"""
        display(HTML(f"""<p style="font-size:12px;font-style:default;"><b>
                         Figure {self.fig_num}. {title}.</b><br>{caption}</p>"""))
        self.fig_num += 1

    def table_caption(self, title, caption):
        global table_num
        """Print table caption on jupyter notebook"""
        display(HTML(f"""<p style="font-size:12px;font-style:default;"><b>
                         Table {self.table_num}. {title}.</b><br>{caption}</p>""")
               )
        self.table_num += 1
    
    def reset_to(self, fig_num=None, table_num=None):
        """Manually reset figure number or table number."""
        if fig_num is not None:
            self.fig_num = fig_num
        if table_num is not None:
            self.table_num = table_num