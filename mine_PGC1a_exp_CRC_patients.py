import os
import csv
import io

from pathlib import Path


def get_sample_file():
    files = [
        file
        for file in next(os.walk("./"))[2]
        if not file.startswith(".") and not file.startswith("_")
    ]
    while True:
        print("Name or path of the sample file: ")
        for i, file in enumerate(files):
            print(f"[{i+1}]", file)
        file = input("Select one or type the absolute path to the file: ")
        if os.path.isfile(file):
            return file
        try:
            if file > "0" and os.path.isfile(files[int(file) - 1]):
                return files[int(file) - 1]
        except ValueError:
            pass
        except IndexError:
            pass
        print(
            "\n#### Please enter a positive number or the absolute path to a file. ####"
        )


def get_parent_folder():
    folders = [
        folder
        for folder in next(os.walk("./"))[1]
        if not folder.startswith(".") and not folder.startswith("_")
    ]
    while True:
        print("Name of the common parent folder of the lookup files: ")
        for i, folder in enumerate(folders):
            print(f"[{i+1}]", folder)
        folder = input("Select one or type the absolute path to the folder: ")
        if os.path.isdir(folder):
            return folder
        try:
            if folder > "0" and os.path.isdir(folders[int(folder) - 1]):
                return folders[int(folder) - 1]
        except ValueError:
            pass
        except IndexError:
            pass
        print(
            "\n#### Please enter a positive number or the absolute path to a folder. ####"
        )


def get_gene():
    while True:
        gene = input("What gene do you want to look for? ")
        confirmation = input(f'Looking for gene "{gene}"? [y/n] ')
        if confirmation in ["y", "Y", "yes", "Yes", "YES"]:
            return gene


def write_gene_info():
    sample_file = get_sample_file()
    parent_folder = get_parent_folder()
    gene = get_gene()
    sample_file_copy = Path(sample_file).stem + "_" + gene + ".csv"

    with open(sample_file, "r", newline="") as csv_in, open(
        sample_file_copy, "w", newline=""
    ) as out_csv:
        csv_reader = csv.DictReader(csv_in, delimiter="\t")
        fieldnames = sample_file_columns + column_name_to_copy
        csv_writer = csv.DictWriter(out_csv, delimiter=",", fieldnames=fieldnames)
        csv_writer.writeheader()
        for row in csv_reader:
            file_path = "/".join([parent_folder, row["File ID"], row["File Name"]])
            try:
                with open(file_path, "r", newline="") as lookup_file:
                    next(lookup_file)
                    lookup_reader = csv.DictReader(lookup_file, delimiter="\t")
                    for lookup_row in lookup_reader:
                        if lookup_row["gene_name"] == gene:
                            for col in column_name_to_copy:
                                row[col] = lookup_row[col]
                            csv_writer.writerow(row)
                            break

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
