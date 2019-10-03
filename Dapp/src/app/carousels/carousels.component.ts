import { Component, OnDestroy, Injectable } from "@angular/core";
import { CarouselConfig } from "ngx-bootstrap/carousel";
import { Router } from "@angular/router";
import Torus from "@toruslabs/torus-embed";
import Web3 from "web3";

@Component({
  templateUrl: "carousels.component.html",
  providers: [
    { provide: CarouselConfig, useValue: { interval: 1500, noPause: false } }
  ]
})
export class CarouselsComponent implements OnDestroy {
  myInterval: number | false = 6000;
  slides: any[] = [];
  activeSlideIndex: number = 0;
  noWrapSlides: boolean = false;
  web3: any;
  torus: any;
  userInfo: any;

  constructor(private router: Router) {
    for (let i = 0; i < 4; i++) {
      this.addSlide();
    }
  }

  // async ngOnInit() {
  //   this.torus = new Torus({
  //     buttonPosition: "bottom-left"
  //   });

  //   await this.torus.init({
  //     buildEnv: "development", // default: production
  //     enableLogging: true, // default: false
  //     network: {
  //       host: "localhost", // default: mainnet
  //       chainId: 1977, // default: 1
  //       networkName: "Ganache" // default: Main Ethereum Network
  //     },
  //     showTorusButton: true // default: true
  //   });

  //   this.torus.setProvider({ host: "localhost" });

  //   await this.torus.login(); // await torus.ethereum.enable()
  //   this.web3 = new Web3(this.torus.provider);

  //   this.userInfo = await this.torus.getUserInfo();
  //   console.log("ji", this.userInfo);

  //   this.torus.showWallet();
  // }

  async ngOnDestroy() {
    this.myInterval = 0;
    this.noWrapSlides = true;
    this.myInterval = false;

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

    // this.userInfo = await this.torus.getUserInfo();
    // console.log("ji", this.userInfo);

    // this.torus.showWallet();
    console.log("ONDESTROY");
  }

  addSlide(): void {
    this.slides.push({
      image: `https://lorempixel.com/900/500/abstract/${(this.slides.length %
        8) +
        1}/`
    });
  }

  removeSlide(index?: number): void {
    const toRemove = index ? index : this.activeSlideIndex;
    this.slides.splice(toRemove, 1);
  }

  redirect() {
    this.router.navigate(["./home"]);
  }
}
