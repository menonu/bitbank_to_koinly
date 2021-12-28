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

HEADER = ['Koinly Date','Pair','Side','Amount','Total','Fee Amount','Fee Currency','Order ID','Trade ID']

cin = csv.reader(sys.stdin)
header = next(cin)
cout = csv.writer(sys.stdout)
cout.writerow(HEADER)

for line in cin:
    d = parser.parse(line[9]).replace(tzinfo=JST).astimezone(tz=timezone.utc)
    pair = line[2].replace('bcc', 'bch')
    side = line[4]
    amount = line[5]
    total = Decimal(line[5]) * Decimal(line[6])
    fee = line[7]
    fee_currency = pair.split('_')[1]
    orderid = line[0]
    tradeid = line[1]
    cout.writerow([d, pair, side, amount, total, fee, fee_currency, orderid, tradeid])
