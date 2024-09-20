# Rammos Thomas
# AM : 4583

import csv
import sys

def merge_sort(data, group_by_attr, aggregate_attr, aggregate_func):
    # Βασική περίπτωση: αν το μήκος του πίνακα είναι 1 ή 0, είναι ήδη ταξινομημένος
    if len(data) <= 1:
        return data

    # Διαίρεση του πίνακα σε δύο μέρη
    mid = len(data) // 2
    left_half = data[:mid]
    right_half = data[mid:]
    
    # Αναδρομική κλήση του merge_sort στα δύο μέρη
    left_sorted = merge_sort(left_half, group_by_attr, aggregate_attr, aggregate_func)
    right_sorted = merge_sort(right_half, group_by_attr, aggregate_attr, aggregate_func)
    
    # Συγχώνευση των δύο ταξινομημένων μερών με την τροποποιημενη merge_sort
    return merge(left_sorted, right_sorted, group_by_attr, aggregate_attr, aggregate_func)


def merge(left, right, group_by_attr, aggregate_attr, aggregate_func):
    result = []
    i = j = 0
    # Ενώ υπάρχουν στοιχεία και στις δύο λίστες
    while i < len(left) and j < len(right):
        
        if left[i][group_by_attr] < right[j][group_by_attr]:
            result.append(left[i])
            i += 1
        elif left[i][group_by_attr] > right[j][group_by_attr]:
            result.append(right[j])
            j += 1
        else:
            # Υπολογισμός της συνάθροισης για τις πλειάδες με ίδιο group_by_attr
            if aggregate_func == 'sum':
                aggregated_value = left[i][aggregate_attr] + right[j][aggregate_attr]
            elif aggregate_func == 'min':
                aggregated_value = min(left[i][aggregate_attr], right[j][aggregate_attr])
            else:  # max
                aggregated_value = max(left[i][aggregate_attr], right[j][aggregate_attr])

            # Προσθήκη της συγχωνευμένης πλειάδας στο αποτέλεσμα
            merged_tuple = (left[i][group_by_attr], aggregated_value)
            result.append(merged_tuple)

            # Προχώρηση στο επόμενο στοιχείο για κάθε λίστα
            i += 1
            j += 1

    # Προσθήκη τυχόν υπολειπόμενων στοιχείων
    result += left[i:]
    result += right[j:]

    return result


# Ενημέρωση της συνάρτησης process_file για να χρησιμοποιεί τον προσαρμοσμένο Merge Sort
def process_file(file_name, group_by_attr, aggregate_attr, aggregate_func):
    with open(file_name, mode='r') as file:
        reader = csv.reader(file)
        data = [row for row in reader]

    # Μετατροπή των τιμών σε ακέραιους για τις στήλες συγκεκριμένου ενδιαφέροντος
    for row in data:
        row[group_by_attr] = int(row[group_by_attr])
        row[aggregate_attr] = int(row[aggregate_attr])

    # Αφαίρεση του attribute που δεν είναι ούτε το attribute ομαδοποίησης ούτε το attribute συνάθροισης
    for i, row in enumerate(data):
        data[i] = (row[group_by_attr], row[aggregate_attr])

    # Εφαρμογή του προσαρμοσμένου Merge Sort
    sorted_aggregated_data = merge_sort(data, 0, 1, aggregate_func)

    with open('O1.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        for row in sorted_aggregated_data:
            writer.writerow([f"{row[0]}", f" {row[1]}"])  # Προσθήκη κενού μεταξύ των τιμών
    return sorted_aggregated_data


def main():
    # Έλεγχος αν έχουν δοθεί αρκετά ορίσματα
    if len(sys.argv) < 5:
        print(
            "Usage: script.py <input_file> <group_by_attribute_index> <aggregate_attribute_index> <aggregate_function> <output_file>")
        sys.exit(1)

    # Ανάκτηση των ορισμάτων από τη γραμμή διαταγών
    file_name = sys.argv[1]
    group_by_attr = int(sys.argv[2])
    aggregate_attr = int(sys.argv[3])
    aggregate_func = sys.argv[4]


    # Επεξεργασία του αρχείου και εγγραφή των αποτελεσμάτων
    process_file(file_name, group_by_attr, aggregate_attr, aggregate_func)


if __name__ == "__main__":
    main()

