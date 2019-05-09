import csv
import sys
import os
from pathlib import Path
sys.path.append(os.getcwd())


def read_from_csv(csv_path) -> list:
    """Reads csv data and return list from given csv path value."""
    try:
        exact_csv_path = get_resource_path(csv_path)
        with open(exact_csv_path, 'r') as f:
            reader = csv.reader(f)
            csv_list = list(reader)
        return csv_list
    except FileNotFoundError as file_exception:
        print(file_exception)


def write_to_csv(csv_path, csv_data):
    """Writes the list data row to csv file. *Note*: csv_data param should be list."""
    try:
        exact_csv_path = get_resource_path(csv_path)
        with open(exact_csv_path, mode='a', newline='') as users_file:
            users_writer = csv.writer(users_file, delimiter=',', quotechar='"',
                                      quoting=csv.QUOTE_MINIMAL)
            users_writer.writerow(csv_data)
    except FileNotFoundError as file_exception:
        print(file_exception)
    except Exception as exception:
        print("Unexpected error raised. See: {}".format(exception))


def get_resource_path(csv_path):
    """ This function returns the actual path of csv. In project structure,
    resource folder is in the other directory. This method is a necessary to receive resource path."""
    exact_path = str(Path(os.getcwd()).parent) + '/' + csv_path
    return exact_path
