"""
A program to analyze json files containing job postings,
normalize the data, and create an SQLite database populated with
that data
"""
from database_management import create_database, populate_database
from file_management import normalize_file
from key_comparison import compare_keys

FILES = [
    "rapid_jobs2.json",
    "rapid_results.json"
]

NORMALIZED_FILES = []

DATABASE_PATH = "job_listings.db"


if __name__ == "__main__":

    for file in FILES:
        NORMALIZED_FILES.append(normalize_file(file))

    # Prints shared and unique keys after initial normalization
    # Can be used for further comparison and normalization of data
    compare_keys(NORMALIZED_FILES)

    create_database(DATABASE_PATH)
    populate_database(DATABASE_PATH, NORMALIZED_FILES)
