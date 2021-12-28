## Specs

* Timezone of output file is UTC
* Need manual copy-and-paste to obtain deposit/withdraw history from bitbank
* Need to add `coin` column manually

## how to use

```
$ cat example_deposit.csv | convert.py > deposit_koinly.csv
$ cat example_withdraw.csv | convert.py > withdraw_koinly.csv
```