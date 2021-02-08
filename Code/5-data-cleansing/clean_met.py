"""
Dataset: MetObjects_sample.csv - from https://github.com/metmuseum/openaccess/
The Metropolitan Museum of Art dataset cleansing
"""
import re
import sys

import numpy as np
import pandas as pd

from utils import *

sys.path.insert(1, ".")

logger("5-data-cleansing/clean_met.log")


def main():
    data = read_data()
    nulls_info(data)
    data = clean_date(data)
    data = clean_year(data)
    data = clean_gender(data)

    logging.info(f" Finished ".center(30, "*"))


def read_data(location="Data/MetObjects_sample.csv"):
    """
    Loads data file from location, and loads it into a pandas data frame.
    Print same basic information.
    Returns DF
    """
    data = pd.read_csv(
        location,
        delimiter=",",
    )

    logging.info(" Met Dataset ".center(30, "="))
    logging.info(data.head(10))

    filas, columnas = data.shape
    logging.info(f"\nDataset has {filas} rows and {columnas} columns\n")
    return data


def nulls_info(data):
    """
    Print total number of nulls by columns, and percentage of each column.
    """
    logging.info(" Null Columns ".center(30, "="))

    nulls = pd.DataFrame(
        [data.isnull().sum(), data.isnull().mean()],
        index=["Total", "Percentage"])

    logging.info(nulls.T)


def column_info(data, column):
    """
    Print information about a column within the dataset
    """
    logging.info(f" {column} Columns ".center(30, "="))

    logging.info(data[column].value_counts())
    logging.info(f"\nUnique values {len(data[column].unique())}\n")
    logging.info(f"Null values {data[column].isnull().sum()}\n")


def clean_date(data):
    """
    Clean Object Date column using Regex
    """
    column_info(data, "Object Date")

    year_pattern = "(\d){3,4}"
    year_pattern_regex = re.compile(year_pattern)

    data_year_mo = data["Object Date"].apply(lambda x: x if x is np.NaN else
                                             year_pattern_regex.search(x))

    data["Object Date Clean"] = data_year_mo.apply(lambda x: x if x is None or
                                                   x is np.NaN else x.group(0))

    data_dates = data[["Object Date", "Object Date Clean"]]

    logging.info(data_dates)

    century_pattern = "(?P<century>\d\d)(th (C|c)entury)"
    century_pattern_regex = re.compile(century_pattern)

    data_century_match = data_dates.apply(
        lambda x: x["Object Date Clean"] if x["Object Date Clean"] is not None
        else x["Object Date"] if x["Object Date"] is np.NaN else
        century_pattern_regex.search(x["Object Date"]),
        axis=1,
    )

    data["Object Date Clean"] = data_century_match.apply(
        lambda x: x if isinstance(x, (str, type(None), type(np.NaN))) else (
            int(x.group("century")) - 1) * 100)

    logging.info(data[["Object Date", "Object Date Clean"]])

    data["Object Date Clean"] = data.apply(lambda x: 0 if x["Object Date"] is
                                           np.NaN else x["Object Date Clean"],
                                           axis=1)
    logging.info(data[["Object Date", "Object Date Clean"]])

    logging.info(data.loc[data["Object Date Clean"].isnull(
    ), ["Object Date", "Object Date Clean"]])

    column_info(data, "Object Date")
    column_info(data, "Object Date Clean")
    return data


def clean_year(data):
    """
    Clean Accession Year column using Regex
    """
    column_info(data, "AccessionYear")

    pattern_fecha = "(?P<year>\d\d\d\d)(?P<month_day>\-\d\d\-\d\d)*"
    pattern_fecha_regex = re.compile(pattern_fecha)
    # resultado_fechas = data.AccessionYear.apply(lambda x: x if (x is np.NaN) | (x is None) else pattern_fecha_regex.match(x))
    resultado_fechas = data.AccessionYear.apply(lambda x: x if x is np.NaN else
                                                pattern_fecha_regex.match(x))

    year_match = resultado_fechas.apply(lambda x: x
                                        if x is np.NaN else x.group("year"))
    logging.info(year_match.dtype)

    year_match_fill = year_match.fillna(0)
    year_match_fill_numeric = year_match_fill.astype(int)

    data["AccessionYearClean"] = year_match_fill_numeric
    data.dtypes

    column_info(data, "AccessionYearClean")
    return data


def clean_gender(data):
    """
    Clean Artist Gender column using Regex
    """
    column_info(data, "Artist Gender")

    # Assign Unknowk to all null values
    data["ArtistGenderClean"] = data["Artist Gender"].fillna("Unknown")

    # Clean up Pipes
    pattern_pipes = "\|+"
    pattern_pipes_regex = re.compile(pattern_pipes)
    cadena_reemplazo = ""
    data["ArtistGenderClean"] = data["ArtistGenderClean"].apply(
        lambda x: pattern_pipes_regex.sub(cadena_reemplazo, x))
    data["ArtistGenderClean"].value_counts()

    # replace multiple instances of Female by one Female
    pattern_female = "(Female)+"
    pattern_female_regex = re.compile(pattern_female)
    cadena_reemplazo = "Female"
    data["ArtistGenderClean"] = data["ArtistGenderClean"].apply(
        lambda x: pattern_female_regex.sub(cadena_reemplazo, x))
    data["ArtistGenderClean"].value_counts()

    # replace empty values by Male
    empty_mask = data["ArtistGenderClean"] == ""
    data.loc[empty_mask, "ArtistGenderClean"] = "Male"
    data["ArtistGenderClean"].value_counts()

    column_info(data, "ArtistGenderClean")


if __name__ == "__main__":
    main()
