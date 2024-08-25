import json
from web3 import Web3

class NFTContract:
    def __init__(self, config_path: str, web3: Web3):
        self.web3 = web3
        self.load_config(config_path)
    
    def load_config(self, config_path: str):
        with open(config_path, 'r') as file:
            config = json.load(config_path)
        self.contract_address = config['contract_address']
        self.contract_abi = config['contract_ABI']
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.contract_abi)
    