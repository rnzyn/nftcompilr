import os
import shutil

from PIL import Image

from .base import NFTBase


class ImageComposite:
    def __init__(self, image_attri: NFTBase, force=False):
        self._taken_from = image_attri
        self.output = ""
        self._fil = ""
        self._force_render = force

    def showLog(self):
        print(self._taken_from.composition)
        print(self._taken_from.dna)

    def setOutPutPath(self, path: str):
        self.output = path

    def _pre(self) -> bool:
        filename = self._taken_from.dna.replace("0x", "")
        self._fil = f"{self.output}/{filename}.png"
        print(f"==> new image complete 🈴 {filename}")
        if self._force_render is False:
            if os.path.isfile(self._fil) is True:
                return True

        return False

    def genByFixSize(self, w: int = 0, h: int = 0) -> "ImageComposite":
        if self._pre() is True:
            return self

        canvasim = Image.new('RGBA', (w, h), (255, 255, 255, 0))
        for h in self._taken_from.composition:
            if "_path" in h:
                path = h["_path"]
                # print(f"✴️ try to open {path}")
                try:
                    with Image.open(path) as im:
                        # print("new image added 🈴", im.format, im.size, im.mode)
                        canvasim = Image.alpha_composite(canvasim, im)
                except:
                    print("error in opening file")

        canvasim.save(self._fil, "PNG")
        return self

    def pngfit(self) -> None:

        if self._pre() is True:
            return

            # $HOME/go/bin/pngquant -i "$f" -o "${f%.*}_.png"
        try:
            if shutil.which("pngquant") is not None:
                os.system(f"pngquant -f \"{self._fil}\" -o \"{self._fil}\"")
        except shutil.Error:
            print("""
            cannot sprink the image since there is no bin PNGQUANT installed.
            maybe try to pull it from [go install github.com/yusukebe/go-pngquant] or install binary from [https://pngquant.org/install.html]
            at pngquant is built with rust.
            """)
