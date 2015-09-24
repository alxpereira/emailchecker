# EmailChecker
A simple CSV email verifier that checks if an email exists. 

### Version
1.0.0

### Installation

You need to install pip in order to get the dependencies
https://pip.pypa.io/en/stable/installing/

Then install the dependencies :
```sh
$ pip install pyDNS
$ pip install pip install validate_email
```

### Usage

To use the Email Checker script, make sure that your email list is in CSV format and the emails on the 1st column, as in the example.csv file 

Then just run it :
```sh
$ ./checkem.py yourfile.csv
```

This will produce a yourfile_export.csv output with the result of the analysis !
And your done !

### Tech

Email Checker uses the following  techs :

* [Python] - the first basic language
* [pip] - the best package library for Python
* [pyDNS] - DNS queries for dummies 
* [validate_email] - email validator library

### Todo's

 - Better management of the export
 - MX domains check

License
----

WTFPL (Do What the Fuck You Want to Public License) 2004

(Copyleft) 2015 - Alexandre Pereira


**Free Software, Hell Yeah!**

[Python]:https://www.python.org
[pip]:https://pip.pypa.io/en/stable/
[pyDNS]:http://pydns.sourceforge.net/
[validate_email]:https://github.com/syrusakbary/validate_email