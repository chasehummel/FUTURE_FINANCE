import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
from start import calculate_net_worth, STATE_TAX_BRACKETS, FEDERAL_TAX_BRACKETS

cash_total = []
stock_total = []
legend_out = []
years_into_future = 10
for salary_dif in np.arange(-10000, 10000, 1000):
    for expense_dif in np.arange(1000, 10000, 1000):
        # define params
        salary_func = lambda x : 100000 + math.sqrt(x) * 30000 + salary_dif
        saved_money_percent_invested = 0.5
        investment_return_func = lambda x : 0.04 * np.cos(2 * math.pi / 5 * x) + 0.02
        contribution_401k_percent = .1
        expenses_func = lambda x : 65000 + x * 4000 + expense_dif
        cash, stock = calculate_net_worth(salary_func, saved_money_percent_invested, investment_return_func, years_into_future, contribution_401k_percent, expenses_func)
        cash_total.append(cash)
        stock_total.append(stock)
        legend_out.append(str(expense_dif))
# plot cash and stock
plt.figure()
for cur_cash in cash_total:
    plt.plot(np.arange(1, years_into_future + 1), cur_cash[1:])
plt.legend(legend_out)
plt.title("CASH FLOW vs Extra Expenses per month")
plt.xlabel("Years into the future")
plt.ylabel("Amount (USD)")
plt.show()

plt.figure()
for cur_stock in stock_total:
    plt.plot(np.arange(1, years_into_future + 1), cur_stock[1:])
plt.legend(legend_out)
plt.title("PORTFOLIO vs Extra Expenses per month")
plt.xlabel("Years into the future")
plt.ylabel("Amount (USD)")
plt.show()
