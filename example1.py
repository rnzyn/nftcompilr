from nftcompilrc import NFTLayerComposite, ImageComposite

instance = NFTLayerComposite()
instance.inputFolder("/Users/hesdx/Documents/b95/nftcompilr/test/bb")
instance.compositeContext("/Users/hesdx/Documents/b95/nftcompilr/test/scanned_context.json")
# instance.compositeDNA()
#instance.recoverFrom("/Users/hesdx/Documents/b95/nftcompilr/test/scanned_context.json")
ok = instance.GetRandomRen()

p = ImageComposite(ok)