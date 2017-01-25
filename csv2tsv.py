#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, csv
csv.field_size_limit(sys.maxsize)

try:
    with open(sys.argv[1]) as csvf:
        headers = next(csv.reader(csvf))
except IndexError as e:
    sys.exit("ERROR: use on a csv file such as `python csv2tsv.py file.csv")
except IOError as e:
    sys.exit(e)

with open(sys.argv[1]) as csvf:
    for row in csv.DictReader(csvf):
        print "\t".join([(row[h] or "").replace("\n", " ") for h in headers])

