# YFCC100M Downloader

This repository contains a set for scripts for downloading the images of the
[YFCC100M data set](https://multimediacommons.wordpress.com/yfcc100m-core-dataset/).


YFCC100M Downloader is published under the
[MIT license](http://opensource.org/licenses/MIT). It requires Python 3.

## Download images

Clone this repository or download the two files `download_files.py` and
`download_index.py`.

Execute

    ./download_index.py

It downloads all index files to a folder `data`.

The download the images with

    ./download_files.py

It reads the index files from `data` and downloads the images of the index
files. The images are stored in the `data` folder, too.