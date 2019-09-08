import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  links = [
    {
      label: 'Voter Registration',
      url: "/kyc"
    },
    {
      label: 'Voter Login',
      url: "/dashboard"
    },
    {
      label: 'KYC Verifier Portal',
      url: "/kycverifier"
    },
    {
      label: 'Admin Portal',
      url: "/admin",
    }
  ];

  constructor() { }

  ngOnInit() {
  }

}
