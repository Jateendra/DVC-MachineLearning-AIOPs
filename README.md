## wokflow -
<img src="others/images/simple-workflow-01@2x.png" alt="workflow" width="70%">

# STEPS:
## STEP 01: Create a empty remote repository

DVC-MachineLearning-AIOPs

## STEP 02: intialize a git local repository and connect to remote repository

* open and project folder in VS code then follow below command -

```bash
echo "# DVC-MachineLearning-AIOPs" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Jateendra/DVC-MachineLearning-AIOPs.git
git push -u origin main
```

```bash
git init
git remote add origin https://github.com/Jateendra/DVC-MachineLearning-AIOPs.git
touch .gitignore
touch README.md
```
content of the gitignore can be found from reference repository

##### How to push the content to Github :

```bash
git status
git add .
git commit -m "first commit"
git branch -M main
git push origin main

```

## STEP 03: create and activate conda environment

```bash
conda create -n dvc-ml python=3.7 -y
source activate dvc-ml
```


## STEP 05: create requirement file and install dependencies
```bash
touch requirements.txt
pip install -r requirements.txt
```
content of requirements.txt - Refer the reference repository

## STEP 06: initialize dvc
```bash
dvc init
```

If error copy : sqlite3.dll from loc:C:\Users\jatpradh\Anaconda3\DLLs to loc: C:\Users\jatpradh\Anaconda3\envs\dvc-ml\DLLs

```bash
dvc init -f
```

## STEP 04: create a setup file
```bash
touch setup.py
```

paste the below content in the setup.py file and make the necessary changes as per your user ID-

```python
from setuptools import setup

from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="src",
    version="0.0.1",
    author="Jateendra",
    description="dvc-ml pipeline designing",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Jateendra/DVC-MachineLearning-AIOPs",
    author_email="jateendra.pradhan@gmail.com",
    packages=["src"],
    python_requires=">=3.7",
    install_requires=[
        'dvc',
        'pandas',
        'scikit-learn'
    ]
)
```


## STEP 05: create requirement file and install dependencies
```bash
touch requirements.txt
pip install -r requirements.txt
```
content of requirements.txt - Refer the reference repository

## STEP 06: initialize dvc
```bash
dvc init
```

## STEP 07: create the basic directory structure

```bash
mkdir -p src/utils config
```
## STEP 08: create the config file 
```bash
touch config/config.yml
```
content of config.yml - 

```yaml

data_source: http://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv

artifacts: 
  artifacts_dir: artifacts
  raw_local_dir: raw_local_dir
  raw_local_file: data.csv


```


## STEP 09: create the stage 01 python file and all_utils file:
```bash
touch src/stage_01_load_save.py src/utils/all_utils.py
```
content of both these files can be refererd from the reference given


## STEP 10: create the dvc.yaml file and add the stage 01:
```bash
touch dvc.yaml
```

content of dvc.yaml file -
```yaml
stages:
  load_data:
    cmd: python src/stage_01_load_save.py --config=config/config.yaml
    deps:
      - src/stage_01_load_save.py
      - src/utils/all_utils.py
      - config/config.yaml
    outs:
      - artifacts/raw_local_dir/data.csv
```

## STEP 11: run the dvc repro command
```bash
dvc repo
```

## STEP 12: push the changes to remote repository
```bash
git add .
git commit -m "stage 01 added"
git push origin main
```

## STEP 13 : Sometime dvc repro gives error as below .

```bash
> python src/stage_01_load_save.py --config=config/config.yaml
directory is created at artifacts\raw_local_dir
ERROR: failed to reproduce 'load_data':  output 'artifacts\raw_local_dir\data.csv' is already tracked by SCM (e.g. Git).
    You can remove it from Git, then add to DVC.
        To stop tracking from Git:
            git rm -r --cached 'artifacts\raw_local_dir\data.csv'
            git commit -m "stop tracking artifacts\raw_local_dir\data.csv"

```

So run below , so this will not be pushed to git : (Because we want out data to be tracked by DVC , not Git)

```bash
git rm -r --cached 'artifacts\raw_local_dir\data.csv'
git commit -m "stop tracking artifacts\raw_local_dir\data.csv"
```