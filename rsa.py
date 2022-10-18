import math
import random
import logging
import argparse


def is_prime(num: int) -> bool:
    _sqrt = math.sqrt(num)
    idx = 2
    while idx <= _sqrt:
        if num % idx == 0:
            return False
        idx += 1
    return True


def gcd(a: int, b: int) -> int:
    """Greatest common divisor of a and b."""

    if b == 0:
        return a
    return gcd(b, a % b)


def rprimes(num: int) -> list[int]:
    """Returns list of relatively prime numbers between 1 and num."""

    rprimes = [1]
    for idx in range(2, num + 1):
        if gcd(idx, num) == 1:
            rprimes.append(idx)
    return rprimes


def inverse_modulo(num: int, modulo: int):
    for idx in range(modulo):
        if idx * num % modulo == 1:
            return idx


argparser = argparse.ArgumentParser()
argparser.add_argument('p', type=int)
argparser.add_argument('q', type=int)
argparser.add_argument('msg', type=str)
argparser.add_argument('-v', '--verbose', action='store_true')

args = argparser.parse_args()

logging.basicConfig(
    level=logging.DEBUG if args.verbose else logging.INFO,
    format='[%(levelname)s]:[%(asctime)s.%(msecs)03d]: %(message)s',
    datefmt='%H:%M:%S',
)
logger = logging.getLogger(__name__)

p, q = args.p, args.q
logger.debug(f'p = {p}, q = {q}')

assert is_prime(p), f'p = {p} is not prime'
assert is_prime(q), f'q = {q} is not prime'

msg = args.msg
logger.info(f"msg: '{msg}' or {tuple(ord(c) for c in msg)}")

n = p * q
logger.debug(f'n = {n}')
euler = (p - 1) * (q - 1)
logger.debug(f'euler = {euler}')
_rprimes = rprimes(euler)

# get random rprime from second part of primes list
# e.g. rprimes == [1, 2, 3, 4, 5] => e == random.choice([3, 4, 5])
d = random.choice(_rprimes[(math.floor(len(_rprimes) / 2)):])
logger.debug(f'd = {d}')

e = inverse_modulo(d, euler)
logger.debug(f'e = {e}')

public_key = (d, n)
private_key = (e, n)
logger.info(f'private_key: {private_key}')
logger.info(f'public_key: {public_key}')

logger.info('encrypting...')
encrypted = tuple(
    ord(c) ** public_key[0] % public_key[1]
    for c in msg
)
logger.info(f"encrypted: {encrypted}")

logger.info('decrypting...')
decrypted_numeric = tuple(
    encr ** private_key[0] % private_key[1]
    for encr in encrypted
)
decrypted = ''.join([chr(decr) for decr in decrypted_numeric])
logger.info(f"decrypted: '{decrypted}' or {decrypted_numeric}")
