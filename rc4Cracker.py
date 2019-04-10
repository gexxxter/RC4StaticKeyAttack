#! /usr/bin/python
from argparse import ArgumentParser
import sys


def readFile(fileName):
    with open (fileName, "rb") as infile:
        data = infile.read()
    return data

def main():
    description = """ 
    Decrypts RC4 ciphertexts with static keys.
    The arguments need to be files, output is delivered via stdout.
    """
    parser = ArgumentParser(description=description)
    parser.add_argument("knownPlaintext", help="Known Plaintext")
    parser.add_argument("knownCiphertext", help="Ciphertext derived from knownPlaintext")
    parser.add_argument("unknownCiphertext", help="Ciphertext you want to decrypt")
    args = parser.parse_args()

    knownPlaintext = readFile(args.knownPlaintext)
    knownCiphertext = readFile(args.knownCiphertext)
    unknownCiphertext = readFile(args.unknownCiphertext)

    decrypted = bytearray()
    for i in range(0, len(unknownCiphertext)):
        p = knownPlaintext[i % len(knownPlaintext)]
        c1 = knownCiphertext[i % len(knownCiphertext)]
        c2 = unknownCiphertext[i] 
        decrypted.append(p ^ c1 ^ c2)
        
    sys.stdout.buffer.write(decrypted)


if __name__=='__main__':
	main()
