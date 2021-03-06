import { Component, OnInit } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { MatSnackBar } from "@angular/material";
import { Router } from "@angular/router";
import { Web3Service } from "../util/web3.service";
import Web3 from "web3";
import voterdata_artifact from "../../../build/contracts/VoterData.json";
import Torus from "@toruslabs/torus-embed";
import moment from "moment";

const network_config = {
  // httpradar: new http("https://api.radarrelay.com/0x/v2"),
  RPC_PROVIDER: "https://localhost:8545/",
  NETWORK_ID: 1
};

// const web3 = Web3Service.web3;

@Component({
  selector: "app-kyc-verifier",
  templateUrl: "./kyc-verifier.component.html",
  styleUrls: ["./kyc-verifier.component.css"]
})
export class KycVerifierComponent implements OnInit {
  VoterDataInstance: any;
  torus: any;
  web3: any;
  std_web3: any;

  // Dummy verifier (in actual practice, login mechanism would be used)
  verifier = {
    name: "Amit Singh"
  };

  // unverifiedVoters = UNVERIFIED_VOTERS;
  unverifiedVoters: any;

  displayedColumns: string[] = [
    "Name",
    "UUID",
    "Date of Birth",
    "Address",
    "Constituency",
    "Status"
  ];

  model = {
    accounts: null,
    primary_account: null
  };

  constructor(
    private matSnackBar: MatSnackBar,
    private http: HttpClient,
    private router: Router,
    private web3Service: Web3Service
  ) {
    console.log("KYC-V CONSTRUCTOR");
    this.watchAccount();
    setInterval(() => this.watchAccount(), 4000);
  }

  ngOnInit() {
    // console.log("OnInit: " + this.web3Service);
    // console.log(this);
    this.getVoterList();
    this.std_web3 = new Web3();
    // this.torus = new Torus({
    //   buttonPosition: "bottom-left"
    // });

    // await this.torus.init({
    //   buildEnv: "production", // default: production
    //   enableLogging: true, // default: false
    //   network: {
    //     host: "localhost", // default: mainnet
    //     chainId: 1977, // default: 1
    //     networkName: "Ganache" // default: Main Ethereum Network
    //   },
    //   showTorusButton: true // default: true
    // });

    // // this.torus.setProvider({ host: "localhost" });

    // await this.torus.login(); // await torus.ethereum.enable()
    // this.web3 = new Web3(this.torus.provider);

    // this.watchAccount();
    // this.model.accounts = await this.web3.eth.getAccounts();
    // // console.log("ji", this.web3Service.web3);
    // this.model.primary_account = this.model.accounts[0];

    // this.web3Service
    //   .artifactsToContract(voterdata_artifact)
    //   .then((result: any) => {
    //     this.VoterDataInstance = result;
    //     this.VoterDataInstance.deployed().then(deployed => {
    //       console.log("deployed contract : ", deployed);
    //       this.VoterDataInstance = deployed;
    //     });
    //   });
  }

  watchAccount() {
    // this.web3Service.accountsObservable.subscribe(accounts => {
    //   this.model.accounts = accounts;
    //   this.model.primary_account = accounts[0];
    //   console.log("ACCOUNT SET", accounts[0]);
    //   // this.refreshBalance();
    // });
    this.model.accounts = this.web3Service.accounts;
    if (this.model.accounts)
      this.model.primary_account = this.model.accounts[0];
  }

  // async refreshBalance() {
  //   console.log("Refreshing balance");

  //   try {
  //     const deployedMetaCoin = await this.MetaCoin.deployed();
  //     console.log("DeployedMetaCoin", deployedMetaCoin);
  //     console.log("Account", this.model.account);
  //     const metaCoinBalance = await deployedMetaCoin.getBalance.call(
  //       this.model.account
  //     );
  //     console.log("Found balance: " + metaCoinBalance);
  //     this.model.balance = metaCoinBalance;
  //   } catch (e) {
  //     console.log(e);
  //     this.setStatus("Error getting balance; see log.");
  //   }
  // }

  setStatus(status) {
    this.matSnackBar.open(status, null, { duration: 3000 });
  }

  setStatusShort(status) {
    this.matSnackBar.open(status, null, { duration: 2000 });
  }

  public async verify(voter: any) {
    this.setStatus("Verifying " + voter.name);
    // Handle dates using moments. Not required anymore
    // let voter_dob = moment(new Date(voter.dob).toUTCString()).valueOf() / 1000;
    // let current_time = moment(new Date().toUTCString()).valueOf() / 1000;

    this.VoterDataInstance = this.web3Service.VoterDataInstance;

    let voter_dob = new Date(voter.dob).getTime();
    let current_time = new Date().getTime();
    let uuidHash = this.std_web3.utils.soliditySha3(voter.uuid);

    try {
      // Get the nonce & post data to the blockchain
      console.log("PRIMARY ACCOUNT", this.model.primary_account);
      const nonce = await this.web3Service.getNonce(this.model.primary_account);
      // .then(() => console.log("DAAL DIYA CALLBACK"));
      console.log("Got nonce: ", nonce);
      console.log("account from : ", this.model.primary_account);
      console.log(this.VoterDataInstance);
      this.VoterDataInstance.kycVerify
        .sendTransaction(uuidHash, voter.name, voter_dob, current_time, {
          from: this.model.primary_account,
          nonce: nonce
        })
        .then((res, err) => {
          if (err !== undefined) {
            console.error("Error!!!!", err);
            this.setStatus("Error: Unable to verify! Please try again later");
            // voter.verification_status = "unverified";
          } else {
            console.log(res.receipt.status);
            if (res.receipt.status == true) {
              console.log("receipt : ", res.receipt);
              this.updateVerificationStatusDB(voter.name, voter.uuid);
            } else {
              console.log("transaction failed. check receipt : ", res.receipt);
              this.setStatus("Error: Unable to verify! Please try again later");
            }
          }
        });
    } catch (err) {
      console.log("Error!!", err);
      this.setStatus("Error: Unable to verify! Please try again later");
    }

    // this.updateVerificationStatusDB(voter.name, voter.uuid);
  }

  async updateVerificationStatusDB(name: string, uuid: number) {
    var data = {
      uuid
    };
    var url = "/v1/kyc/info/verify/";
    this.http.post(url, data).subscribe(res => {
      console.log(res);
      this.setStatus("Voter " + name + " verified!");
      console.log("calling voter list function inside....");
      this.getVoterList();
    });
  }
  removeVoterFromUnregistered(voter: any) {
    console.log("I am here");
    this.unverifiedVoters.splice(
      this.unverifiedVoters.findIndex(_voter => _voter.uuid == voter.uuid),
      1
    );
    console.log(this.unverifiedVoters);
  }

  getVoterList() {
    console.log("getting the list of voters ...");
    let url = "/v1/kyc/info/list/";
    this.http.get(url).subscribe(res => {
      console.log(res);
      this.unverifiedVoters = res;
    });
  }

  home() {
    this.router.navigateByUrl("/home");
  }
}
