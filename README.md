# Algorand Mnemonic Recovery Tool
 This tool will attempt to look for incorrect, missing or misplaced words using brute force and word swapping.

## Prerequisites
* `python3.6+`
* `pip3`
* `py-algorand-sdk`

## Usage

Inside the `mnemonic_recover.py` file there are two variables that need to be filled in. The first is `mnemonic_broken` which will be the 25 word mnemonic you can't import correctly, or 24 word mnemonic if you have lost a word. The second is `public_key` which will be the public key of the account you are trying to recover. With these two filled in, the script can be run using the following command:

```bash
python3 mnemonic_recover.py
```
If an error was found and corrected, it will be printed to the terminal along with the correct mnemonic. 
