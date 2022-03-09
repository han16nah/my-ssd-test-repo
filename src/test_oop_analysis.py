import unittest
from oop_analysis import in_out
import pandas as pd
import numpy as np
from oop_analysis import analysis

class test_in_out(unittest.TestCase):
    def test_read_csv_as_df(self):

        # given
        file_in = r"J:\01_Projekte\SSC_Workshop\my-ssd-test-repo\data\expec.t"

        # expected
        input_table = in_out()
        input_table.df = file_in
        df = input_table.read_csv_as_df(input_table.df, "    ")
        len_df = 101
        first_row_first_val = "0.2"

        # check if length of dataframe is as expected
        self.assertTrue(len(df.index) == len_df)

        # check if first value in first column is as expected
        self.assertTrue(df.iloc[0][0:2] == first_row_first_val)


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

