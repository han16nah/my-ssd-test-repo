import pandas as pd
import numpy as np
import time
import sys

# import getopt
# import matplotlib.pyplot as plt
# import seaborn as sns
# sns.set_theme(style="darkgrid")


##############################################################
#                    helper functions                        #
##############################################################


##############################################################
#                    main function                           #
##############################################################


def main(argv):
    """
    Args:

        argv (list, required): user input
    """

    """
    # get user input instead of hardcoding all inputs
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["file_in=", "col_sep=",
                                                   "skip_init_space=",
                                                   "file_out=" "header="])

    # option to check usage of script
    except getopt.GetoptError:
        print('oop_analysis.py -file_in <file_in> -col_sep <col_sep> '
              '-file_out <file_out> -skip_init_space <skip_init_space> '
              '-header_outfile <header_outfile')
        sys.exit(2)

    # store user input as var
    for opt, arg in opts:
        if opt == '-h':
            print('oop_analysis.py -i <file_in>')
            sys.exit()
        elif opt in ("-file_in", "--file_in"):
            file_in = arg
            print('file_in is "', file_in)
        elif opt in ("-col_sep", "--col_sep"):
            col_sep = arg
            print('col_sep is "', col_sep)
        elif opt in ("-skip_init_space", "--skip_init_space"):
            skip_init_space = arg
            print('skip_init_space "', skip_init_space)
        elif opt in ("-file_out", "--file_out"):
            file_out = arg
            print('file_out is"', file_out)
        elif opt in ("-header_outfile", "--header_outfile"):
            header_outfile = arg
            print('header_outfile is"', header_outfile)

    """


##############################################################
#                    main classes                            #
##############################################################


class in_out:
    def __init__(
        self,
        df: str = None,
        np_array: str = None,
        file_out: str = None,
        table: str = None,
    ):
        self.df = df
        self.np_array = np_array
        self.file_out = file_out
        self.table = table

        """
        Args:
            df (str, optional): Dataframe.
                Defauts to None.
            np_array (str, optional): name of np array.
                Defaults to None.
            file_out (str, optional): path to output file.
                Defaults to None.
            table (str, optional): path to table file.
                Defaults to None.

        """

    # read csv file into dataframe
    def read_csv_as_df(
        self,
        file_in: str = None,
        col_separator: str = ",",
        skip_initial_space: bool = True,
    ):
        """Method to read csv file into dataframe

        Args:
            file_in (str, optional): Path to input file.
                Defaults to None.
            col_separator (str, optional): Column separator of input file.
                Defaults to ",".
            skip_initial_space (bool, optional): Indicator if initial space
            should be skipped.
                Defaults to True.

        Returns:
            self.df: Generated dataframe

        """

        self.df = pd.read_csv(
            file_in, sep=col_separator, skipinitialspace=skip_initial_space
        )

    # read csv file as numpy array
    def read_csv_as_np_array(self, file_in: str = None):
        """Method to read csv file into numpy array

        Args:
            file_in (str, optional): input file
                Defaults to None.

        Returns:
            self.table: Generated numpy array

        """

        self.table = np.loadtxt(file_in, skiprows=True)

    # write dataframe to csv file
    def write_df_to_csv(self, file_out: str = None, header: bool = True):
        """Method to write dataframe into csv file
        Args:

            file_out (str, optional): Path to output file.
                Defaults to None.
            header (bool, optional): Indicator if header shall be stored.
                Defaults to True.

        Returns:
            file_out: Path to output csv file.

        """
        self.file_out = self.df.to_csv(file_out, header=header)


class analysis:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.df_clean = None
        self.eudlid_dist = []

    def filter_columns_by_variance(self, threshold: float):
        """
        Filter dataframe by variance threshold.
        Args:
            threshold: Filter value to surpass for columns to be considered further.
        Returns:
            Dataframe cleaned of columns with a small variance.

        """
        self.df_clean = self.df.loc[:, (self.df.var() >= threshold)]
        return self.df_clean

    def get_corr(self, rm_col: str = None) -> pd.Series:
        """Function to compute the correlation coefficients (Pearson'r R)
        between values in a data frame.
        Optionally, a single column can be removed.
        The output contains no redundant correlation values
        and is sorted ascending.

        Args:
            rm_col (str, optional): Name of column in the data frame to remove.
                Defaults to None.

        Returns:
            pd.Series: Sorted Series of Pearson's Correlation Coefficient

        """

        # correlation matrix
        corr_mat = self.df_filtered.corr()

        # get only upper triangle without diagonal
        corr_mat_ut = corr_mat.where((np.triu(np.ones(corr_mat.shape), 1).astype(bool)))

        # remove column (if one is specified)
        if rm_col is not None:
            corr_mat_ut.pop(rm_col)

        # sort ascending
        sorted_r = corr_mat_ut.unstack().dropna().sort_values()

        return sorted_r

    # calculate euclidean distance
    def calc_euclidean_dist(self, col_a: int = None, col_b: int = None):
        """Method to calculate euclidean distance between two vectors

        Args:
            col_a (int, optional): Index of column a.
                Defaults to None.
            col_b (int, optional): Index of column b.
                Defaults to None.

        Returns:
            self.euclid_dist: eudlidean distance between two columns

        """

        # using loadtxt, bc nan_to_num did not work with np.genfromtxt()
        table = np.nan_to_num(self.table)

        # calculate euclidean distance between vectors of different columns
        self.eudlid_dist = np.sqrt((table[:, col_a] - table[:, col_b]) ** 2)

    def fourier_trafo(self):
        """
        Perform Fourier transform.

        Returns:
            Fourier transform and frequency

        """
        fft = np.fft.fft(self.np[1:, 1].astype("float64"))
        fftfreq = np.fft.fftfreq(fft.size, 0.1)
        return fft, fftfreq


##############################################################
#                                                            #
##############################################################

if __name__ == "__main__":
    start = time.time()
    main(sys.argv[1:])
    end = time.time()
    print("Runtime: %.3fs" % (end - start))
    sys.exit()
