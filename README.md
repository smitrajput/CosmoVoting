<p align="center"><img src="./Dapp/src/assets/final_logo.png" align="center"></p>
<p align="center">Taking Decentralized Voting to the <strong><i>next</i></strong> level</p>

## Table of Contents

- [Vision](#vision)
- [Problems to Solve](#problems-to-solve)
- [Key Features](#key-featuers)
- [Impact Points](#impact-points)
- [Collaboration](#collaboration)
- [Local Setup](#local-setup-)
- [Next Steps](#next-steps)
- [Core Team](#core-team)

## Vision

Spinning up ultra-secure, anonymous and decentralized voting solutions, for

- Governments
- Enterprises and Corporates
- Governance Protocols (in Ethereum and other blockchains)
- Providing Customized Voting Solutions,

while exploring/exploiting the synergies produced during the process.

## Problems To Solve

1. Increasing the average voter turnout in Elections around the world, by bringing the end-to-end voting process, online, in a secure manner
2. Removing trust issues in Country election campaigns all over the world.
3. Speeding up the State-Of-The-Art voting processes in the 3 domains mentioned in the 'Vision' above.
4. Reducing overall costs incurred by Governments in conducting their elections.

## Key Features

1. Current implementation includes a secure, anaonymous and transparent implementation of the First-Past-The-Post type Elections, which is one type out of a total of 13 concrete types of Electoral systems.
2. Providing full-fledged voting solutions, and SATaaS (Security, Anonymity and Transparency as a Service) to existing voting solutions in the 3 domains mentioned in the 'Vision' above.
3. A Plug-and-Play SDK to allow developers and other organizations to create Secure, Anonymous, Transparent (SAT from here on) and customized voting solutions, in accordance with their needs.

## Impact Points

1. Increased _accessibility_ to Voters, leading to a larger voter turnout, eventually, if not immediately.
2. Immense business value for Torus (our Auth Partner), even at a very low global acceptance rate of the project.
3. _International Voting Interoperability_, as a consequence of multiple Countries' and Orgs' voting implementations on a single platform (think International and Inter-Continental voting, for making global decisions, based on decentralized Global Identities, powered by Torus)
4. Birth of _International Voting Standards_ for fair, secure and anonymous voting, which would act as the next _Status Quo_, as far as voting is concerned.
5. Even a success rate of 5% of this project, would be a _major boost_ to Blockchain adoption to the masses.

## Collaboration

<p align="center"><img src="./Dapp/src/assets/collab.png" align="center"></p>

CosmoVoting uses Torus for a seamless authentication experience for its users, for the following reasons:

1. One of the easiest ones to integrate with.
2. Generates a wallet for every gmail account, which acted as a sweet bridge for us, between OAuth 2.0 and Web 3.0 wallets like MetaMask.
3. Torus would help us in orders of magnitudes, in exploring decentralized Global Identites for International and Inter-Continental Voting, for purposes meant to impact the world as a whole (think Framing international policies to tackle Climate Change, and the likes)

## Local Setup

1. Clone the repo using `https://github.com/smitrajput/CosmoVoting.git` and `cd` into it
2. To start the ganache instance, type `ganache-cli --port 8546`
3. Start a ganache proxy server using: `ganache-http-proxy`
4. Fire a new terminal in the same folder type `cd Dapp` and then `truffle migrate` to deploy the contracts to the local ganache instance
5. Now, type `cd ..` and create a python3 virtual environment using `python3 -m venv ./venvs/django` OR `virtualenv -p python3 ./venvs/django/bin/`
6. In the same terminal, start the virtual environment using `source ./venvs/django/bin/activate`
7. After making sure pip, python, django are installed in the virtual environment too, type `cd django && pip3 install -r requirements.txt`
8. [In case it doesn't get installed automatically], `pip install wheel`
9. To start the Django server, `cd vote`, followed by `python manage.py runserver` OR `python3 manage.py runserver`
10. Now, fire up a new terminal, `cd` into 'Dapp' directory and type in `npm start` to start the Voting DApp.

## Next Steps

1. Creating a clean and sleek UI/UX for the current implementation of the First-Past-The-Post type Elections.
2. Implementing SAT elections for the remaining 12 types of Electoral systems.
3. Inculcating Advanced Security implementations via GPIPs (Global Project Improvement Proposals)

## Core Team

[Smit Rajput](https://www.linkedin.com/in/smit-rajput-417517139/)<br />[Akash Kumar](https://www.linkedin.com/in/akash981/)<br />[Tezan Sahu](https://www.linkedin.com/in/tezan-sahu/)
