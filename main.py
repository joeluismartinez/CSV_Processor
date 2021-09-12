
from modules import *
import pandas as pd
import os
import glob

SCHEMA_TARGET = "Homework_-_Target_Schema.csv"

path = os.getcwd()
csv_files = glob.glob(os.path.join(path, "csv_ingest/*.csv"))

# Read in schema data
schema = pd.read_csv(SCHEMA_TARGET)

# sort columns based on schema order
schema_cols = list(schema.columns.values)
schema_types = pd.read_csv(SCHEMA_TARGET, usecols=schema_cols, sep=',')

# combine and process csv files or raise exception. 
results = combine_files(csv_files)

# Log out columns not in schema
columns_not_in_schema = results.columns.difference(schema.columns.values)

# If columns in not in schema do not exists print message else log out incorrect schemas.
schema_column_check(columns_not_in_schema, results)
   
# sorting by correct column order outlined in schema
results = results[schema_cols]

# store missing data
missing = results[schema_cols].isnull().any(axis=1)

# If missing data does not exist print message else log out blank fields.
missing_values_check(missing, results)

# Strip out blank data
results = results.dropna()

# Cast to correct datatype
final_results = cast_datatypes(results, schema_cols)

# Datatype check and log out before final CSV processing.
print(f"Datatype check:\n\n{final_results.dtypes}\n")
print(f"Final output before write:\n\n{final_results}\n")
final_results.to_csv('results.csv')