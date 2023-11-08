<h1 align="center">
RNAseq_CRC
</h1>

## Introduction
This script is a special request for research in molecular biology, by a Research Assistant Professor at the University of Rochester, NY.
The goal is to gather gene information from a file from gene sequencing.

The goal of this script is to make the tedious task of comparing these files much 
faster and efficient, allowing more time for meaningful research.

This script has been tailored to the researcher's immediate needs.

## Installation
To install this web application:
- Clone this project to your local disk.
```bash
$ cd path/to/the/project
$ git clone https://github.com/franfif/RNAseq_CRC.git
```
- Create and open a virtual environment:
```bash
$ python3 -m venv env
$ source env/bin/activate 
```
- Run the server through the console.
```bash
$ python3 mine_PGC1a_exp_CRC_patients.py
```


## How to use the script
### Follow the instructions
  - Type or choose the sample file
The sample file is [...]
  - Type or chose the parent folder of the lookup files
    - The parent folder is the folder that contains all the folders indicated in the sample 
      file column "File ID".<br>
    - The lookup files are the files indicated in the sample file column "File Name".
  - Type the name of the gene to look for, then confirm
    - The gene's name will be found in the column "gene_name" of the lookup files.

### Moving the script for convenience
You can move the script to place it in the same folder as the sample file and the parent folder.<br>
This way, the script will find and suggest to use this file and this folder, for more convenience.

If the script is in another folder, simply provide the absolute path of the file and parent folder.
