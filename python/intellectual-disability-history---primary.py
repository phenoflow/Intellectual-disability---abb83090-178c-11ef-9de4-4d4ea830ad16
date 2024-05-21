# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"106219.0","system":"readv2"},{"code":"32952.0","system":"readv2"},{"code":"22760.0","system":"readv2"},{"code":"19445.0","system":"readv2"},{"code":"102234.0","system":"readv2"},{"code":"106249.0","system":"readv2"},{"code":"100730.0","system":"readv2"},{"code":"32511.0","system":"readv2"},{"code":"108881.0","system":"readv2"},{"code":"106247.0","system":"readv2"},{"code":"106248.0","system":"readv2"},{"code":"106272.0","system":"readv2"},{"code":"41391.0","system":"readv2"},{"code":"43447.0","system":"readv2"},{"code":"43445.0","system":"readv2"},{"code":"106274.0","system":"readv2"},{"code":"100965.0","system":"readv2"},{"code":"43436.0","system":"readv2"},{"code":"106276.0","system":"readv2"},{"code":"100729.0","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('intellectual-disability-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["intellectual-disability-history---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["intellectual-disability-history---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["intellectual-disability-history---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
