var HelloBlockchain = artifacts.require("HelloBlockchain");

module.exports = function(done) {
  console.log(
    "Getting the deployed version of the HelloBlockchain smart contract"
  );
  HelloBlockchain.deployed()
    .then(function(instance) {
      console.log(
        "Calling SendRequest function for contract ",
        instance.address
      );
      return instance.SendRequest("Hello, blockchain!");
    })
    .then(function(result) {
      console.log("Transaction hash: ", result.tx);
      console.log("Request complete");
      done();
    })
    .catch(function(e) {
      console.log(e);
      done();
    });
};
