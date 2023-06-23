#https://stackoverflow.com/questions/64771092/azure-devops-rest-api-create-work-item-a-value-is-required
#https://developercommunity.visualstudio.com/t/azure-devops-api-return-401-unauthorized-update-wo/552636

import requests

organization = "orgName"
project = "projectName"
id = 608

response = requests.get(
    url="https://dev.azure.com/novonordiskMRDEV/RegART-AutoVal-Pilot/_apis/wit/workitems/608?$expand=all&api-version=7.0"
             , auth=('account-name', 'pat-token'))

response.raise_for_status()

data = response.json()
print(data)