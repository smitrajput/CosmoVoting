# Excalibur [codefundo++]

***
#### To set up the project, follow the steps mentioned [here](excalibur_setup.md)

***
## Proposed Solution

#### Phase 0 [Groundwork]:

- The ECI head will deploy smart contracts on the blockchain, specifying the details like voting phases of the election, start and end date/time of the election, etc.

#### Phase 1 [Registration (to be done sufficiently before the election)]:

- Every citizen will come to our platform and register with his basic details. This would include their name, father's name, age, address, etc.
- Once registered, the person will have to go to a verification center with documents to support his provided information
- The verifiers will have private-public key pairs assigned by the election commission
- They will verify the data provided using the documents presented by the citizen, and on verification, will call the blockchain to store minimal information like UUID and Date of birth

#### Phase 2 [Voting]:

- On the voting day, the voter logs into the platform which already contains his basic information.
- Using the UUID & age from the blockchain, eligibility of the voter is verified & an e-Voter card with his Voter ID is generated
- After determining the voter's constituency through his verified address, the voter will be able to see candidates contesting from his constituency.
- He will select one of them, and enter a security token (kind of a password, or salt).
  *This will be used to verify his vote later. Using the token and the voter ID, a vote hash is generated and sent along with the vote transaction to the blockchain.*
- On submitting, his actual vote is encrypted using a public key after adding a random salt.
- After the voting phase ends, the ECI Head will make a transaction, initiating the decryption of encrypted votes using an oracle, followed by aggregation of votes in the Smart Contract
- At the end of the process, the aggregated vote count per constituency decides the winner
- All vote hashes would now be made public for voters to verify if their vote was recorded correctly

##### Problems Solved:

- Voters can verify if their votes were recorded correctly
- Transparency: As smart contracts are public, anyone can verify the logic used.
- Immutability: No more allegations like EVM Hacks.
- Increase in voter turnout: The voter doesn't have to be present physically in his constituency anymore to vote.
- Automatic Voter ID. No more standing in queues to get Voter ID Card.
- No more missing names from voter's list: Anyone who registered in phase 1 and is above 18 yrs of age will be able to vote.
- Faster result declaration: Results will be available within a few hours of the end of the voting phase.

##### Tech-Stack to be Used:
- Quorum (for blockchain & smart contracts)
- Microsoft Azure (for deployment)
- Angular (for front-end)
- Django (for back-end) 
