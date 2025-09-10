import my_utils
import argparse


def main():
    parser = argparse.ArgumentParser(prog="print_fires",
                                     description="Print number of fires "
                                     "in a specified country.")
    parser.add_argument("--file",
                        help="Path to CSV data file")
    parser.add_argument("--country_name", required=True,
                        help="Country to filter on "
                        "(e.g. 'United States of America')")
    parser.add_argument("--country_column", type=int, required=True,
                        help="Index of the country column (default=0)")
    parser.add_argument("--fires_column", type=int, required=True,
                        help="Index of the fire column "
                        "(e.g. 2 for savanna fires)")

    # from ArgumentParser documentation
    # -> The ArgumentParser.parse_args() method runs the parser and places the
    # -> extracted data in a argparse.Namespace object:
    args = parser.parse_args()

    fires = my_utils.get_column(file_name=args.file,
                                query_column=args.country_column,
                                query_value=args.country_name,
                                result_column=args.fires_column)
    print(f'Savanna fires in the US: {fires}')


if __name__ == "__main__":
    main()
