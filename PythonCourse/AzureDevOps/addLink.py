#https://powerusers.microsoft.com/t5/Building-Flows/Send-an-image-to-Azure-DevOps-HTTP-request-PATCH/td-p/2051421
#https://stackoverflow.com/questions/61524419/azure-devops-api-invalid-patch-document

import requests

organization = "org"
project = "proj"
id = 608

params = [
    {
        "op": "add",
        "path": "/relations/-",
        "value": 
            {
                "rel": "System.LinkTypes.Hierarchy-Forward",
                "url": "https://dev.azure.com/org/proj/_apis/wit/workItems/609",
                "attributes": {
                    "comment": "locking link"
                }
            }
    }
]

headers = {
    'Content-Type': 'application/json-patch+json'
}

response = requests.patch(
            url="https://dev.azure.com/org/proj/_apis/wit/workitems/608?api-version=7.0",
            auth=('user-name', 'pat-token'),
            json=params, headers=headers
        )

response.raise_for_status()

data = response.json()

print(data)