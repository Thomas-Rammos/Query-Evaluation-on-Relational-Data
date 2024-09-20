# Rammos Thomas
# AM : 4583

import csv
import sys
def evaluate_query(r_file_path, s_file_path, output_file_path):
    # Ανοίγουμε τα αρχεία R και S για ανάγνωση και το αρχείο O3.csv για εγγραφή
    with open(r_file_path, 'r') as r_file,open(s_file_path, 'r') as s_file ,open(output_file_path, 'w',newline='') as output_file:
        r_reader = csv.reader(r_file)
        s_reader = csv.reader(s_file)
        output_writer = csv.writer(output_file, delimiter=',')

        # Αρχικοποίηση των μεταβλητών
        r_row = next(r_reader, None)
        s_row = next(s_reader, None)
        current_a_value = None
        sum_e = 0

        # Επανάληψη για κάθε γραμμή των αρχείων R και S
        while r_row is not None and s_row is not None:
            r_a, r_c = int(r_row[0]), int(r_row[2])
            s_d, s_a, s_e = int(s_row[0]), int(s_row[1]), int(s_row[2])

            # Όταν το R.A είναι μικρότερο από το S.A, μετακινούμαστε στην επόμενη γραμμή του R
            if r_a < s_a:
                r_row = next(r_reader, None)
            # Όταν το S.A είναι μικρότερο από το R.A, μετακινούμαστε στην επόμενη γραμμή του S
            elif s_a < r_a:
                s_row = next(s_reader, None)
            # Όταν βρίσκουμε ταίριασμα και το R.C είναι 7
            else:
                if r_c == 7:
                    # Αν έχουμε νέο κλειδί Α, εγγράφουμε το προηγούμενο άθροισμα στο αρχείο
                    if current_a_value is not None and current_a_value != s_a:
                        output_writer.writerow([f"{current_a_value}", f" {sum_e}"])
                        sum_e = 0  # Μηδενισμός του αθροίσματος για το νέο κλειδί Α
                    current_a_value = s_a
                    sum_e += s_e  # Προσθήκη της τιμής S.E στο άθροισμα
                # Μετακίνηση στην επόμενη γραμμή του S
                s_row = next(s_reader, None)

        # Εγγραφή του τελευταίου άθροισματος αν υπάρχει
        if current_a_value is not None:
            output_writer.writerow([f"{current_a_value}", f" {sum_e}"])


# Κλήση της συνάρτησης
evaluate_query('R.csv', 'S.csv', 'O3.csv')
