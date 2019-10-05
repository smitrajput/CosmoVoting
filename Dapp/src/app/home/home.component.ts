import { Component, OnInit } from "@angular/core";
import { Web3Service } from "../util/web3.service";

@Component({
  selector: "app-home",
  templateUrl: "./home.component.html",
  styleUrls: ["./home.component.css"]
})
export class HomeComponent implements OnInit {
  ElectionInstance: any;
  accounts: any;
  nonce: any;
  links = [
    {
      label: "Voter Registration",
      url: "/kyc"
    },
    {
      label: "Voter Login",
      url: "/dashboard"
    },
    {
      label: "KYC Verifier Portal",
      url: "/kycverifier"
    },
    {
      label: "Admin Portal",
      url: "/admin"
    }
  ];

  constructor(private web3Service: Web3Service) {
    // this.addConstituencies();
  }

  ngOnInit() {}

  async addConstituencies() {
    // this.ElectionInstance = await this.web3Service.ElectionInstance;
    // this.accounts = await this.web3Service.accounts;
    // if (this.accounts) {
    // this.nonce = await this.web3Service.getNonce(this.accounts[0]);
    //   this.addConstituencies();
    // }
    // await this.ElectionInstance.addConstituency("Bangalore", {
    //   from: this.accounts[0],
    //   nonce: this.nonce
    // });
    //   this.nonce = this.nonce + 1;
    //   await this.ElectionInstance.addConstituency("mumbai", {
    //     from: this.accounts[0],
    //     nonce: this.nonce
    //   });
    //   this.nonce = this.nonce + 1;
    //   await this.ElectionInstance.addConstituency("banglore", {
    //     from: this.accounts[0],
    //     nonce: this.nonce
    //   });
    //   await this.ElectionInstance.addParty("Congress", {
    //     from: this.accounts[0],
    //     nonce: this.nonce
    //   });
    //   await this.ElectionInstance.addParty("BJP", {
    //     from: this.accounts[0],
    //     nonce: this.nonce
    //   });
    //   await this.ElectionInstance.addParty("BSP", {
    //     from: this.accounts[0],
    //     nonce: this.nonce
    //   });
    //   console.log("CONSTITUENCIES ADDED");
    //   console.log("HAVE A LOOK", await this.ElectionInstance.getConstituencies());
  }
}
