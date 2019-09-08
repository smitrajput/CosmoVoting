<h1 align="center">Excalibur</h1>
<p align="center">:computer: :closed_lock_with_key: :scroll:</p>

***

## Steps to set up the project 

#### Using Local Ganache Instance:

1. Clone the repo using `git clone git@github.com:tHeMaskedMan981/Excalibur-code-fun-do.git` and `cd` into it
2. To start the ganache instance, type `ganache-cli -m 'emotion wall cash clown nut tongue project picnic public arch blush inform'` *[Here, we use a predefined mnemonic to seed the accounts that are generated for ease of demo]*
3. Fire a new terminal in the same folder & type `truffle migrate` to deploy the contracts to the local ganache instance
4. Fire another terminal in the same folder, create a python3 virtual environment using `python3 -m venv ./venvs/django`
5. In the same terminal, start the virtual environment using `source ./venvs/django/bin/activate`
6. To start the Django server, `cd ./django/vote`, followed by `python manage.py runserver`
7. Now, fire up a new terminal and type in `npm start` to start the Voting DApp.