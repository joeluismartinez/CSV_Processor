
from main import *
from modules import *
from pandas._testing import assert_frame_equal
import numpy as np

def test_schema_columns():
    ''' asserts schema columns that are pulled from file are correct '''
    assert schema_cols == ['Provider Name', 'CampaignID', 'Cost Per Ad Click',\
         'Redirect Link', 'Phone Number', 'Address', 'Zipcode']


def test_results_columns_equal_to_schema():
    ''' assers final results columns is equal to schema columns '''
    final_columns = final_results.columns.values.tolist()
    assert final_columns == schema_cols


def test_results_string_datatype():
     ''' test dataframe matches expected schema datatypes for strings before write out '''
     assert final_results.dtypes['Provider Name'] == pd.StringDtype
     assert final_results.dtypes['CampaignID'] == pd.StringDtype
     assert final_results.dtypes['Redirect Link'] == pd.StringDtype
     assert final_results.dtypes['Phone Number'] == pd.StringDtype
     assert final_results.dtypes['Address'] == pd.StringDtype
     assert final_results.dtypes['Zipcode'] == pd.StringDtype


def test_results_float64_datatype():
     ''' test dataframe matches expected schema datatype for float64 before write out '''
     assert final_results.dtypes['Cost Per Ad Click'] == np.float64


def test_combine_files():
     ''' test combine files function returns the correct value '''
     test_results = pd.concat((pd.read_csv(file).replace('"','', regex=True) for file in csv_files), ignore_index = True)
     assert_frame_equal(combine_files(csv_files), test_results)