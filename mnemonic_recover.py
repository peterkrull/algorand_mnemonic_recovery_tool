import algosdk

# To find the checksum word (25th) of any mnemonic fill in:
mnemonic_broken  = "your mnemonic goes here"
public_key = "YOURPUBLICKEYGOESHERE"

# Can recover mnemonics with:
# - Single missing word
# - Single invalid word

# Check for valid mnemonic public key pair
def check_mnem_pub(mnemonic,public_key,message = "Mnemonic and public keys match"):
    try:
        if algosdk.mnemonic.to_public_key(mnemonic) == public_key:
            exit(message)
    except algosdk.error.WrongChecksumError: pass
    except algosdk.error.WrongMnemonicLengthError: pass

# Get all 
words = algosdk.wordlist.word_list_raw().split('\n')

print("\n\n\n")

# Detect any non-supported words
for split in mnemonic_broken.split():
    if split not in words:
        mnem_split = mnemonic_broken.split()
        invalid_idx = mnem_split.index(split)
        print("Invalid mnemonic word '{}'".format(split))
        mnem_split.pop(invalid_idx)
        mnemonic_broken = " ".join(mnem_split)

# Do initial check for working mnemonic
check_mnem_pub(mnemonic_broken,public_key,"Mnemonic is functional, skipping search.")

# For each place
for place in range(algosdk.constants.mnemonic_len):

    # Split mnemonic into 'first' and 'last' part
    mnem_split = mnemonic_broken.split()
    if len(mnemonic_broken.split()) == 25:
        first = " ".join(mnem_split[0:place])
        last = " ".join(mnem_split[place+1:algosdk.constants.mnemonic_len])
    elif len(mnemonic_broken.split()) == 24:
        first = " ".join(mnem_split[0:place])
        last = " ".join(mnem_split[place:algosdk.constants.mnemonic_len-1])
    else:
        exit("Unable to recover mnenonics with fewer than 24 words")

    # Loop through all words
    for word in words:
        mnem_try = first + " " + word + " " + last
        if len(mnemonic_broken.split()) == 25:
            check_mnem_pub(mnem_try,public_key,f"Found replacement word '{word}' at place {place+1}\n{mnem_try}")
        elif len(mnemonic_broken.split()) == 24:
            check_mnem_pub(mnem_try,public_key,f"Found missing word '{word}' at place {place+1}\n{mnem_try}")

print("Could not recover mnemonic..")

