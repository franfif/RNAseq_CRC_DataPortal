<h1 align="center">
RNAseq_CRC
</h1>

## Introduction
Welcome to RNAseq_CRC, a Gene Expression Analysis Script!<br>
RNAseq_CRC stands for RNA sequencing in Colorectal Cancer.

This Python script was specially crafted to support cutting-edge research in molecular biology, commissioned by a dedicated Research Assistant Professor at the prestigious University of Rochester, NY.

### Script Purpose:
The primary objective of this script is to generate a comprehensive report, offering open-access gene expression data for a specific gene of interest. It covers tumor samples and corresponding normal tissue samples from de-identified patients, facilitating vital insights into molecular biology.

### Efficiency Redefined:
This script redefines efficiency by automating the arduous process of comparing these data files. With lightning-fast data analysis and intuitive visualization, it empowers researchers to spend less time on manual tasks and more time on groundbreaking discoveries.

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
