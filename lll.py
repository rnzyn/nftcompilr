import os
import re
import json

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


class NFTHelper:
    def __init__(self):
        # self.a = ...
        pass


class NFTLayerComposite(NFTHelper):
    def __init__(self):
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

            # print(folder_list)
            else:
                layer = dict()
                layer["variants"] = list()
                layer["layer"] = os.path.basename(i)
                folder = i
                print(f"scan the child files for this folder {folder} and the name is {os.path.basename(i)}")
                for file in p:
                    metadata = dict()
                    metadata["file"] = p
                    metadata["name"] = str.split(".", file)[0]
                    metadata["path"] = os.path.join(i, file)
                    metadata["attack"] = 100.00
                    layer["variants"].append(metadata)


                print(f"The files are {p}")

                self._json.append(layer)

        print(self._json)

    def compsite(self):
        """
        This method is to building the layer of pictures from the given parameters.
        :return:
        """
        pass


instance = NFTLayerComposite()
instance.inputFolder("/Users/a/Desktop/gamef")
