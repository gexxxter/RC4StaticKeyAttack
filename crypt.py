#! /usr/bin/python
from Crypto.Cipher import ARC4
import base64
from argparse import ArgumentParser

#This is a vulnerable implementation of RC4 never ever do this!

def enc(key,p):
	return ARC4.new(key).encrypt(p)

def dec(key,msg):
	return ARC4.new(key).decrypt(msg)

def readFile(fileName):
    with open (fileName, "r") as infile:
        data = infile.read()
    return data

def main():
    description =""" 
    This is a vulnerable implementation of RC4 never ever do this!
    The flaw in this implemenation is using the same key for all of the encryptions.
    This leads to a vulnerability in wich an attacker could decrypt all encrypted data.
    Find more information in the Readme.md
    """
    parser = ArgumentParser(description=description)
    parser.add_argument("plaintext", help="Data to encrypt")
    args = parser.parse_args()
   
    plaintext =  readFile(args.plaintext)
    
    key = 'Never ever use the same key more than once!!!!'
    encrypted = enc(key, plaintext)
    print(base64.b64encode(encrypted)) 

if __name__=='__main__':
	main()
