import requests
import configuration
def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)


response = get_docs()

print(response.status_code)
