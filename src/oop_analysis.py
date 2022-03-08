import pandas as pd
# import numpy as np
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
    def read_csv(self, file_in):
        return self.df_name

    def write_to_csv(self, file_out):
        pass


class analysis:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.df_clean = None

    def filter_columns_by_variance(self, threshold: float):
        """
        Filter dataframe by variance threshold.
        :param threshold: Filter value to surpass for columns to be considered further.
        :return: Dataframe cleaned of columns with a small variance.
        """
        df_clean = self.df.loc[:, (self.df.var() >= threshold)]
        return df_clean

    def create_corr_matrix(self):
        return  # sorted r2 values as pandas sequence

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
