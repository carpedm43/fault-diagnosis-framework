# SHRM
Deep Learning Research Library for Prognostics and Health Management

## Install

```
$ pip install shrm # from PYPI, recommended
# pip install git+https://github.com/carpedm43/shrm.git # from github, Not recommended
```


## Usage

```python
from shrm.data import CWRUDataset
dataset = CWRUDataset(loads = [0,1,2])
print(dataset.__getitem__(0))
```
