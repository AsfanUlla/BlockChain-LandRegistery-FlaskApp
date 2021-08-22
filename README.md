# BlockChain-LandRegistery-FlaskApp

## Requirements
* truffle
* eth blockchain

## pre-installation
update host and port in ```truffle-config.js```

## Installation
```
truffle migrate
pip install -r requirements.txt
```

## post-installation
update values of variables represented by ```<>``` in ```utils.py```
* note - contract address's are returned by the blockchain when they are deployed to the blockchain using the migrate command

## Run
```
uwsgi -i uwsgi.ini
```
* front end is simple html and jquery copy the code to root of your nginx server and update ```uri``` & ```s_url``` variables if necessary

## License :
https://github.com/AsfanUlla/BlockChain-LandRegistery-FlaskApp/blob/main/LICENSE
