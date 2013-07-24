##pymfinder

**pymfinder** is Python package with which to find network motifs in complex networks and to analyze a growing list of network-motif related *stuff*.

At its core, pymfinder is a combination of Python methods for network-motif analysis as well as a Python wrapper for the _original_ mfinder version 1.2 written in C and available on [Uri Alon's website](http://www.weizmann.ac.il/mcb/UriAlon/). This code has been included and modified here with the explicit consent of [Nadav Kashtan](mailto:nadav.kashtan@gmail.com), the author of mfinder 1.2.


## Installation instructions


Installation should be relatively straightforward using the included `setup.py`. In fact, it should be as simple as navigating to the directory where you cloned the git repository ('pymfinder/') and running

	python setup.py install

If you receive an error about 'Permission denied' or something similar, you most likely don't have permission to install pymfinder in the global Python site-packages or dist-packages directory. In that case, you can install it locally by adding the `--user` option

	python setup.py install --user

If you still cannot install pymfinder, please check [the issues page](https://github.com/stoufferlab/pymfinder/issues/) and, if your problem isn't listed, create a new one.