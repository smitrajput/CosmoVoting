const fs = require("fs");
const HDWalletProvider = require("truffle-hdwallet-provider");
var defaultnode =
  "https://akash.blockchain.azure.com:3200/WsUdgDBd0FSR3QjR6-4RQ707";
var Web3 = require("web3");
module.exports = {
  networks: {
    defaultnode: {
      provider: new Web3.providers.HttpProvider(defaultnode),
      network_id: "*"
    },
    election2: {
      network_id: "*",
      gas: 70000000,
      gasPrice: 0,
      provider: new HDWalletProvider(
        fs.readFileSync(
          "/home/tezansahu/Tezan/Github Repos/Excalibur-code-fun-do/blockchain/election.env",
          "utf-8"
        ),
        "https://akash.blockchain.azure.com:3200/WsUdgDBd0FSR3QjR6-4RQ707"
      ),
      consortium_id: 1565635202622
    },
    development: {
      host: "localhost",
      port: 8545,
      network_id: "*" // Match any network id
    }
  }
};
