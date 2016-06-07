import pandas as pd
import glob
import argparse
import os
import fnmatch

# If you are uncomfortable with the command line, set use_default_args to True and change the values for the flags in
# my_args and run script without arguments.
# Default values with no args: {'r': False, 'e': False, 'l': False, 'w': '*.csv', 'f': None}
use_default_args = False
my_args = {'r': False, 'e': False, 'l': False, 'w': '*.csv', 'f': None}


def create_parser():
    my_parser = argparse.ArgumentParser(description='Remove specified columns from CSV')
    my_parser.add_argument('-f', help='File name of file with columns to remove (File must have one column per line)')
    my_parser.add_argument('-w', default="*.csv", help='Wildcard for which files to use. default: "*.csv"')
    my_parser.add_argument('-e', action='store_true', help='Drop all empty columns')
    my_parser.add_argument('-l', action='store_true', help='Drop last column if it\'s empty and has no column name')
    my_parser.add_argument('-r', action='store_true',
                           help='Recursively search for files starting from current directory')
    return my_parser


def remove_specified_columns(file_name, my_df):
    print file_name


def drop_empty_columns(my_df):
    print my_df


def drop_empty_last_column(my_df):
    print my_df


if __name__ == '__main__':
    parser = create_parser()
    args = vars(parser.parse_args())

    if use_default_args:
        args = my_args
    print args

    for root, dirnames, filenames in os.walk('.'):
        for filename in fnmatch.filter(filenames, '*.csv'):
            csv_path = os.path.join(root, filename)
            if args['f']:
                remove_specified_columns(args['f'], "data_frame_here")
            if args['e']:
                drop_empty_columns("data_frame_here")
            elif args['l']:  # Only attempt if -e is not called
                drop_empty_last_column("data_frame_here")
            if args['r']:
                pass
            if args['w']:
                pass


# # SOME CSV FILE GENERATORS WILL CREATE AN ADDITIONAL COLUMN WITH NO VALUES.
# # SET BOTTOM VARIABLE (DROP_EMPTY_LAST_COLUMN) TO TRUE IF YOU WOULD LIKE TO REMOVE THE LAST COLUMN IF EVERY VALUE IS
# # EMPTY AND THE THERE IS NO HEADER FOR THAT COLUMN.
# DROP_EMPTY_LAST_COLUMN = False
#
# columns_file = open('columns_to_remove.txt', 'r')
# columns_list = columns_file.readlines()
# columns_file.close()
#
# csv_list = glob.glob('*.csv')
#
# for csv in csv_list:
#     df = pd.read_csv(csv)
#
#     # If user opted True for deleting last col: drop last column if all values are empty and column has no header
#     if DROP_EMPTY_LAST_COLUMN and len(df) > 0:
#         last_col = df.columns.values[-1]
#         if 'Unnamed' in last_col and df[last_col].isnull().all():
#             df.drop(last_col, axis=1, inplace=True)
#
#     # Drop all columns from the list of columns if they exist in the table
#     for column in columns_list:
#         column = column.strip()
#         if column in df.columns:
#             df.drop(column, axis=1, inplace=True)
#
#     df.to_csv(csv, index=False)
