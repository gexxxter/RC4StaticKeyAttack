# RC4StaticKeyAttack
Attack on weak RC4 implementations that use static keys

# Requirements
For this attack to work a few requirements have to be met.

## 1. The attacker must have the ability to encrypt a known plaintext
In order for this to work you need the ability to encrypt a known plaintext or you need a known plaintext and the
corresponding ciphertext.

## 2. The cipher system must use a static key.
A vulnerable implementation should look something like this.
```python
key = 'Never ever use the same key more than once!!!!'
encrypted = enc(key, plaintext)
print(base64.b64encode(encrypted)) 
```
Notice the static hardcoded key.

If there is no access to the sourcecode of the encrypting system, a static key can be identified by encrypting a known plaintext two times.
If both resulting ciphertext are identical, it´s almost certain that the same encryption key is being used.

An example of such a vulnerable implementation can be found in ```crypt.py```.
Use the script ```crypt.py``` to encrypt a given plaintext twice.
```console
python crypt.py testData/knownPlainTextSmall.txt
H4FXzKw=
python crypt.py testData/knownPlainTextSmall.txt
H4FXzKw=
```
Notice the identical ciphertexts.

# Usage
Find a vulnerable encryptio system and let it encrypt a known plaintext.
Store the corresponding ciphertext.
Then pass the known plaintext, known ciphertext and the ciphertext you want to crack to rc4Cracker.py
```
python3 rc4Cracker.py testData/knownPlainText.txt testData/knownPlainText.rc4 testData/unknownPlainText.rc4
```
The script will return the previously unknown plaintext.

# Disclaimer
This tool should only be used for educational purposes.
It was build with the intention to make the lives of security researchers and pentersters a bit easier.