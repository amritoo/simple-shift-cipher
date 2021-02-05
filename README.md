# Simple shift cipher

A simple shift ciper that shifts forwards every _even_ position character by `17` and _odd_ ones by `21` positions.

## How to run

Python 3 is required to run this program.

For the _encryption_ file:

    python3 encryption.py

For the _keys_ file:

```
Usage: python3 keys.py -{e|d} <file> [output]
        -e      : encrypt
        -d      : decrypt
```

For example -

    python3 keys.py -e input_file
