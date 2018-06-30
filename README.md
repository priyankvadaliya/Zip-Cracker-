# Zip Cracker 


This Script Supports Only Zip File in This Verson

You Can Also Use This Script With crunch

Cross-platform Supported

*****************************************************

Usage: zipcracker.py [options] 
```
Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -f FILENAME, --file=FILENAME
                        Please Specify Path of Zip File
  -d DICTIONERY, --dict=DICTIONERY
                        Please Specify Path of Dictionery.
  -o OUTPUT, --output=OUTPUT
                        Please Specify Path for Extracting
  -r RESULT, --result=RESULT
                        Please Specify Path if You Want to Save Result
  -c CRUNCH, --crunch=CRUNCH
                        For Using Passwords Directly from crunch use this
                        arguments: -c True or --crunch True
```
# examples 1:
	- python zipcracker.py -f testfile.zip -d passwords.txt

# examples 2:
	-python zipcracker.py -f testfile.zip -d passwords.txt -o extractdir
