# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"Eu73000","system":"readv2"},{"code":"Eu7zy00","system":"readv2"},{"code":"Eu71z00","system":"readv2"},{"code":"Eu7z.12","system":"readv2"},{"code":"E3...00","system":"readv2"},{"code":"E312.00","system":"readv2"},{"code":"Eu73z00","system":"readv2"},{"code":"Eu84400","system":"readv2"},{"code":"Eu70y00","system":"readv2"},{"code":"E31z.00","system":"readv2"},{"code":"Eu72y00","system":"readv2"},{"code":"E31..00","system":"readv2"},{"code":"Eu84112","system":"readv2"},{"code":"Eu7y000","system":"readv2"},{"code":"E3y..00","system":"readv2"},{"code":"Eu72.00","system":"readv2"},{"code":"Eu7z000","system":"readv2"},{"code":"Eu7y.00","system":"readv2"},{"code":"Eu7z.11","system":"readv2"},{"code":"E311.00","system":"readv2"},{"code":"E30..00","system":"readv2"},{"code":"Eu7yy00","system":"readv2"},{"code":"Eu73y00","system":"readv2"},{"code":"Eu72z00","system":"readv2"},{"code":"Eu70.00","system":"readv2"},{"code":"Eu72000","system":"readv2"},{"code":"E310.00","system":"readv2"},{"code":"Eu7z.00","system":"readv2"},{"code":"Eu7zz00","system":"readv2"},{"code":"Eu73.11","system":"readv2"},{"code":"Eu71.00","system":"readv2"},{"code":"Eu71000","system":"readv2"},{"code":"Eu71.11","system":"readv2"},{"code":"Eu73.00","system":"readv2"},{"code":"Eu70000","system":"readv2"},{"code":"Eu72.11","system":"readv2"},{"code":"E3z..00","system":"readv2"},{"code":"Eu7..00","system":"readv2"},{"code":"Eu7yz00","system":"readv2"},{"code":"Eu70z00","system":"readv2"},{"code":"Eu70.12","system":"readv2"},{"code":"F79","system":"readv2"},{"code":"F71","system":"readv2"},{"code":"F78","system":"readv2"},{"code":"F72","system":"readv2"},{"code":"F73","system":"readv2"},{"code":"F70","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('intellectual-disability-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["developmental-intellectual-disability---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["developmental-intellectual-disability---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["developmental-intellectual-disability---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
