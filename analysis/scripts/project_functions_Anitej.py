import pandas as pd
import csv
import chardet

def load_and_process(dataframe_path, service_name, columns_to_drop=[]):
    # Load data
    df = (
        pd.read_csv(dataframe_path)
    )

    # Check file properties
    file_type = "File Type: " + type(df).__name__
    encoding = "Encoding: " + chardet.detect(open(dataframe_path, 'rb').read())['encoding']
    delimiter = "Delimiter: " + csv.Sniffer().sniff(open(dataframe_path).read(1024)).delimiter
    print(f"{service_name} {file_type}, {encoding}, {delimiter}")

    # Clean data
    df = (
        df.drop(columns=columns_to_drop)
    )

    # Process data
    df = (
        df.assign(listed_in_count=lambda x: x.iloc[:, -1].str.count(",") + 1)
    )

    # Wrangle data
    df['date_added'] = pd.to_datetime(df['date_added'])

    # Save data
    df.to_csv(f"../data/processed/{service_name}/{service_name}_analysisPipeline.csv", index=False)

    return df