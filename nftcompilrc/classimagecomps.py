import os
import shutil

from PIL import Image

from .base import NFTBase, FileOp


class ImageComposite(FileOp):
    def __init__(self, image_attri: NFTBase, force=False):
        self._taken_from = image_attri
        self.output = ""
        self.outputmeta = ""
        self._fil = ""
        self._meta = ""
        self._force_render = force

    def showLog(self):
        print(self._taken_from.composition)
        print(self._taken_from.dna)

    def setOutPutImage(self, path: str):
        self.output = path

    def setOutPutMeta(self, path: str):
        self.outputmeta = path

    def _pre(self) -> bool:
        filename = self._taken_from.dna.replace("0x", "")
        self._fil = f"{self.output}/{filename}.png"
        # print(f"==> new image complete 🈴 {filename}")

        if self.outputmeta != "":
            self._meta = f"{self.outputmeta}/{filename}.json"

        if self._force_render is False:
            if os.path.isfile(self._fil) is True:
                return True

        return False

    def compose(self, w: int = 0, h: int = 0, extra_no: int = 0) -> "ImageComposite":
        if self._pre() is True:
            return self

        canvasim = Image.new('RGBA', (w, h), (255, 255, 255, 0))
        attrbank = []
        for h in self._taken_from.composition:
            if "_path" in h:
                path = h["_path"]

                # print(f"✴️ try to open {path}")
                try:
                    with Image.open(path) as im:
                        # print("new image added 🈴", im.format, im.size, im.mode)
                        aftermod = self.modIm(im)
                        canvasim = Image.alpha_composite(canvasim, aftermod)

                        if "attribute" in h:
                            attr = h["attribute"]
                            attrbank = attrbank + attr

                except:
                    print("error in opening file")
        meta = self.metaComposite(extra_no)
        meta["attributes"] = attrbank
        canvasim.save(self._fil, "PNG")
        self.StoreJson(meta, self._meta)
        return self

    def modIm(self, im: Image) -> Image:
        return im

    def exposeIm(self, im: Image) -> dict:
        pass

    def metaComposite(self, ex: int) -> dict:
        """
        example in here...
        {
          "image": "https://gateway.pinata.cloud/ipfs/QmNVa6BauCLV92F8NQDf7jt5HfcJXcbAuGn247HRwBqr87",
          "name": "Collection SS Girl #1",
          "description": "Its an interesting image of #1. More than 60 skin regions (123) 0x7fd681f45e20",
        }
        :param ex:
        :return:
        """
        pass

    def pngfit(self) -> None:
        if self._pre() is True:
            return
            # $HOME/go/bin/pngquant -i "$f" -o "${f%.*}_.png"
        try:
            if shutil.which("pngquant") is not None:
                os.system(f"pngquant -f \"{self._fil}\" -o \"{self._fil}\"")

            print(f" 🈴 ok-{self._fil}")
        except shutil.Error:
            print("""
            cannot sprink the image since there is no bin PNGQUANT installed.
            maybe try to pull it from [go install github.com/yusukebe/go-pngquant] or install binary from [https://pngquant.org/install.html]
            at pngquant is built with rust.
            """)
