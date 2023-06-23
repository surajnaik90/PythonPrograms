#https://powerusers.microsoft.com/t5/Building-Flows/Send-an-image-to-Azure-DevOps-HTTP-request-PATCH/td-p/2051421
#https://stackoverflow.com/questions/61524419/azure-devops-api-invalid-patch-document

import requests

organization = "org"
project = "proj"
id = 608

params = [{
    "op": "add",
    "path": "/relations/-",
    "value": {
        "rel": "System.LinkTypes.Hierarchy-Forward",
        "url": "https://dev.azure.com/org/proj/_apis/wit/workItems/608",
        "attributes": {
            "comment": "locking link",
            "isLocked": True
        }
    }
}]

headers = {
    'Content-Type': 'application/json-patch+json'
}

#Needs ADO Server Admin access
response = requests.patch(
            url="https://dev.azure.com/{organization}/{project}/_apis/wit/workitems/{id}?api-version=7.0",
            auth=('user-name', 'pat-token'),
            params=params,
            headers=headers
        )

response.raise_for_status()

data = response.json()
print(data)