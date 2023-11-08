import os
import csv
import re

from pathlib import Path


# constants used for os.walk method to retrieve a folder or a file
OS_WALK_FOLDER = 1
OS_WALK_FILE = 2


def get_sample_file():
    # gather all files in current directory
    files = [
        file
        for file in next(os.walk("./"))[OS_WALK_FILE]
        if not file.startswith(".") and not file.startswith("_")
    ]
    while True:
        print("Name or path of the sample file: ")
        # lists all the files in the current directory with a number
        for i, file in enumerate(files):
            print(f"[{i+1}]", file)
        file = input("Select one or type the absolute path to the file: ")
        # if the input is a path to a file, use it
        if os.path.isfile(file):
            return file
        # if the input does not lead to a file:
        try:
            # if the input is a positive number, use the file indicated by the number
            if int(file) > 0 and os.path.isfile(files[int(file) - 1]):
                return files[int(file) - 1]
        # the input is not a number
        except ValueError:
            pass
        # the input is a number too high
        except IndexError:
            pass
        print(
            "\n#### Please enter a positive number or the absolute path to a file. ####"
        )


def get_parent_folder():
    # gather all folders in current directory
    folders = [
        folder
        for folder in next(os.walk("./"))[OS_WALK_FOLDER]
        if not folder.startswith(".") and not folder.startswith("_")
    ]
    while True:
        print("Name of the common parent folder of the lookup files: ")
        # lists all the folders in the current directory with a number
        for i, folder in enumerate(folders):
            print(f"[{i+1}]", folder)
        folder = input("Select one or type the absolute path to the folder: ")
        # if the input is a path to a folder, use it
        if os.path.isdir(folder):
            return folder
        try:
            # if the input is a positive number, use the folder indicated by the number
            if folder > "0" and os.path.isdir(folders[int(folder) - 1]):
                return folders[int(folder) - 1]
        # the input is not a number
        except ValueError:
            pass
        # the input is a number too high
        except IndexError:
            pass
        print(
            "\n#### Please enter a positive number or the absolute path to a folder. ####"
        )


def get_gene():
    # get a gene name from the user
    while True:
        gene = input("What gene do you want to look for? ")
        # ask user to confirm the gene
        confirmation = input(f'Looking for gene "{gene}"? [y/n] ')
        # regular expression matched any input starting with "Y" or "y"
        if re.search("^[Yy].*", confirmation):
            return gene


def write_gene_info():
    sample_file = get_sample_file()
    parent_folder = get_parent_folder()
    gene = get_gene()
    # create a copy of the sample file as a csv
    sample_file_copy = Path(sample_file).stem + "_" + gene + ".csv"

    with (
        open(sample_file, "r", newline="") as csv_in,
        open(sample_file_copy, "w", newline="") as out_csv,
    ):
        # read the sample file
        csv_reader = csv.DictReader(csv_in, delimiter="\t")
        # create list of headers
        fieldnames = sample_file_columns + column_name_to_copy
        # write headers to copy of sample file
        csv_writer = csv.DictWriter(out_csv, delimiter=",", fieldnames=fieldnames)
        csv_writer.writeheader()
        for row in csv_reader:
            # get the lookup file path
            file_path = "/".join([parent_folder, row["File ID"], row["File Name"]])
            try:
                # open the lookup file
                with open(file_path, "r", newline="") as lookup_file:
                    # skip the header row
                    next(lookup_file)
                    # read the lookup file
                    lookup_reader = csv.DictReader(lookup_file, delimiter="\t")
                    # look for the gene in each row
                    for lookup_row in lookup_reader:
                        if lookup_row["gene_name"] == gene:
                            for col in column_name_to_copy:
                                # add the information from the lookup file to the memory of row of the sample file
                                row[col] = lookup_row[col]
                            # write all row to copy of sample file
                            csv_writer.writerow(row)
                            break
            # the file is not where it was expected, let the user know
            except FileNotFoundError:
                print(f"No such file: {file_path}")


sample_file_columns = [
    "File ID",
    "File Name",
    "Data Category",
    "Data Type",
    "Project ID",
    "Case ID",
    "Sample ID",
    "Sample Type",
]

column_name_to_copy = [
    "unstranded",
    "stranded_first",
    "stranded_second",
    "tpm_unstranded",
    "fpkm_unstranded",
    "fpkm_uq_unstranded",
]

if __name__ == "__main__":
    write_gene_info()
