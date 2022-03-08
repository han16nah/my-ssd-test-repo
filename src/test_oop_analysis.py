import unittest
from oop_analysis import in_out


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
