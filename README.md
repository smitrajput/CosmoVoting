<h1 align="center">CosmoVoting</h1>
<p align="center">Taking Decentralized Voting to the <strong><i>next</i></strong> level</p>

### Setting up the project

1. Clone the repo using `https://github.com/smitrajput/VoteX.git` and `cd` into it
2. To start the ganache instance, type `ganache-cli --port 8546`
3. Start a ganache proxy server using: `ganache-http-proxy`

4. Fire a new terminal in the same folder type `cd Dapp` and then `truffle migrate` to deploy the contracts to the local ganache instance
5. Now, type `cd ..` and create a python3 virtual environment using `python3 -m venv ./venvs/django` OR `virtualenv -p python3 ./venvs/django/bin/`
6. In the same terminal, start the virtual environment using `source ./venvs/django/bin/activate`
7. After making sure pip, python, django are installed in the virtual environment too, type `cd django && pip3 install -r requirements.txt`
8. [In case it doesn't get installed automatically], `pip install wheel`
9. To start the Django server, `cd vote`, followed by `python manage.py runserver` OR `python3 manage.py runserver`
10. Now, fire up a new terminal, `cd` into 'Dapp' directory and type in `npm start` to start the Voting DApp.
