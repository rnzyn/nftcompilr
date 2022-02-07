from PIL import Image

from .base import NFTBase


class ImageComposite:
    def __init__(self, image_attri: NFTBase):
        self._taken_from = image_attri
        self.output = ""

    def showLog(self):
        print(self._taken_from.composition)
        print(self._taken_from.dna)

    def setOutPutPath(self, path: str):
        self.output = path

    def genByFixSize(self, w: int = 0, h: int = 0):
        canvasim = Image.new('RGBA', (w, h), (255, 255, 255, 0))
        for h in self._taken_from.composition:
            if "_path" in h:
                path = h["_path"]
                print(f"✴️ try to open {path}")
                try:
                    with Image.open(path) as im:
                        print("new image added 🈴", im.format, im.size, im.mode)
                        canvasim = Image.alpha_composite(canvasim, im)
                except:
                    print("error in opening file")

        filename = self._taken_from.dna.replace("0x", "")
        canvasim.save(f"{self.output}/{filename}.png", "PNG")
