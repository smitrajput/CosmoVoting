// import { InjectionToken } from "@angular/core";
// import Web3 from "web3";
// import Torus from "@toruslabs/torus-embed";

// export const WEB3 = new InjectionToken<Web3>("web3", {
//   providedIn: "root",
//   factory: () => {
//     try {
//       this.torus = new Torus({
//         buttonPosition: "bottom-left"
//       });

//       this.torus.init({
//         buildEnv: "production", // default: production
//         enableLogging: true, // default: false
//         network: {
//           host: "localhost", // default: mainnet
//           chainId: 1977, // default: 1
//           networkName: "Ganache" // default: Main Ethereum Network
//         },
//         showTorusButton: true // default: true
//       });

//       // this.torus.setProvider({ host: "localhost" });

//       this.torus.login(); // await torus.ethereum.enable()
//       web3 = new Web3(this.torus.provider);

//       const provider =
//         "ethereum" in window ? window["ethereum"] : Web3.givenProvider;
//       return new Web3(provider);
//     } catch (err) {
//       throw new Error(
//         "Non-Ethereum browser detected. You should consider trying Mist or MetaMask!"
//       );
//     }
//   }
// });
