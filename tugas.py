# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 21:33:09 2020

@author: Kevin
"""

import sqlite3
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

connection = sqlite3.connect('chinook.db')
select_film = '''SELECT  (FirstName || ' ' ||LastName) as CustomerName ,SUM(total) as 'Total Pembelian'
                FROM invoices i
                JOIN customers c
                	ON i.CustomerId = c .CustomerId
                WHERE InvoiceDate BETWEEN '2009-02' AND '2009-06'
                GROUP BY CustomerName;'''
                
order_film = ''' SELECT  (FirstName || ' ' ||LastName) as CustomerName ,SUM(total) as 'Total Pembelian'
                FROM invoices i
                JOIN customers c
                	ON i.CustomerId = c .CustomerId
                WHERE InvoiceDate BETWEEN '2009-02' AND '2009-06'
                GROUP BY CustomerName
                ORDER BY SUM(total) DESC;'''
                                
cursor = connection.cursor()
cursor.execute(select_film)
res = cursor.fetchall()

label = []
data = []
for i in range(0,len(res)):
    label.append(res[i][0])
    data.append(res[i][1])


xpos = np.arange(len(label))
plt.xticks(xpos,label, rotation=90)
plt.title('Penjualan Bulan Februari - Juni')
plt.ylabel("Total Pembelian")
plt.bar(xpos,data)
plt.show()

cursor = connection.cursor()
cursor.execute(order_film)
res = cursor.fetchall()

label = []
data = []
for i in range(0,len(res)):
    label.append(res[i][0])
    data.append(res[i][1])

xpos = np.arange(len(label))
plt.xticks(xpos,label, rotation=90)
plt.title('Penjualan Bulan Februari - Juni (Terurut)')
plt.ylabel("Total Pembelian")
plt.bar(xpos,data)