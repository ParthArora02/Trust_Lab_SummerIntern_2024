import requests

def get_gas_fees(api_key):
    url = f"https://api.etherscan.io/api?module=gastracker&action=gasoracle&apikey={api_key}" # use your api key for getting the prices from etherscan
    response = requests.get(url)
    data = response.json()
# there are 3 types of gas prices i.e. safe, proposed and fast https://etherscan.io/gastracker
# safe is cheapest but may take longer times for the transactions, proposed is the recommended one for general
# purposes, fast is expensive than both of the previous ones, but makes fast transactions.
    if data['status'] == '1':  # Successful response
        safe_gas_price = data['result']['SafeGasPrice']
        propose_gas_price = data['result']['ProposeGasPrice']
        fast_gas_price = data['result']['FastGasPrice']
        
        return {
            "SafeGasPrice": safe_gas_price,
            "ProposeGasPrice": propose_gas_price,
            "FastGasPrice": fast_gas_price
        }
    else:
        raise Exception("Error fetching gas fees from Etherscan") # throws error if it is unable to get the data
