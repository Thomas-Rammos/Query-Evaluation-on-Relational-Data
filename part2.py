# Rammos Thomas
# AM : 4583

# Υλοποίηση του προγράμματος για τη φυσική συνένωση των πινάκων R και S
import csv
import sys

def merge_join(r_file_path, s_file_path, output_file_path):
    with open(r_file_path, 'r') as r_file, open(s_file_path, 'r') as s_file, open(output_file_path, 'w',
                                                                                  newline='') as output_file:
        r_reader = csv.reader(r_file)
        s_reader = csv.reader(s_file)
        output_writer = csv.writer(output_file, delimiter=',')

        r_row = next(r_reader, None)
        s_row = next(s_reader, None)

        while r_row is not None and s_row is not None:
            # Σύγκριση των τιμών του πεδίου Α από R και S
            if int(r_row[0]) < int(s_row[1]):  # Το πεδίο Α του R είναι μικρότερο
                r_row = next(r_reader, None)
            elif int(r_row[0]) > int(s_row[1]):  # Το πεδίο Α του S είναι μικρότερο
                s_row = next(s_reader, None)
            else:  # Ισότητα του πεδίου Α, συνένωση και εγγραφή της γραμμής
                output_writer.writerow([f"{r_row[0]}",f" {r_row[1]}",f" {r_row[2]}",f" {s_row[0]}",f" {s_row[2]}"])

                # Λόγω της υπόθεσης ότι το πεδίο Α είναι primary key στο R και foreign key στο S,
                # και οι δύο πίνακες είναι ταξινομημένοι, διαβάζουμε την επόμενη γραμμή μόνο από το S
                s_row = next(s_reader, None)


merge_join('R.csv', 'S.csv', 'O2.csv')

