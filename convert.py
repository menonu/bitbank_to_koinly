#!/usr/bin/env python3

import sys
import csv
from dateutil import parser
from dateutil import tz
from datetime import timezone
from decimal import Decimal

JST = tz.gettz('Asia/Tokyo')
DEPOSIT_LINE_LENGTH = 6
WITHDRAW_LINE_LENGTH = 10

HEADER = ["Koinly Date", "Amount", "Currency", 'TxHash']

def is_deposit(l):
    return len(l) is DEPOSIT_LINE_LENGTH

cin = csv.reader(sys.stdin)
header = next(cin)
cout = csv.writer(sys.stdout)
cout.writerow(HEADER)

for line in cin:
    if is_deposit(line):
        d = parser.parse(line[0]).replace(tzinfo=JST).astimezone(tz=timezone.utc)
        amount = line[1]
        tx = line[3]
        currency = line[5]
        cout.writerow([d, amount, currency, tx])
    else:
        d = parser.parse(line[0]).replace(tzinfo=JST).astimezone(tz=timezone.utc)
        amount = -Decimal(line[3])
        tx = line[6]
        currency = line[9]
        cout.writerow([d, amount, currency, tx])