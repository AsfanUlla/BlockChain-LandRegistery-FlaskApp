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

## License :
https://github.com/AsfanUlla/BlockChain-LandRegistery-FlaskApp/blob/main/LICENSE
