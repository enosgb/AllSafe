from __future__ import print_function
import time
import cloudmersive_virus_api_client
from cloudmersive_virus_api_client.rest import ApiException
from pprint import pprint


def scanningWebSite(webUrl):
  # Configure API key authorization: Apikey
  configuration = cloudmersive_virus_api_client.Configuration()
  configuration.api_key['Apikey'] = 'apikey'
  '''
  {
    "Url": "https://secure.eicar.org/eicar.com"
  }
  '''

  # create an instance of the API class
  api_instance = cloudmersive_virus_api_client.ScanApi(cloudmersive_virus_api_client.ApiClient(configuration))
  #input = cloudmersive_virus_api_client.WebsiteScanRequest(url="https://secure.eicar.org/eicar.com") # WebsiteScanRequest | 
  input = cloudmersive_virus_api_client.WebsiteScanRequest(url=webUrl) # WebsiteScanRequest | 

  try:
      # Scan a website for malicious content and threats
      api_response = api_instance.scan_website(input)
      #pprint(api_response)
      pprint(api_response.clean_result)
      return api_response.clean_result
  except ApiException as e:
      print("Exception when calling ScanApi->scan_website: %s\n" % e)
