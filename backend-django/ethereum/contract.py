from web3 import Web3
from solc import compile_source

rpc_url = "http://localhost:8545"
web3 = Web3(Web3.HTTPProvider(rpc_url))
web3.geth.personal.unlockAccount(web3.eth.accounts[0], "rondo14!", 0)

compiled_sol = compile_source(contract_source_code)
contract_interface = compiled_sol["<stdin>:Greeter"]

# 배포 준비, 스마트 컨트랙트 껍데기(abi)에 내용물(bin)을 채운다.
contract = w3.eth.contract(abi= contract_interface['abi'],
                           bytecode= contract_interface['bin'],
                           bytecode_runtime= contract_interface['bin-runtime'])


# 비용을 부담할 주소를 from으로 하는 트랜잭션을 포함해 배포한다.
tx_hash = contract.deploy(transaction={'from': w3.eth.accounts[0]})

# 마이닝을 해줘야 후에 실제로 사용할 수 있다.
w3.miner.start(2)
time.sleep(5)
w3.miner.stop()

print(web3.isConnected())
print(web3.eth.blockNumber)

balance = web3.eth.getBalance("0xc725bD3F7Fb9E7D3E8A8d20545b4024333abdC0a")
print(web3.fromWei(balance, "ether"))