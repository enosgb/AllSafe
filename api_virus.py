from __future__ import print_function
import time
import cloudmersive_virus_api_client
from cloudmersive_virus_api_client.rest import ApiException
from pprint import pprint

def scanningFile(filepath):
    # Configure API key authorization: Apikey
    configuration = cloudmersive_virus_api_client.Configuration()

    # ----- API KEY
    configuration.api_key['Apikey'] = '59b1bcd2-0c92-4a90-8c64-26c128639bf0'



    # create an instance of the API class
    api_instance = cloudmersive_virus_api_client.ScanApi(cloudmersive_virus_api_client.ApiClient(configuration))
    #input_file = 'C:\\Users\\Enos\\Downloads\\vtex.json' # file | Input file to perform the operation on.
    input_file = filepath

    try:
        # Scan a file for viruses
        api_response = api_instance.scan_file(input_file)
        pprint(input_file)
        pprint(api_response)
        return(api_response.clean_result)
    except ApiException as e:
        print("Exception when calling ScanApi->scan_file: %s\n" % e)
