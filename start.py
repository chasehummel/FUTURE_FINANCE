import pandas as pd
import math
import numpy as np



def get_tax_brackets_dataframe():
    return pd.read_csv("tax brackets single filer.xlsx")

"""
Written by ChatGPT
"""
def compute_tax_from_tax_brackets(taxable_income, tax_brackets):
    previous_bracket_end = 0
    income_left_to_tax = taxable_income
    total_tax = 0
    for bracket in tax_brackets:
        bracket_difference = bracket[0] - previous_bracket_end
        if income_left_to_tax > bracket_difference:
            total_tax += bracket_difference * bracket[1]
            income_left_to_tax -= bracket_difference
        else:
            total_tax += income_left_to_tax * bracket[1]
            break
        previous_bracket_end = bracket[0]
    return total_tax

"""
Written by ChatGPT
"""
def compute_effective_tax_rate(taxable_income, tax_brackets):
    tax = compute_tax_from_tax_brackets(taxable_income, tax_brackets)
    return tax / taxable_income

def compute_taxes(taxable_income, effective_tax_rate):
    return taxable_income * effective_tax_rate







FEDERAL_TAX_BRACKETS = [(10275, 0.10), (41775, 0.12), (89075, 0.22), (170050, 0.24), (215950, 0.32), (539900, 0.35), (float('inf'), 0.37)]
STATE_TAX_BRACKETS = [(10099, 0.01), (23942, 0.02), (37788, 0.04), (52455, 0.06), (66295, 0.08), (338639, 0.09), (float('inf'), 0.11)] # california
CAPITAL_GAINS_TAX_RATE = 0.15


print(compute_tax_from_tax_brackets(200000, STATE_TAX_BRACKETS))



# chat gpt omegalul

def calculate_net_worth(current_salary_func, saved_money_percent_invested, investment_return_func, years_into_future, contribution_401k_percent, expenses_func):

    # create fields to be incremented
    total_portfolio = [0]
    total_cash_savings = [0]

    # iterate through future years and calculate net worth
    for year in range(years_into_future):
        # get the pre tax salary
        pre_tax_salary = current_salary_func(year)
        # apply tax deductibles to salary
        contribution_401k = pre_tax_salary * contribution_401k_percent
        # get total taxable income
        total_taxable_income = pre_tax_salary - contribution_401k
        # get your income after tax
        post_tax_income = total_taxable_income - compute_tax_from_tax_brackets(total_taxable_income, STATE_TAX_BRACKETS) - compute_tax_from_tax_brackets(total_taxable_income, FEDERAL_TAX_BRACKETS)
        # get money left over for this year and add to total cash savings
        current_cash_savings = post_tax_income - expenses_func(year)
        total_cash_savings.append(total_cash_savings[-1] + current_cash_savings)
        # check if you just got out of debt, if so your current cash savings is actually just equal to your total cash savings
        if current_cash_savings > total_cash_savings[-1]:
            current_cash_savings = total_cash_savings[-1]
        
        # get your percent saved
        invested_savings = 0 
        # if you made money this year and you have no debt to pay off
        if current_cash_savings > 0 and total_cash_savings[-1] >=0:
            invested_savings = current_cash_savings * saved_money_percent_invested
            total_cash_savings[-1] -= invested_savings
            # apply gains from previous year and then add in contributions for this year (should be continuous irl)
            total_portfolio.append(total_portfolio[-1] * 1 + investment_return_func(year))
            total_portfolio[-1] += invested_savings + contribution_401k
        else:
            total_portfolio.append(0)

    return total_cash_savings, total_portfolio



# define params
salary_func = lambda x : 100000 + math.sqrt(x) * 30000
saved_money_percent_invested = 0.5
investment_return_func = lambda x : 0.04 * np.cos(2 * math.pi / 5 * x) + 0.02
years_into_future = 5
contribution_401k_percent = .1
expenses_func = lambda x : 65000 + x * 4000


cash, stock = calculate_net_worth(salary_func, saved_money_percent_invested, investment_return_func, years_into_future, contribution_401k_percent, expenses_func)
print(f"Cash {cash[-1]} and stock {stock[-1]}")
