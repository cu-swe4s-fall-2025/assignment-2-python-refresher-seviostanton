import my_utils
import argparse
import sys

"""
print_fires.py

Command-line tool that reads a CSV and prints values from a specified
column for rows matching a given country.
Implements best practices: argparse, main(), stderr for errors, exit codes.
"""


def parse_args():
    """
    Set up and parse command-line arguments.

    Returns:
        argparse.Namespace: parsed arguments with attributes:
            - file_name (str): path to CSV file
            - country (str): country name to filter on
            - country_column (int): index of country column
            - fires_column (int): index of fires (numeric) column
    """

    p = argparse.ArgumentParser(prog="print_fires",
                                description="Print values from a CSV column "
                                            "for rows matching a country.")
    # Path to the input CSV file
    p.add_argument("--file_name", required=True,
                   help="Path to CSV data file")
    # Country to filter rows by
    p.add_argument("--country", required=True,
                   help="Country name to filter on "
                        "(e.g. 'United States of America')")
    # Column index containing country names
    p.add_argument("--country_column", type=int, required=True,
                   help="Index of the country column (default=0)")
    # Column index containing fire counts
    p.add_argument("--fires_column", type=int, required=True,
                   help="Index of the fire column "
                        "(e.g. 2 for savanna fires)")
    # Optional operation to perform on the fire counts
    p.add_argument("--operation", choices=["sum", "mean", "std"],
                   default=None,
                   help="If provided: Operation to perform on the fire counts")
    return p.parse_args()


def main():
    """
    Main program logic:
      - Parse command line arguments
      - Call my_utils.get_column to extract values
      - Handle errors cleanly with stderr & exit codes
      - Print matching values to stdout on success

    Returns:
        int: exit code (0 = success, 1 = file error, 2 = column/value error)
    """
    args = parse_args()

    try:
        fires = my_utils.get_column(file_name=args.file_name,
                                    query_column=args.country_column,
                                    query_value=args.country,
                                    result_column=args.fires_column)
    except FileNotFoundError as e:
        # Handle missing file
        sys.stderr.write(f"Error: File not found: ",
                         f"{args.file_name}.\n {e}\n")
        return 1
    except IndexError as e:
        # Handle bad column indices
        sys.stderr.write(f"Error: Column not found: ",
                         f"{args.fires_column}.\n {e}\n")
        return 2
    except IndexError as e:
        # Handle bad country column indices
        sys.stderr.write(f"Error: Column not found: ",
                         f"{args.country_column}.\n {e}\n")
        return 2

    if args.operation:
        try:
            if args.operation == "sum":
                result = my_utils.sum_ints(fires)
            elif args.operation == "mean":
                result = my_utils.mean_ints(fires)
            elif args.operation == "std":
                result = my_utils.std_ints(fires)
            print(f"{args.operation} of values from column "
                  f"{args.fires_column} for {args.country}: {result}")
            return 0
        except ValueError as e:
            sys.stderr.write(f"Error: Could not perform operation ",
                             f"{args.operation} on values from column ",
                             f"{args.fires_column} for"
                             f"{args.country}.\n {e}\n")
            return 2

    if args.operation is None:
        # On success, print list of integer values
        print(f"Values from column {args.fires_column} for {args.country}:",
              f"{fires}")
        return 0


if __name__ == "__main__":
    # Execute the main program logic
    # and pass the exit code
    raise SystemExit(main())
