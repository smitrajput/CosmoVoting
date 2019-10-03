### A unique voting solution on the Ethereum blockchain using Torus for authentication

#### Setting up the project

1. Clone the repo using `git clone git@github.com:smitrajput/Excalibur-voting.git` and `cd` into it
2. To start the ganache instance, type `ganache-cli -m 'emotion wall cash clown nut tongue project picnic public arch blush inform'` _[Here, we use a predefined mnemonic to seed the accounts that are generated for ease of demo]_
3. Fire a new terminal in the same folder & type `truffle migrate` to deploy the contracts to the local ganache instance
4. Fire another terminal in the same folder, create a python3 virtual environment using `python3 -m venv ./venvs/django` OR `virtualenv -p python3 ./venvs/django/bin/`
5. In the same terminal, start the virtual environment using `source ./venvs/django/bin/activate`
6. After making sure pip, python, django are installed in the virtual environment too, run `pip3 install -r requirements.txt`
7. `pip install wheel`
8. To start the Django server, `cd ./django/vote`, followed by `python manage.py runserver` OR `python3 manage.py runserver`
9. Now, fire up a new terminal and type in `npm start` to start the Voting DApp.
