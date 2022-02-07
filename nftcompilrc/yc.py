"""Transaction parameters for use with contract wrappers."""
import os
import random
import re

from web3 import Web3

from .base import FileOp, NFTBase

"""

[
    {
        "layer":"{folder}"
        "variants":[
            {
                "file": "abc.png",
                "path": "{folder}/{file}",
                "name": "abc",
                "attack": 100.0
            }
            ...
        ]
     }
     ....
]

"""


class NFTLayerComposite(FileOp):
    def __init__(self):
        self._ignore = ["node_modules",
                        ".DS_Store"]
        self._path = ""
        self._preFolder = []
        self._json = []
        super().__init__()

    def inputFolder(self, path: str):
        self._path = path
        self.scan()

    def scan(self):
        folder_list = []
        temp = []
        for i, o, p in os.walk(self._path):
            # os.walk(f).sort(key=int)
            print("当前文件路径%s" % i)
            print("当前路径下所有子文件夹%s" % o)
            print("当前路径下所有文件%s" % p)
            # self._preFolder.append(o)
            if i == self._path:
                print("NFTLayerComposite works..")

                for r in o:
                    folder_list.append(r)

                folder_list.sort(key=lambda f: int(re.sub('\D', '', f)))
                print("folder list is here")
                print(folder_list)
            else:
                layer = dict()
                layer["variants"] = list()
                layer["layer"] = os.path.basename(i)
                folder = i
                print(f"scan the child files for this folder {folder} and the name is {os.path.basename(i)}")
                for file in p:
                    if file in self._ignore:
                        print("ignore this")
                        continue

                    metadata = dict()
                    metadata["_file"] = file
                    metadata["name"] = file.split(".")[0]
                    metadata["_path"] = os.path.join(i, file)
                    metadata["attribute"] = self.configDataFromFileName(file)
                    layer["variants"].append(metadata)

                temp.append(layer)

        for order_f in folder_list:
            for layer in temp:
                if layer["layer"] == order_f:
                    self._json.append(layer)

        print(self._json)

    def configDataFromFileName(self, string_file_data: str) -> dict:
        """
              "attributes": [
                {
                    "trait_type": "cuteness",
                    "value": 100
                }
            ]

        :param string_file_data:
        :return:
        """
        return []

    def compositeContext(self, path: str):
        """
        This method is to building the layer of pictures from the given parameters.
        :return:
        """
        self.StoreJson(self._json, path)

    def _checkJsonContext(self):
        if len(self._json) == 0:
            print("There is no context loaded.")
            exit(0)

    def compositeDNA(self):
        self._checkJsonContext()

    def recoverFrom(self, context_file: str):
        self._json = self.LoadJson2Dict(context_file)

    def genDNA(self, items: list) -> str:
        message = "|".join(items)
        ss = Web3.sha3(text=message)
        return Web3.toHex(ss)

    def GetRandomRen(self) -> NFTBase:
        self._checkJsonContext()
        new_dna = []
        compile_list = []
        for order_f in self._json:
            if "variants" in order_f and len(order_f["variants"]) > 0:
                layer_attr = random.choices(order_f["variants"])[0]
                if "name" in layer_attr:
                    new_dna.append(layer_attr["name"])
                compile_list.append(layer_attr)

        n = NFTBase()
        n.dna = self.genDNA(new_dna)
        n.composition = compile_list

        return n
