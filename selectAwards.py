import pathlib
import requests
from requestAccessToken import *

def requestAwards(id: str, accTkn: str):
    '''This function will return the data of an award given its id '''

    urlbase = f'https://www.contrataciones.gov.py/datos/api/v3/doc/awards/{id}'
    headers = {'accept':'application/json', 'Authorization':f'Bearer {accTkn}'}
    data = requests.get(urlbase, headers = headers)
    if data.ok == True:
        data = data.json()
        res = {}
        for el in data['awards']:
            res[el['id']] = el
    elif data.reason == "TOO MANY REQUESTS":

        with open(pathlib.Path(__file__).parent / "CK.txt", 'r') as file:
            CK = file.read()
        with open(pathlib.Path(__file__).parent / "CS.txt", "r") as file:
            CS = file.read()
        accTkn = requestAccessToken(CK, CS)
        return requestAwards(id, accTkn)
    else:

        raise Exception(data.reason)
    return res


if __name__ == "__main__":
    import requests
    import pathlib
    from requestAccessToken import *

    mypath = pathlib.Path(__file__).parent
    #First, we obtain the access token
    with open(mypath / "CK.txt", 'r') as file:
        CK = file.read()
    with open(mypath / "CS.txt", "r") as file:
        CS = file.read()
    accTkn = requestAccessToken(CK, CS)
    requestAwards("351815-classic-mobles-sociedad-anonima-3", accTkn)

    
