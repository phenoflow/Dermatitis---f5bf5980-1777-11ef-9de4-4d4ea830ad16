# Kuan V, Denaxas S, Gonzalez-Izquierdo A, Direk K, Bhatti O, Husain S, Sutaria S, Hingorani M, Nitsch D, Parisinos C, Lumbers T, Mathur R, Sofat R, Casas JP, Wong I, Hemingway H, Hingorani A, 2024.

import sys, csv, re

codes = [{"code":"M124400","system":"readv2"},{"code":"M122000","system":"readv2"},{"code":"M2y4100","system":"readv2"},{"code":"M12zz00","system":"readv2"},{"code":"M12yB00","system":"readv2"},{"code":"M12y011","system":"readv2"},{"code":"M126500","system":"readv2"},{"code":"M123200","system":"readv2"},{"code":"M12y012","system":"readv2"},{"code":"M12z.00","system":"readv2"},{"code":"M12yD00","system":"readv2"},{"code":"M125500","system":"readv2"},{"code":"M124500","system":"readv2"},{"code":"M126000","system":"readv2"},{"code":"M124111","system":"readv2"},{"code":"M123300","system":"readv2"},{"code":"M130.11","system":"readv2"},{"code":"M123000","system":"readv2"},{"code":"H330.00","system":"readv2"},{"code":"M12yA00","system":"readv2"},{"code":"M120.00","system":"readv2"},{"code":"M126300","system":"readv2"},{"code":"M126600","system":"readv2"},{"code":"M123600","system":"readv2"},{"code":"M125100","system":"readv2"},{"code":"M122300","system":"readv2"},{"code":"M124600","system":"readv2"},{"code":"M12..13","system":"readv2"},{"code":"M124000","system":"readv2"},{"code":"M125200","system":"readv2"},{"code":"M123800","system":"readv2"},{"code":"M124700","system":"readv2"},{"code":"M11..00","system":"readv2"},{"code":"M124300","system":"readv2"},{"code":"M12y800","system":"readv2"},{"code":"M12y811","system":"readv2"},{"code":"M125000","system":"readv2"},{"code":"M125300","system":"readv2"},{"code":"M183100","system":"readv2"},{"code":"M130200","system":"readv2"},{"code":"M12y600","system":"readv2"},{"code":"M116.00","system":"readv2"},{"code":"M12y500","system":"readv2"},{"code":"M125z00","system":"readv2"},{"code":"M121.12","system":"readv2"},{"code":"3355.00","system":"readv2"},{"code":"M126100","system":"readv2"},{"code":"M125400","system":"readv2"},{"code":"M123700","system":"readv2"},{"code":"M123500","system":"readv2"},{"code":"M125z11","system":"readv2"},{"code":"M123100","system":"readv2"},{"code":"M12yC00","system":"readv2"},{"code":"M1...11","system":"readv2"},{"code":"M12z000","system":"readv2"},{"code":"M123400","system":"readv2"},{"code":"M12y700","system":"readv2"},{"code":"M125.00","system":"readv2"},{"code":"M122100","system":"readv2"},{"code":"M12y300","system":"readv2"},{"code":"M12y200","system":"readv2"},{"code":"M12y900","system":"readv2"},{"code":"M126200","system":"readv2"},{"code":"M11z.00","system":"readv2"},{"code":"M124800","system":"readv2"},{"code":"M124200","system":"readv2"},{"code":"M116.11","system":"readv2"},{"code":"2859.0","system":"readv2"},{"code":"L26","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('dermatitis-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["dermatitis-atopccontactotherunspecified---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["dermatitis-atopccontactotherunspecified---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["dermatitis-atopccontactotherunspecified---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
