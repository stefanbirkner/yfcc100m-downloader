#!/usr/bin/env python3

import os
import urllib.request
from xml.dom.minidom import parse

def collect_index_files(path):
    index_files = []
    for root, subdirs, files in os.walk(path):
        file_path = os.path.join(root, "index.xml")
        if os.path.exists(file_path):
            index_files.append(file_path)
    return index_files

def download_files(paths):
    for path in paths:
        url = "https://multimedia-commons.s3-us-west-2.amazonaws.com/" + path
        print("Download " + url)
        urllib.request.urlretrieve (url, path)

def extract_image_paths(index_files):
    paths = []
    for index_path in index_files:
        doc = parse(index_path)
        for content in doc.getElementsByTagName("Contents"):
            image_path = content.getElementsByTagName("Key")[0].firstChild.data
            paths.append(image_path)
    return paths


def parse_file(path):
    datasource = open(path)
    return parse(datasource)

index_files = collect_index_files("data")
paths = extract_image_paths(index_files)
download_files(paths)
