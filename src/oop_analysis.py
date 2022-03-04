import pandas as pd
import numpy as np

# import matplotlib.pyplot as plt
# import seaborn as sns
import time
import sys

# sns.set_theme(style="darkgrid")


##############################################################
#                    helper functions                        #
##############################################################


def df_to_np_array():
    pass


def create_plot(x_col, y_col, file_out):
    # plot and save as pdf
    pass


##############################################################
#                    main function                           #
##############################################################
def main(argv):
    pass


##############################################################
#                    main classes                            #
##############################################################


class in_out:
    def __init__(self, df_name: str):
        self.df_name = df_name

    """
    :param str : df_name : name of df
    """
    # import data into df
    def read_csv(self, file_in: str):
        return self.df_name

    def write_to_csv(self, file_out: str):
        pass


class analysis:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.df_filtered = None

    def filter_columns_by_variance(self, treshold):
        return self.df_filtered

    def create_corr_matrix(self, rm_col: str = None):

        # correlation matrix
        r = self.df_filtered.corr()

        # get only upper triangle without diagonal
        r_ut = r.where((np.triu(np.ones(r.shape)).astype(bool)) & (r != 1.0))
        if rm_col is not None:
            r_ut.pop(rm_col)

        # sort
        sorted_r = r_ut.unstack().dropna().sort_values()

        return sorted_r

    def calc_euclidean_dist(self):
        return

    def fourier_trafo(self):
        pass


##############################################################
#                                                            #
##############################################################

if __name__ == "__main__":
    start = time.time()
    pass
    end = time.time()
    print("Runtime: %.3fs" % (end - start))
    sys.exit()
