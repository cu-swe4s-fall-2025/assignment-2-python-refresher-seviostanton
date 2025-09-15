import my_utils
import argparse
import sys

def parse_args():
    p = argparse.ArgumentParser(prog="print_fires",
                                description="Print values from a CSV column "
                                            "for rows matching a country."
                                )
    p.add_argument("--file_name", required=True,
                   help="Path to CSV data file")
    p.add_argument("--country", required=True,
                   help="Country name to filter on "
                        "(e.g. 'United States of America')")
    p.add_argument("--country_column", type=int, required=True,
                   help="Index of the country column (default=0)")
    p.add_argument("--fires_column", type=int, required=True,
                   help="Index of the fire column "
                        "(e.g. 2 for savanna fires)")
    return p.parse_args()

def main():
    args = parse_args()

    try:
        fires = my_utils.get_column(file_name=args.file_name,
                                    query_column=args.country_column,
                                    query_value=args.country,
                                    result_column=args.fires_column)
    except FileNotFoundError as e:
        sys.stderr.write(f"Error: File not found: ",
                         f"{args.file_name}.\n {e}\n")
        return 1
    except IndexError as e:
        sys.stderr.write(f"Error: Column not found: ",
                         f"{args.fires_column}.\n {e}\n")
        return 2
    except IndexError as e:
        sys.stderr.write(f"Error: Column not found: ",
                         f"{args.country_column}.\n {e}\n")
        return 2

    print(f"Values from column {args.fires_column} for {args.country}: {fires}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
