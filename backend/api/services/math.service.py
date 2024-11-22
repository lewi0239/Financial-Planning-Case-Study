import pandas as pd
import numpy as np
import typing import Union
from math import log, pow

# Budgting Formulas


# Debt to Equity Ratio


"""
Debt to Equity Ratio:
As discussed earlier, a derivation of the debt-to-equity ratio is the total debt-to-total-assets ratio. Similar to a business, a leverage ratio can provide information as to the extent to which an individual’s assets are financed through debt rather than equity. The debt-to-assets ratio has some of the same uses as the debt-to-equity ratio, but it expresses the leverage of the individual in a slightly different fashion.

"""


def get_debt_to_equity_ratio(debt: int, equity: int):
    debt_equity = debt / equity
    return debt_equity


"""
Gross Debt Service Ratio:
Most mortgage lenders use the Gross Debt Service Ratio (GDSR) to evaluate an applicant’s ability to service his or her mortgage debt. Included in the calculation are monthly payments associated with the mortgage principal, mortgage interest, and property taxes. In addition, an estimate of monthly heating costs is commonly added to the liability side of the equation by many lending institutions. When the mortgage involves a condominium, condominium fees are part of the equation, and ½ the condo fee is included in the calculation. The GDSR is calculated as:

"""


def get_gross_debt_service_ratio(
    mortgage_pmt: Union[int, float],
    half_condo_fee_rule: Union[int, float],
    property_tax: Union[int, float],
    utilities: Union[int, float],
    annual_gross_income: Union[int, float]
):


gross_monthly_income = annual_gross_income / 12

GDSR = (mortgage_pmt + half_condo_fee_rule +
        property_tax + utilities) / gross_monthly_income

return GDSR


"""
Total Debt Service Ratio:

The most widely accepted guideline for estimating how much of an individual’s income can be allocated to a monthly loan payment is derived through a mathematical equation referred to as the Total Debt Service Ratio (TDSR). This ratio calculates the proportion of all debt obligations relative to the borrower’s gross income. Debts include housing costs such as a mortgage payment, property taxes, and heating, as well as other liabilities such as credit cards, car loans, and other personal loans. The TDSR is calculated as: 

"""


def get_total_debt_service(
    # Costs related to housing (e.g., mortgage, property tax, heating)
    monthly_housing_costs: Union[int, float],
    # Debts like car loans, credit cards
    all_other_monthly_debt_payments: Union[int, float],
    gross_monthly_income: float  # Borrower's gross monthly income
):

    TDSR = (monthly_housing_costs + all_other_monthly_debt_payments) /
    gross_monthly_income


return TDSR


"""
Cash Flow Unlike a net worth statement, which is an overview of financial health calculated at a single point in time, a cash flow statement is a detailed description of cash inflows and outflows over a stated period of time. Often times, we may look at our bank or credit card statements and be surprised by how much we’ve actually spent. Indeed, without proper accounting or record keeping, it’s easy to lose track of our expenses. The most effective way to address this problem is by constructing a personal cash flow statement. 


"""


def get_net_cash_flow(cash_flow_in: int, cash_flow_out: int):
    net_cash_flow = cash_flow_in - cash_flow_out
    return net_cash_flow


# Insurance Formulas:

# Investing Formulas:


# TVM


def tvm_pv(fv: float, i: float, n: float) -> float:
    """Calculate Present Value (PV)."""
    return fv / ((1 + i) ** n)


def tvm_fv(pv: float, i: float, n: float) -> float:
    """Calculate Future Value (FV)."""
    return pv * (1 + i) ** n


def tvm_n(pv: float, fv: float, i: float) -> float:
    """Calculate Number of Periods (N)."""
    return log(fv / pv) / log(1 + i)


def tvm_i(pv: float, fv: float, n: float) -> float:
    """Calculate Interest Rate (i)."""
    return (fv / pv) ** (1 / n) - 1


def tvm_pmt(pv: float, i: float, n: float) -> float:
    """Calculate Fixed Payment (PMT)."""
    return (pv * i * (1 + i) ** n) / ((1 + i) ** n - 1)


def retirement_savings_goal(fv: float, i: float, n: float) -> float:
    """Calculate Retirement Savings PMT."""
    return (fv * i) / ((1 + i) ** n - 1)


def loan_balance(pv: float, i: float, n: float, pmt: float) -> float:
    """Calculate Remaining Loan Balance."""
    return pv * (1 + i) ** n - pmt * (((1 + i) ** n - 1) / i)
