import os
import requests
import gzip
import input
from io import BytesIO

def download_and_unzip_data(start_year, end_year):
    base_url = "http://data.cquest.org/meteo-france/synop/synop.{}.csv.gz"
    os.makedirs('data', exist_ok=True)  # Ensure the 'data' directory exists
    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            date_str = f"{year}{month:02d}"
            file_path = os.path.join('data', f"synop.{date_str}.csv")
            if not os.path.exists(file_path):
                url = base_url.format(date_str)
                response = requests.get(url)
                if response.status_code == 200:
                    compressed_file = BytesIO(response.content)
                    decompressed_file = gzip.GzipFile(fileobj=compressed_file)
                    with open(file_path, 'wb') as outfile:
                        outfile.write(decompressed_file.read())
                else:
                    print(f"Failed to download data for {date_str}")
            else:
                print(f"File for {date_str} already exists, skipping download.")

download_and_unzip_data(input.START_YEAR, input.END_YEAR)