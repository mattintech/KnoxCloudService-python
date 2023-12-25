<div style="text-align: right"> 
    <a href="https://www.buymeacoffee.com/mattintech" target="_blank">
    <img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
</div>

# KnoxCloudService-Python
**Not an offical Samsung** Repository.  

This repository leveages the PyKTL & PYKATh libraries to interact with Samsung's Knox Cloud Service ('KCS') APIs

## Getting started
Install the unofficial Knox Python Access Token Helper Library.  
```
pip install PyKATh
```
Log into the SamsungKnox.com portal and download the private keys file.

Create a client json 
```
{
    "kme": "insert clientId from the SamsungKnox.com portal" 
}
```
For more information on obtaining the private/public key (keys.json) and/or a client id reference Samsung's KCS Tutorial. - https://docs.samsungknox.com/dev/knox-cloud-authentication/tutorial/tutorial-for-customers-generate-access-token/


## API Reference
Here are a list of API references by service:

- KME - https://docs.samsungknox.com/dev/knox-mobile-enrollment/server-integration/api/
- KAI - https://docs.samsungknox.com/dev/knox-asset-intelligence/api/
- KM - https://docs.samsungknox.com/dev/knox-manage/api/
- KC - https://docs.samsungknox.com/dev/knox-configure/api/
- KG - https://docs.samsungknox.com/dev/knox-guard/api/
