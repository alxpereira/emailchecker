#!/usr/bin/python

# author : @alxndr_pereira
# github : github.com/alxpereira

# Dependencies 
# - pyDNS : pip install pyDNS
# - validate_email : pip install validate_email

# Install "pip" Package manager
# - https://pip.pypa.io/en/stable/installing/

import sys
import csv
from validate_email import validate_email

def main():
    if len(sys.argv) < 2:
        print 'Usage : ./checkem.py file.csv'
        sys.exit()
    
    filename = sys.argv[1];

    with open(filename.split('.csv')[0] + '_export.csv', 'w') as csvfile:
        fieldnames = ['email', 'valid']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        with open(sys.argv[1], "rb") as f:
            reader = csv.reader(f, delimiter="\t")

            for i, line in enumerate(reader):
                email = line[0]
                
                try : 
                    is_valid = validate_email(email,verify=True)
                except : 
                    is_valid = True

                writer.writerow({'email': email, 'valid': str(is_valid)})
                print email + ' => ' + str(is_valid)

if __name__ == "__main__":
    main()