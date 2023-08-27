#!/usr/bin/env python
# -*- coding: utf-8 -*-
import ytmusicapi
headers = "".join(open("../../secrets/headers.txt").readlines())


class UploadService:
    def __init__(self):
        ytmusicapi.setup(filepath="../../secrets/browser.json", headers_raw=headers)


if __name__ == '__main__':
    us = UploadService()

