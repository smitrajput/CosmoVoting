pragma solidity ^0.5.0;
pragma experimental ABIEncoderV2;

// import "./VoteVault.sol";

contract Election {
 
    address public EC_Head;
    mapping(address => bool) public kyc_verifiers;
    mapping(address => bool) public ec_officials;

    // event Approval(address indexed tokenOwner, address indexed spender, uint tokens);
    // event Transfer(address indexed from, address indexed to, uint tokens);

    string[] public  constituencies;
    string[] public parties;
    // mapping(uint8 => string) public partyName;
    mapping(bytes32 => bool) public hasVoted;
    mapping(bytes32 => bool) public kycDone;
    // mapping(uint => bool) public kycDone;
    uint public voterCount;
    mapping(string => mapping (string => bytes32[]))  vote_hashes;
    mapping(string => mapping (string => uint))  result;
    mapping(string => string)  winner;

    // Vault opens/opened at this time
    uint256 public beginTime;
    
    // Vault closes/Closed at this times
    uint256 public endTime;
    
    // flag to track whether vault closed permanently or not
    bool public vaultSealed;
    
    // Checks whether the vault is opened or not
    bool public isVaultOpened;


    using SafeMath for uint;
    
    modifier onlyEcHead {
        require((msg.sender == EC_Head), "You are not Authorized to make this function Call.");
        _;
    }
    modifier onlyEcOfficial {
        require((ec_officials[msg.sender]), "You are not Authorized to make this function Call.");
        _;
    }
    modifier onlyKycVerifier {
        require((kyc_verifiers[msg.sender]), "You are not Authorized to make this function Call.");
        _;
    }

   constructor() public {  
	
    EC_Head = msg.sender;
    ec_officials[msg.sender] = true;
    // will remove this when actual voting occurs
    kyc_verifiers[msg.sender] = true;
    voterCount = 0;

    vaultSealed = false;
    isVaultOpened = false;
    }  

    function addEcOfficial (address official) public onlyEcHead {
        ec_officials[official] = true;
    }
    function removeEcOfficial(address official) public onlyEcHead {
        ec_officials[official] = false;
        delete ec_officials[official];
    }
    function addKycVerifier (address verifier) public onlyEcOfficial {
        kyc_verifiers[verifier] = true;
    }
    function removeKycVerifier(address verifier) public onlyEcOfficial {
        kyc_verifiers[verifier] = false;
        delete kyc_verifiers[verifier];
    }
    function addParty (string memory party_name) public onlyEcOfficial {
        // require(!isVaultOpened);
        // require(beginTime >= uint256(now), "Cannot add a party after the elections have started.");
        parties.push(party_name);
    }
    function addConstituency (string memory constituency) public onlyEcOfficial{
        // require(!isVaultOpened);
        // require(beginTime >= uint256(now), "Cannot add a constituency after the elections have started.");
        constituencies.push(constituency);
    }

    function kycVerify(bytes32  uuid_hash) public onlyKycVerifier {
        kycDone[uuid_hash] = true;
    }

    function registerVote(bytes32 uuid_hash, string memory constituency, string memory party,  bytes32 vote_hash) public {
        // require(!vaultSealed);
        // require(isVaultOpened);
        // require(beginTime <= uint256(now), "The elections haven't started yet"); 
        // require(endTime >= uint256(now), "The election period is over");
        require(kycDone[uuid_hash], "KYC process is not complete for this voter");
        require(!(hasVoted[uuid_hash]), "The voter has already voted. Aborting.");

        vote_hashes[constituency][party].push(vote_hash);
        voterCount++;
        hasVoted[uuid_hash] = true;
    }

    function calculateVotes() public  onlyEcHead returns (bool) {
        // require(endTime <= uint256(now), "The election period is not over. Can't calculate the votes before election ends.");
        string memory _winner;

        for (uint i = 0; i < constituencies.length; i++)
        {
            _winner = parties[0];
            for (uint j = 0; j < parties.length; j++){
                 result[constituencies[i]][parties[j]] = vote_hashes[constituencies[i]][parties[j]].length;
                if ( result[constituencies[i]][parties[j]] > result[constituencies[i]][_winner]){
                    _winner = parties[j];
                }
            }
             winner[constituencies[i]] = _winner;
        }
        return true;
    }

    function getWinner(string memory constituency) public view returns (string memory) {
        return  winner[constituency];
    }
    function getVoteHashes(string memory constituency, string memory party) public view returns (bytes32[] memory) {
        return  vote_hashes[constituency][party];
    }
    function getVoteCount(string memory constituency, string memory party) public view returns (uint) {
        return  result[constituency][party];
    }
}

library SafeMath { 
    function sub(uint256 a, uint256 b) internal pure returns (uint256) {
      assert(b <= a);
      return a - b;
    }
    
    function add(uint256 a, uint256 b) internal pure returns (uint256) {
      uint256 c = a + b;
      assert(c >= a);
      return c;
    }
}
