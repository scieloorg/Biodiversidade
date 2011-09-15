#!/usr/bin/env python
# *-* coding: iso-8859-1 *-*

from csv2tag import csv2tag
from record2id import record2id


input_filename = 'biota-fapesp-FIXED.csv'
separator = ';'
id_filename = 'biota_fapesp_lildbi'
default_content_filename = 'default.seq'
convertion_table_filename = "table.seq"


dv = {}
f = open(default_content_filename,'r')
default_values = f.readlines()
f.close()
for val in default_values:
    if '|' in val:
        v = val.split("|")
        if not v[1]=='':
            dv[v[0]] = v[1].strip('\n')


c2t = csv2tag(convertion_table_filename)
records = c2t.convert(input_filename, separator)

r2id = record2id(id_filename)
for r in records:
    record = r2id.convert(r, dv)
    r2id.save(record)
r2id.close_files()
