import requests

base_url = "https://api.voyager.online/beta/"
headers = {
    'accept': 'application/json'
}


def call_api(number: str, content: str, apiKey: str) -> str:
    if number == "1":
        blockHash = content.split(".")[1]
        return get_block(blockHash, apiKey)
    elif number == "2":
        return get_blocks(apiKey)
    elif number == "3":
        transactionHash = content.split(".")[1]
        return get_transaction(transactionHash, apiKey)
    elif number == "4":
        return get_contracts(apiKey)
    elif number == "5":
        contractAddress = content.split(".")[1]
        return get_contract(contractAddress, apiKey)


def get_block(blockHash: str, apiKey: str) -> str:
    headers["x-api-key"] = apiKey
    response = requests.get(base_url + "block/" + blockHash, headers=headers)
    return response.text


def get_blocks(apiKey: str) -> str:
    headers["x-api-key"] = apiKey
    response = requests.get(base_url + "blocks", headers=headers)
    return response.text


def get_transaction(transactionHash: str, apiKey: str) -> str:
    headers["x-api-key"] = apiKey
    response = requests.get(base_url + "txns/" + transactionHash, headers=headers)
    return response.text


def get_contract(contractAddress: str, apiKey: str) -> str:
    headers["x-api-key"] = apiKey
    response = requests.get(base_url + "contracts/" + contractAddress, headers=headers)
    return response.text


def get_contracts(apiKey: str) -> str:
    headers["x-api-key"] = apiKey
    response = requests.get(base_url + "contracts", headers=headers)
    return response.text
