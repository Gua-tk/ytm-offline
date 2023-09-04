#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zipfile
import os


class CompressionService:
    def __init__(self):
        pass

    def zip_folder(self, folder_path, output_path):
        with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for root, _, files in os.walk(folder_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    rel_path = os.path.relpath(file_path, folder_path)
                    zipf.write(file_path, arcname=rel_path)
