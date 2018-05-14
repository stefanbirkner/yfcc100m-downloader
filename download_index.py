#!/usr/bin/env python3

import os
import urllib.request
from xml.dom.minidom import parse

def collect(prefix):
    ensuredirs(prefix)
    index = ensure_index_file(prefix)
    for child_prefix in extract_children(index):
        collect(child_prefix)

def ensuredirs(path):
    if not os.path.isdir(path):
        os.makedirs(path)

def ensure_index_file(prefix):
    path = prefix + "index.xml"
    if not os.path.isfile(path):
        download(prefix, path)
    return path

def extract_children(path):
    datasource = open(path)
    doc = parse(datasource)
    return [
        common_prefix.getElementsByTagName("Prefix")[0].firstChild.data
        for common_prefix
        in doc.getElementsByTagName("CommonPrefixes")
    ]

def download(prefix, path):
    url = "https://multimedia-commons.s3-us-west-2.amazonaws.com/?delimiter=/&prefix=" + prefix
    print("Download " + url)
    urllib.request.urlretrieve (url, path)
    return path

collect("data/")