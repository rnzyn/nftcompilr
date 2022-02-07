"""Transaction parameters for use with contract wrappers."""
import codecs
import glob
import itertools as it
import json
import sys
import time
from dataclasses import dataclass

if sys.version_info < (3, 7):
    raise EnvironmentError("Python 3.7 or above is required")

# __version__ = pkg_resources.get_distribution("nftcompilrc").version

def multiple_file_types(*patterns):
    return it.chain.from_iterable(glob.iglob(pattern) for pattern in patterns)


def capPattern(s: str) -> str:
    return f"*.{s}"


def p2f(x: str) -> float:
    return float(x.strip('%')) / 100


"""
usage:


instance = NFTLayerComposite()
instance.inputFolder("/Users/a/Desktop/gamef")


"""
__all__ = [
]
