import fastly
from fastly.api import historical_api
from pprint import pprint
configuration = fastly.Configuration()
configuration.api_token = 'YOUR_FASTLY_API_TOKEN'
with fastly.ApiClient(configuration) as api_client:
    api_instance = historical_api.HistoricalApi(api_client)
    
    try:
        api_response = api_instance.get_regions()
        pprint(api_response)
    except fastly.ApiException as e:
        print("Exception when calling HistoricalApi->get_regions: %s\n" % e)