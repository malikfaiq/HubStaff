from bank.models import BankInfo , BankBranches
from django.db import DatabaseError , transaction
import csv
bank_ls = BankInfo.objects.all().values_list('i_bank_info','name')
bank_dict = {}
for record in bank_ls:
    bank_dict[record[1]] = record[0]

with open('/home/malikfaiq/Downloads/map.csv') as f:
    reader = csv.reader(f,delimiter=',')
    next(reader, None)
    for row in reader:
        bank_codes  = row[1].replace(" ", "").split(',')
        branch_name = row[0]
        branch_address = row[2]
        emirates = row[3]
        for bank_code in bank_codes:
            if bank_code in bank_dict.keys():
                attrs ={}
                attrs ['branch_name'] = branch_name
                attrs ['bank_code_id'] = BankInfo.objects.get(i_bank_info=bank_dict[bank_code]).pk
                attrs ['branch_address'] = branch_address
                attrs ['branch_emirates'] = emirates
                try:
                    bank_branch_obj = BankBranches(**attrs).save()
                except DatabaseError as d:
                    print d

