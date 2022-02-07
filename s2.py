from nftcompilrc.classimagecomps import ImageComposite
from nftcompilrc.yc import NFTLayerComposite

"""
Step2:
the NFT layer composite is here.
"""


class Comps(ImageComposite):
    def metaComposite(self, n: int) -> dict:
        return {
            "image": "---",
            "name": "Pys Girl #1",
            "description": "Sometime we need to take some attention to it.",
        }


instance = NFTLayerComposite()
instance.recoverFrom("/Users/hesdx/Documents/b95/nftcompilr/test/scanned_context.json")

for n in range(1000):
    p = Comps(instance.GetRandomRen())
    p.setOutPutImage("/Users/hesdx/Documents/b95/nftcompilr/test/prenft")
    p.setOutPutMeta("/Users/hesdx/Documents/b95/nftcompilr/test/premeta")
    # p.showLog()
    p.compose(300, 300).pngfit()
