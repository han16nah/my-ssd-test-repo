import unittest
import pandas as pd
import numpy as np
from oop_analysis import analysis


class test_create_corr_matrix(unittest.TestCase):
    def test_create_corr_matrix(self):
        # given
        d = {"col1": [1, 2, 3], "col2": [3, 2, 1], "col3": [1, 2, 3]}
        df = pd.DataFrame(data=d)

        # expected
        r_exp = np.array(
            [
                -1.0,  # between 'col1' and 'col2'
                -1.0,  # between 'col2' and 'col3'
                1.0,  # between 'col1' and 'col3'
            ]
        )

        obj = analysis(df)
        obj.df_filtered = df
        ser_r = obj.get_corr()
        self.assertTrue(np.array_equal(ser_r, r_exp))

    # TODO: Test the rm_col option of get_corr()
