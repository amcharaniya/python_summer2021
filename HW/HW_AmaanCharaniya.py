#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 12:18:30 2021

@author: amaancharaniya
"""

class Stock(object):
    def __init__(self, price, symbol):
        self.price = price
        self.symbol = symbol
        

class MutualFund(object):
    def __init__(self,symbol):
        self.symbol = symbol
        
        
        
class Portfolio(object):
    def __init__(self, stockshares, mutualfunds, Cash):
        self.stockshares = stockshares
        self.mutualfunds = mutualfunds
        self.Cash = Cash
        self.stocklist = {}
        self.mutualfundlist = {}
        self.history = []
    def addCash(self, Portfolio, cash):
        self.Cash += cash
    def withdrawCash(self, Portfolio, cash):
        self.Cash -= cash
    def buyStock(self, stockshares, symbol):
        if self.stockshares >= self.Cash:
            print('You need more money')
        else:
            self.Cash -= stockshares*10
            if symbol in self.stocklist:
                self.stocklist[symbol] += stockshares 
            else: self.stocklist[symbol] = stockshares
        self.history.append('Purchased {} shares of {}'.format(stockshares,symbol))
    def sellStock(self, stockshares, symbol):
        if symbol not in self.stocklist:
            print('You do not own this stock')
        else:
            self.stocklist[symbol] -= stockshares
            self.Cash += 20*stockshares
        self.history.append('Sold {} shares of {}'.format(stockshares,symbol))
    def buyMutualFund(self, mutualfunds, symbol):
        if mutualfunds >= self.Cash:
            print('You need more money')
        else:
            self.Cash -= mutualfunds
            if symbol in self.mutualfundlist:
                self.mutualfundlist[symbol] += mutualfunds 
            else: 
                self.mutualfundlist[symbol] = mutualfunds
            self.history.append('Purchased {} shares of {}'.format(mutualfunds,symbol))
    def sellMutualFund(self,mutualfunds,symbol):
       if symbol not in self.mutualfundlist:
           print('You do not own this fund')
       else:
           self.mutualfundlist[symbol] -= mutualfunds
           self.Cash += mutualfunds
           self.history.append('Sold {} shares of {}'.format(mutualfunds,symbol))

portfolio = Portfolio(0,0,0) #Creates a new portfolio
portfolio.addCash(portfolio, 300.50)
s = Stock(20, "HFH") 
portfolio.buyStock(5, s) 
mf1 = MutualFund("BRT") 
mf2 = MutualFund("GHT") 
portfolio.buyMutualFund(10.3, mf1)
portfolio.buyMutualFund(2, mf2) 
print(portfolio)
portfolio.sellMutualFund(3, mf1)
portfolio.sellStock(1, s)
portfolio.withdrawCash(portfolio, 50)
portfolio.history
