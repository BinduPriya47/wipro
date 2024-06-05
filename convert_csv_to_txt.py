import pandas as pd # type: ignore

def convert_csv_to_piped(input_file, output_file):
    # Read the CSV file
    df = pd.read_csv(input_file)

    # Write to a pipe-delimited text file
    df.to_csv(output_file, sep='|', index=False)

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python convert_csv_to_piped.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_csv_to_piped(input_file, output_file)
        print(f"Converted {input_file} to pipe-delimited file {output_file}")
