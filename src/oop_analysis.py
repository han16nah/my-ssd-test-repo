import pandas as pd

# import getopt
import numpy as np

# import matplotlib.pyplot as plt
# import seaborn as sns
import time
import sys


# sns.set_theme(style="darkgrid")


##############################################################
#                    helper functions                        #
##############################################################


##############################################################
#                    main function                           #
##############################################################
def main(argv):
    """

    :param argv: user input
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
    def __init__(self, df_name: str):
        self.df_name = df_name
        self.np_array_name = ""
        self.file_out = ""
        self.table_name = None

        """
        :param str df_name : name of df
        :param str file_out : path to output file
        :param str np_array_name : name of np array
        """

    # read csv file into dataframe
    def read_csv_as_df(self, file_in, col_separator, skip_initial_space):
        """

        Method to read csv file into dataframe

        :param str file_in : path to input file
        :param str col_separator : column separator
        :param bool skip_initial_space : indicator if initial space should be
        skipped

        :return self.df_name : name of generated dataframe
        """

        self.df_name = pd.read_csv(
            file_in, sep=col_separator, skipinitialspace=skip_initial_space
        )

    # read csv file as numpy array
    def read_csv_as_np_array(self, file_in, skip_rows):
        """
        Method to read csv file into numpy array

        :param skip_rows:
        :param str file_in: input file

        :return self.table_name : name of generated numpy array

        """

        self.table_name = np.loadtxt(file_in, skiprows=skip_rows)

    # write dataframe to csv file
    def write_df_to_csv(self, df, file_out, header):
        """
        Method to write dataframe into csv file

        :param df: dataframe to be written to csv
        :param bool header: indicator if header shall be stored
        :param str file_out : path to output file

        :return file_out : path to output csv file
        """
        self.file_out = df.to_csv(file_out, header=header)


class analysis:
    def __init__(self, df: str, table_name: str):
        self.table = None
        self.df = df
        self.df_filtered = None
        self.table_name = table_name
        self.eudlid_dist = []

    def filter_columns_by_variance(self, treshold):
        return self.df_filtered

    def create_corr_matrix(self):
        return  # sorted r2 values as pandas sequence

    # calculate euclidean distance
    def calc_euclidean_dist(self, col_a, col_b):
        """

        Method to calculate euclidean distance between two vectors

        :param col_a: index of column a
        :param col_b: index of column b

        :return self.euclid_dist : eudlidean distance between two columns
        """

        # using loadtxt, bc nan_to_num did not work with np.genfromtxt()
        tab = np.nan_to_num(self.table)

        # calculate euclidean distance
        euclid_dist = np.sqrt((col_a - col_b) ** 2)

        # calculate euclidean distance between vectors of different columns
        self.eudlid_dist = euclid_dist(tab[:, col_a], tab[:, col_b])

    def fourier_trafo(self):
        pass


##############################################################
#                                                            #
##############################################################

if __name__ == "__main__":
    start = time.time()
    main(sys.argv[1:])
    end = time.time()
    print("Runtime: %.3fs" % (end - start))
    sys.exit()
