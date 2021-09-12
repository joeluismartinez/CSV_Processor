import pandas as pd

def combine_files(csv_files=0):
    ''' Takes CSV files argument to be processed by pandas concat. Returns results, if no CSV supplied will
       raise exception and halt process. '''
    try:
        results = pd.concat((pd.read_csv(file).replace('"','', regex=True) for file in csv_files), ignore_index = True)
        return results
    except ValueError:
        print("No CSV data supplied. Please make sure csv_ingest directory is loaded with CSV's")
        exit()


def schema_column_check(columns_not_in_schema=0, results=0):
    ''' Takes columns_not_in_schema arg and results arg and prints out if column outside of schema exists. '''
    if columns_not_in_schema.values[0] == 'Unnamed: 0':
        print("No columns outside of schema\n")
    else :
        print(f"\nError columns not in schema:\n\n{results[columns_not_in_schema]} \n")


def missing_values_check(missing=0, results=0):
    ''' Takes missing and results arg and prints out if blank data exists in dataframe. '''
    if  missing.values.any() == True:
        print(f"Error! offending rows do not meet specificaitons:\n\n{results.loc[missing]}\n")
    else:
        print("No missing data detected.\n")


def cast_datatypes(results, schema_cols):
    ''' Take results and schema_cols arguments and cast it to correct data types and returns it out '''
    results[schema_cols] = results[schema_cols].astype(str)
    results["Cost Per Ad Click"] = results["Cost Per Ad Click"].astype(float)
    return results
