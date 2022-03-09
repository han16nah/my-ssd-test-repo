import pytest
import pandas as pd
import numpy as np
from oop_analysis import in_out, analysis


@pytest.mark.in_out
@pytest.mark.parametetrize("first_row_first_val", "len_df", [(0.0, 101), (0.0, 101)])
# @pytest.mark.skip(reason="Already using unittest")
def test_read_csv_as_df(len_df, first_row_first_val):
    """Test reading a csv file into a dataframe"""

    # given
    file_in = r"J:\01_Projekte\SSC_Workshop\my-ssd-test-repo\data\expec.t"

    # expected
    input_obj = in_out()
    df = input_obj.read_csv_as_df(file_in)

    # check if length of dataframe is as expected
    assert (len(df.index) == len_df) is True

    # check if first value in first column is as expected
    row_1 = df.iloc[0]
    print(row_1)

    assert (row_1[0] == first_row_first_val) is True


def test_create_corr_matrix():
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
    np.testing.assert_array_equal(ser_r, r_exp)


# TODO: Test the rm_col option of get_corr()


if __name__ == "__main__":
    pytest.main()
