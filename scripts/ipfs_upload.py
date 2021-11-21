import os
import typing as tp

import requests

# Custom tpe hints
ResponsePayload = tp.Dict[str, tp.Any]
OptionsDict = tp.Dict[str, tp.Any]
Headers = tp.Dict[str, str]

# global constants
API_ENDPOINT: str = "https://api.pinata.cloud/"


class PinataPy:
    def __init__(self, pinata_api_key: str, pinata_secret_api_key: str) -> None:
        self._auth_headers: Headers = {
            "pinata_api_key": pinata_api_key,
            "pinata_secret_api_key": pinata_secret_api_key,
        }

    @staticmethod
    def _error(response: requests.Response) -> ResponsePayload:
        return {"status": response.status_code, "reason": response.reason, "text": response.text}

    def pin_file_to_ipfs(self, path_to_file: str, options: tp.Optional[OptionsDict] = None) -> ResponsePayload:
        url: str = API_ENDPOINT + "pinning/pinFileToIPFS"
        headers: Headers = self._auth_headers

        def get_all_files(directory: str) -> tp.List[str]:
            """get a list of absolute paths to every file located in the directory"""
            paths: tp.List[str] = []
            for root, dirs, files_ in os.walk(os.path.abspath(directory)):
                for file in files_:
                    paths.append(os.path.join(root, file))
            return paths

        files: tp.Dict[str, tp.Any]

        if os.path.isdir(path_to_file):
            all_files: tp.List[str] = get_all_files(path_to_file)
            files = {"file": [(file, open(file, "rb")) for file in all_files]}
        else:
            files = {"file": open(path_to_file, "rb")}

        if options is not None:
            if "pinataMetadata" in options:
                headers["pinataMetadata"] = options["pinataMetadata"]
            if "pinataOptions" in options:
                headers["pinataOptions"] = options["pinataOptions"]
        response: requests.Response = requests.post(url=url, files=files, headers=headers)
        return response.json() if response.ok else self._error(response)  # type: ignore

