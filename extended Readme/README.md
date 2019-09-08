# Excalibur-code-fun-do

Online Voting is something which has been there in discussions since a long time. But because of a lot of technical limitations, and prone to hacking, it never actually got accepted on large scales.
But with the emergence of Blockchain technology, this seems possible in near future.

### Current Scenerio

Voting in most of the countries still use paper ballot as the main option. Some countries like india use EVMs. Following are the problems with the current system :

- EVM hacks, manual intervention in paper ballot
- No verifiability; a voter can't verify whether his vote went to the right candidate or not, or whether it was even counted or not.
- Long delays in calculation of results.
- People not physically in their constituencies are unable to vote
- Not enough transparency in the election process.

All the above problems can be solved using blockchain. Although a few things have to be kept in mind. Though blockchain brings in verifiability, transparency and immutability in the picture, it takes away anonymity and confidentiality. Very basic requirements of any election is :

- Secrecy of Vote : No one should know who or what I voted for.
- any kind of bias should not be created before the voting period ends; ie all the votes should remain confidential till the end of voting phase.

These 2 requirements are a must for any online voting system to work in real world. This can be done with careful use of cryptography.

So the solution that we are presenting involves cryptography to keep the anonymity and confidentiality of vote, and blockchain to maintain immutability, transparency and verifiability in the election system, along with faster results and increase in voter turnout.

## Our Solution

#### Phase 1 : Registration

- Every user or citizen of a country will come to our platform and register with his basic details. This may include his name, father's name, age, address, etc.
- Once registered, the person will have to go to a verification center with all his documents to support his provided information in a limited period of time.
- The verifiers will be assigned by the election commission. Every verifier will have his private public key pair, whose mapping will be there with the election commission.
- The verifier verifies the data provided in the form using the documents presented by the citizen, and on verification, makes a transaction on the blockchain which stores minimal information like UUID and Date of birth on the blockchain.
- This process is supposed to be done way before the election.

#### Phase 2 : Voting

- On the voting day, voter logs in the platform.
- The platform will already have the basic information of the voter. Using the UUID, we will check if the voter is eligible to vote or not based on his age stored on the blockchain.
- If eligible, an e-Voter Card will be generated for the user, which will have a voter ID, which will remain unique corresponding to a particular UUID.
- Using the verified address of the user, we will be able to figure out the constituency and the polling booth the person was supposed to vote at.
- Now the ECI head will deploy the smart contract on the blockchain, specifying the details like the voting phases of the election, start and end date and time of election, etc.
- Once the voting period starts, the voter will be able to see the candidates from his constituency contesting for the seat.
- He will select one of them, and enter a security token (kind of a password, or salt).
  This token will be used letter on to verify his vote. using the token and the voter ID, a vote hash is generated and sent along with the vote transaction.
- Once he clicks on submit vote, his actual vote, ie the party he choose, is encrypted using a public key after adding a random salt. That way doing any brute force attack becomes infeasible, and just looking at transaction parameter no one will be able to figure out anything about the vote.
- After the voting phase ends, the ECI Head will make a transaction, which will initiate the decryption of encrypted votes.
- We can use an oracle to decrypt the party data and send back to the contract. We can maintain a counter for each party in each constituency.
- At the end of the process, the ECI head makes another transaction, which starts calculating the result, which just looks at the counter values to decide the winner in each constituency.
- At the end, all the vote hashes are made public and anyone can verify regenerating his vote hash whether his/her vote went to the intended candidate or not.

##### Problems Solved :

- A voter can verify whether his vote went to the inteded candidate or not
- Transparency of the complete election process. As smart contract is public, anyone can verify the logic for register vote and calculation of votes functions
- Immutability. No more allegations and doubts like EVM Hacks.
- Increase in voter turnout. The voter doesn't have to be present physically in his constituency anymore to vote.
- Automatic Voter ID. No more standing in queues to get Voter ID Card.
- No more missing names from voter's list. Anyone who registered earlier in phase 1 and is above 18 yrs of age will be able to vote.
- Anonymity and security. No information about the voter revealed at any point of time.
- Faster declaration of results. No more waiting for multiple days for declaration of results. Results will be available within few hours of end of voting phase.
- No more manual intervention possible.

#### Corner Cases : Mitigation of possible errors

- The verifier Colludes : Right now, in current scenerio, the person issuing voter ID card can also collude and generate fake ID Cards. But we don't have any way to backtrack to the defaulter. In our system, if any verifier does anything malicious, we will know exactly the person responsible for the malicious act.
- There might be a concern that the oracle decrypting the data and submitting back to the smart contract can be malicious. Using simple hashing and ecryption techniques, we can easily make sure that contract will only accept the value if it is exactly what it was supposed to be. If the oracle is compromised, we will know right away and he won't to able to manipulate the votes.
- Because of the checks in the smart contract corresponding to the timing of the voting phase, even the ECI Head himself can't do anything to extract any information about the voting. Only once the voting period ends he will be able to call those functions. To further increase the security, we can make the result calculation transaction a multisig.
- There are chances that Voter coercion might increase with the introduction of online voting. In that case, we can have special voting booths where a tablet or a PC can be used for voting, with the same amount of security which is there in the current system.
- Online voting might not work in places where there is weak or no internet connection. So we can remove those constituencies from the online voting process beforehand, such that the voters from those constituencies will be allowed to vote only physically on the polling booth. But that raises the concern of multiple votes. To solve that problem, we can keep the online voting phase 4-5 days before the offline voting, and at the time of offline voting, we can just make a call to the smart contract to make sure whether the person have already voted or not. We can also provide a list of all the voters in a particular constituency who voted online which can be downloaded by concerned officials.
