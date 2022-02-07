import json
import os
from pathlib import Path

import requests
from requests import Response

from . import multiple_file_types, capPattern
from .base import FileOp

class Pinata(FileOp):
    PINATA_BASE_URL = 'https://api.pinata.cloud/'
    endpointFile = 'pinning/pinFileToIPFS'
    endpointJson = 'pinning/pinJSONToIPFS'
    PINATA_API_KEY = ""
    PINATA_API_SECRET = ""

    def __init__(self):
        self._filepath = ""
        self._scanPath = ""
        self._scanExts = ""
        self._root = ""
        # self._scanMode = False
        self._scanMode = True

    def setAPI(self, key: str, secret: str) -> None:
        self.PINATA_API_KEY = key
        self.PINATA_API_SECRET = secret

    def loadPathFile(self, file_name: str) -> None:
        self._filepath = file_name

    def scanPathForFiles(self, root: str, path: str, exts: list = []) -> None:
        self._root = root
        self._scanPath = path
        self._scanExts = exts
        self._scanMode = True

    def _filename(self, t: str) -> str:
        return t.split('/')[-1:][0]

    def _filenameJson(self, t: str) -> str:
        return t + ".json"

    def pinataIdHash(self, hash_id: str) -> str:
        return f"https://gateway.pinata.cloud/ipfs/{hash_id}"

    @property
    def _headers(self) -> dict:
        return {
            'pinata_api_key': self.PINATA_API_KEY,
            'pinata_secret_api_key': self.PINATA_API_SECRET
        }

    def _execute(self, target: str) -> None:
        with Path(target).open("rb") as fp:
            image_binary = fp.read()
            response = self._postImage(self._filename(target), image_binary)
            # {'IpfsHash': 'QmbtpwG9AtkF9TdWdF7mW4aw7hicqAxB19F1VBKV2fYwjA', 'PinSize': 877361, 'Timestamp': '2021-09-20T18:45:25.607Z'}
            if "IpfsHash" in response.json():
                print("Success uploaded!")
                print(response.json()["IpfsHash"])
                with open(self._filenameJson(target), 'w', encoding='utf-8') as f:
                    json.dump(response.json(), f, ensure_ascii=False, indent=4)

    def _postImage(self, file_name: str, image_bin: any) -> Response:
        response = requests.post(
            self.PINATA_BASE_URL + self.endpointFile,
            files={"file": (file_name, image_bin)},
            headers=self._headers)
        print(response.json())
        return response

    def _postFileJson(self, data: dict) -> Response:
        response = requests.post(
            self.PINATA_BASE_URL + self.endpointJson,
            json=data,
            headers=self._headers)
        print(response.json())
        return response

    def _metadataFound(self, _f_: str) -> bool:
        path_dpj = os.path.join(self._root, self._filenameJson(_f_))
        path_dpi = os.path.join(self._root, _f_)
        f = os.path.abspath(path_dpj)
        h = os.path.abspath(path_dpi)
        # print(f"found - {os.path.isfile(f)}, {f} {h}")
        if os.path.exists(path_dpj):
            print(f"found json {f}")
            return True
        else:
            print(f"can do! {h}")
            return False

    def exeHandleUpload(self):
        if self._scanMode is True:
            os.chdir(self._scanPath)
            alltypes = map(capPattern, self._scanExts)
            for file in multiple_file_types(*alltypes):
                if self._metadataFound(file) is False:
                    self._execute(file)
                    # print("double check..")
        else:
            self._execute(self._filepath)
