# About Sub3num

Sub3num is a python wordlist-based DNS subdomain scanner.
This script just perform a lookup A records for the domains yet,
and then print the results.

# Usage
```
python3 subdomain.py [-h] -d DOMAIN [-v]
```

* To list all the basic options and switches use -h switch

  ``python3 subdomain.py -h | python3 subdomain.py --help``
* To enumerate subdomains of specific domain:
  
  ``python3 subdomain.py -d example.com | python3 subdomain.py --domain example.com``


* To enumerate subdomains of specific domain and show the results in realtime:

  ``python3 subdomain.py -v | python3 subdomain.py --verbose``
  
## Options:
```
-h, --help                  show this help message and exit
-d DOMAIN, --domain DOMAIN  Target domains(sperated by commas)
-v, --verbose               Verbose mode
```

# Installation
``git clone https://github.com/Muhammetcansimsek/sub3num.git``

``pip install -r requirements.txt``

*Thanks for taking time to read, hope it was usefull*
