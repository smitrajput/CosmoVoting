const VoterData = artifacts.require("VoterData");
const assert = require("chai").assert;
const truffleAssert = require("truffle-assertions");
const Web3 = require("web3");
var web3 = new Web3();
const uuidv4 = require("uuid/v4");

contract("VoterData", accounts => {
  var ec_head;
  var VoterDataInstance;
  var voterid;
  var current_timestamp;

  before(async () => {
    VoterDataInstance = await VoterData.deployed();
    // Setup account.
    ec_head = accounts[0];
    uuid1 = 121212121212;
    uuid_hash_1 = web3.utils.keccak256(uuid1.toString());
    voterid = uuidv4().toString();
    var date = new Date();
    current_timestamp = date.getTime();
  });

  describe("success states", async () => {
    
    it("should hash correctly", async () => {
      
      console.log(web3.utils.sha3("a"));
      let hash = await VoterDataInstance.hash.call("a");
      console.log(hash);
    });

    it("should add voter data correctly", async () => {
      
      let dob = new Date(1998, 1, 8); // for the age to be 21 years 
      console.log("dob : ", dob, " : ", dob.getTime());
      await VoterDataInstance.kycVerify(
        uuid_hash_1,
        "akash kumar",
        dob.getTime(),
        current_timestamp,
        { from: ec_head }
      );
      var voter = await VoterDataInstance.voters.call(uuid_hash_1);
      console.log("voter object : ", voter);
    });

    it("should generate voter id correctly", async () => {
      await VoterDataInstance.generateVoterId(
        uuid_hash_1,
        voterid,
        current_timestamp,
        {
          from: ec_head
        }
      );
      var voter = await VoterDataInstance.voters.call(uuid_hash_1);
      console.log("voter object : ", voter);
    });
  });

  describe("failure states", async () => {
    it("should not generate voter id if age is less than 18 years ", async () => {
      let dob = new Date(2001, 9, 16); // for the age to be 17 years 
      await VoterDataInstance.kycVerify(
        uuid_hash_1,
        "smit rajput",
        dob.getTime(),
        current_timestamp,
        { from: ec_head }
      );
      var voter = await VoterDataInstance.voters.call(uuid_hash_1);
      console.log("voter object : ", voter);

      await truffleAssert.reverts(
        VoterDataInstance.generateVoterId(
          uuid_hash_1,
          voterid,
          current_timestamp,
          {
            from: ec_head
          }
        ),
        "Not Allowed to Vote. Only eligible to vote if age is above 18 years."
      );
    });
  });
});
