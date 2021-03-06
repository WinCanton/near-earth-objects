"""Extract neos and close approaches data from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the
command line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth
    objects.
    :return: A collection of `NearEarthObject`s.
    """
    with open(neo_csv_path, 'r') as f:
        reader = csv.DictReader(f)
        neo_data = []
        for item in reader:
            info = {k: v for k, v in item.items()
                    if k in ['pdes', 'name', 'diameter', 'pha']}
            neo_data.append(NearEarthObject(**info))
    return neo_data


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close
    approaches.
    :return: A collection of `CloseApproach`es.
    """
    with open(cad_json_path, 'r') as f:
        reader = json.load(f)
        data = reader['data']
        ca_data = []
        for item in data:
            info = {"des": item[0], "cd": item[3],
                    "dist": item[4], "v_rel": item[7]}
            ca_data.append(CloseApproach(**info))
    return ca_data
