#!/usr/bin/env python
# -*- coding: utf-8 -*-
from zipfile import ZipFile, ZipExtFile

import bson
import copy


class AdmfLite:
    __bsonZipName: str = "description"

    def __init__(self, admfFilePath: str):
        self.__isOK: bool = False
        self.__admfFilePath: str = admfFilePath
        self.__zipFile: ZipFile = None
        self.__bsonDict: dict = None
        self.__open()

    def __open(self):
        try:
            self.zipFile = ZipFile(self.__admfFilePath)

            with self.zipFile.open(self.__bsonZipName) as bsonBinary:
                bsonContent = bsonBinary.read()
                a = len(bsonContent)

                self.__bsonDict = bson.loads(bsonContent[16:])

            self.__isOK = True
        except Exception as e:
            pass

    def isValid(self) -> bool:
        return self.__isOK

    def bsonDict(self) -> dict:
        return copy.deepcopy(self.__bsonDict)

    def getBinaryFile(self, fileName: str) -> ZipExtFile:
        try:
            return self.zipFile.open(fileName)
        except Exception as e:
            return None

    def close(self):
        self.__isOK = False
        self.__zipFile.close()
        self.__zipFile = None
        self.__bsonDict = {}
