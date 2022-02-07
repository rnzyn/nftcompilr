import codecs
import json
import time
from dataclasses import dataclass


@dataclass
class NFTBase:
    dna: str
    composition: dict
    attributions: dict

    def __init__(self):
        pass


statement = 'End : {}, IO File {}'


def writeFile(content, filename):
    fo = open(filename, "w")
    fo.write(content)
    fo.close()
    print(statement.format(time.ctime(), filename))


class FileOp:
    def LoadJson2Dict(self, path: any) -> dict:
        return json.load(codecs.open(path, 'r', 'utf-8-sig'))

    def StoreJson(self, pre_dump: any, filepath: str):
        writeFile(json.dumps(pre_dump, ensure_ascii=False), filepath)
