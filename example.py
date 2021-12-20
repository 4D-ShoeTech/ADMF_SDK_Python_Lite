#!/usr/bin/env python
# -*- coding: utf-8 -*-


from admf_python_lite import AdmfLite


admf = AdmfLite(r"/Users/yushihang/Documents/未命名文件夹/temp/1/4ab4670aca655f15ecff359e760c45b1.admf")

isValid = admf.isValid()

file = admf.getBinaryFile('137_Base.png')
file1 = admf.getBinaryFile('137_Base1.png')
isValid = isValid
