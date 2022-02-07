from nftcompilrc.classimagecomps import ImageComposite
from nftcompilrc.yc import NFTLayerComposite

instance = NFTLayerComposite()
instance.inputFolder("/Users/hesdx/Documents/b95/nftcompilr/test/bb")
instance.compositeContext("/Users/hesdx/Documents/b95/nftcompilr/test/scanned_context.json")

instance.recoverFrom("/Users/hesdx/Documents/b95/nftcompilr/test/scanned_context.json")
instance.compositeDNA()

for n in range(10):
    p = ImageComposite(instance.GetRandomRen())
    p.setOutPutPath("/Users/hesdx/Documents/b95/nftcompilr/test/prenft")
    p.showLog()
    p.genByFixSize(300, 300)
