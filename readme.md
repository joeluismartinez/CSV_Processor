# What does this program do?

This program will take csv files staged in the csv_ingest directory. 
Once desired csv files are in the csv_ingest directory, the script 
can be run to grab the csv files and merge them into on dataframe to 
be processed. 

If the processed csv files do not match the schema type columns they will 
be printed out and discarded. 

If the processed csv files contain any row with blanks they will be printed out
and discarded from the dataframe.

In the root directory there is a target schema. Right now the code works
for a specific schema and datatypes cast, but can be expanded in the future 
to receive any schema csv file and update datatype casts accordingly.

# Requirements
This script uses Python 3.9.7 and
Pandas and Pytest are required to run the scripts and test:

- https://pandas.pydata.org/docs/getting_started/install.html
- https://docs.pytest.org/en/6.2.x/getting-started.html

# How to get started 

Once pandas and pytest is install you can run the script with 
the following command below:

- python3 main.py

After the script completes we should see a clean and merged 
CSV titled results.csv

# Testing

This program comes with tests to ensure this code is working correctly.
The tests are stored in test_main.py. The test ensure proper columns found
in schema are used, final_results adhere to the schema columns, proper datatypes
are found in the final_results before writing to CSV, and that the combine files
function is working correctly.

Test can be run with the following command:

- pytest or python3 -m pytest

Expected outputs will be passes or failures
