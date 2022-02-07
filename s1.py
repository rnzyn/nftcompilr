from nftcompilrc.yc import NFTLayerComposite

"""
Step1:
the NFT layer composite is here.
"""


class EC(NFTLayerComposite):
    def configDataFromFileName(self, a: str, b: str) -> dict:
        return [
            {
                "trait_type": b,
                "value": a
            }
        ]


instance = EC()
instance.inputFolder("/Users/hesdx/Documents/b95/nftcompilr/test/bb")
instance.compositeContext("/Users/hesdx/Documents/b95/nftcompilr/test/scanned_context.json")
