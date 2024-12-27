from typing import Type
import csv 
from datetime import datetime

class SparkasseDialect(csv.Dialect):
    delimiter = ';'
    quotechar = '"'
    doublequote = True
    skipinitialspace = True
    lineterminator = '\n'
    quoting = csv.QUOTE_MINIMAL

class Transaction():
    amount = 0.0
    date = ''
    note = ''
    currency = 'EUR'
    payee = ''

    def __init__(self):
        pass

def read(path: str):
    data = []
    with open(path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, dialect=SparkasseDialect)

        for row in csv_reader:
            data.append(row)

    return data

def objectify(data: list):
    transactions = []

    for row in data:
        transaction = Transaction()
        
        try:
            date = datetime.strptime(row['Valutadatum'], '%d.%m.%y')
            transaction.date = date.strftime('%d.%m.%Y')
        except ValueError:
            print(f'Error parsing date: {row["Valutadatum"]}')
            continue
        
        transaction.amount = row['Betrag']

        payee = row['Beguenstigter/Zahlungspflichtiger']
        if payee is None:
            print(f'Error parsing payee: {row["Beguenstigter/Zahlungspflichtiger"]} date: {row["Valutadatum"]}')
            continue

        transaction.payee = payee
        transaction.note = payee + ' /// ' + row['Verwendungszweck']
        
        transaction.currency = row['Waehrung']

        transactions.append(transaction)

    return transactions

def write(data: list, path: str):
    preparedList = []

    for t in data:
        d = {
            'date': t.date,
            'amount': t.amount,
            'payee': t.payee,
            'note': t.note,
            'currency': t.currency
        }
        preparedList.append(d)

    with open(path, mode='w', newline='') as file:
        fieldnames = ['date', 'amount', 'payee', 'note', 'currency']
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')

        writer.writeheader()

        for row in preparedList:
            writer.writerow(row)

def convert(inPath: str, outPath: str):
    print(f'Converting {inPath} to {outPath}')

    rawData = read(inPath)
    transactions = objectify(rawData)
    write(transactions, outPath)

    print('Conversion done')