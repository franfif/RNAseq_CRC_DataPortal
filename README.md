<h1 align="center">
RNAseq_CRC
</h1>

## Introduction
This script is a special request for research in molecular biology, by a Research Assistant Professor 
of the University of Rochester, NY.
The purpose of this script is to create a file that provides open-access expression 
levels of a gene of interest in tumor samples or corresponding normal tissue samples 
from anonymized patients. 

This script makes this tedious task much 
faster and efficient, allowing more time for meaningful research.

This script has been tailored to the researcher's immediate needs.

## Pre-requisites
* [Git](https://git-scm.com/downloads)
* [Python 3.12](https://www.python.org/downloads/release/python-3120/)

## Installation
To install this web application:
- Clone this project to your local disk.
```bash
$ cd path/to/the/project
$ git clone https://github.com/franfif/RNAseq_CRC.git
```

## How to use the script
### Download the files
Before running this script, download the input files from 
the [Genomic Data Commons Data Portal repository](https://portal.gdc.cancer.gov/repository):
- In the "Files" tab, select the following options as such:
  - Data Category: transcriptome profiling, 
  - Data Type: Gene Expression Quantification, 
  - Experimental Strategy: RNA-Seq,
  - Access: open.
- In the "Cases" tab, select the cases of interests.
- In the center part of the page, click on the "Add All Files to Cart" button.
- In the Cart page:
  - Click on the "Sample Sheet" button to download the "Sample Sheet" file,
  - Click on the "Download" button, then on the "Cart" button to download the Processed next generation RNA-Seq data files (aka lookup files).

### Run the script
- Run the script through the console.
```bash
$ python3 mine_PGC1a_exp_CRC_patients.py
```

### Follow the instructions in the script
  - Choose the sample file of type its path.
You should have downloaded a sample file in the previous steps.
  - Type or chose the parent folder of the lookup files
    - The parent folder is the folder that contains all the folders indicated in the sample 
      file column "File ID".
    - The lookup files are the files indicated in the sample file column "File Name".
  - Type the name of the gene to look for, then confirm
    - The gene's name will be found in the column "gene_name" of the lookup files.

### Moving the script for convenience
You can move the script to place it in the same folder as the sample file and the parent folder.<br>
This way, the script will find and suggest to use this file and this folder, for more convenience.

If the script is in another folder, simply provide the absolute path of the file and parent folder.
