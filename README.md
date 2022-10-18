# RSA algorithm implementation

Simple RSA encryption/decryption demo written in Python.

## Run

Requirements: Python 3.10 or above.

```python
python rsa.py <p> <q> <msg> [-v/--verbose]
```

where

* `p` is the first prime number,
* `q` is the second prime number,
* `msg` is the message you want to encrypt and decrypt,
* `-v` or `--verbose` is the optional flag used to increase verbosity of
output.

**Important**: ensure `p` and `q` are high enough, otherwise the message
will not be decoded correctly.

Example command:

```python
python rsa.py 257 113 'some text' -v
```
