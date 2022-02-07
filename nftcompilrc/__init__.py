"""Transaction parameters for use with contract wrappers."""
import sys

import pkg_resources

from .yc import NFTLayerComposite, NFTBase, ImageComposite

if sys.version_info < (3, 5):
    raise EnvironmentError("Python 3.5 or above is required")

# __version__ = pkg_resources.get_distribution("nftcompilrc").version

__all__ = [
    ImageComposite,
    NFTBase,
    NFTLayerComposite,

]

"""
usage:


instance = NFTLayerComposite()
instance.inputFolder("/Users/a/Desktop/gamef")


"""
