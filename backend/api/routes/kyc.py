from typing import Optional, List

# Define what a tax agent:


class TaxAgent:
    def __init__(self, tax_agent_first_name: str, tax_agent_last_name: str, tax_agent_id: str, tax_agent_bussiness_name: str, tax_agent_designation: str):
        self.tax_agent_first_name = tax_agent_first_name
        self.tax_agent_last_name = tax_agent_last_name
        self.tax_agent_id = tax_agent_id
        self.tax_agent_business_name = tax_agent_bussiness_name
        self.tax_agent_designation = tax_agent_designation

    def __str__(self):
        return f"{self.tax_agent_first_name} {self.tax_agent_last_name} works at {self.tax_agent_business_name}"

# Define what an Advisor:


class Advisor:
    def __init__(self, advisor_first_name: str, advisor_last_name: str, advisor_id: str, advisor_bussiness_name: str, advisor_designation: str):

        self.advisor_first_name = advisor_first_name
        self.advisor_lewis_name = advisor_last_name
        self.advisor_id = advisor_id
        self.advisor_business_name = advisor_bussiness_name
        self.advisor_designation = advisor_designation

    def __str__(self):
        return f"{self.advisor_first_name} {self.advisor_last_name} works at {self.advisor_business_name}"


class Client:
    def __init__(self, first_name: str, last_name: str, birthday: str, age: int, street_address: str, postal_code: str, snn: int, has_beneficiary: bool, beneficiary_name: Optional[str], has_life_insurance: bool, has_financial_advisor: bool, advisor_first_name: str, advisor_last_name: str, advisor_id: str, advisor_business_name: str, advisor_designation: str, has_tax_agent: bool, income: dict[str, int], debt: dict[str, int], assets: dict[str, int], investments: dict[str, int], life_insurnace_death_benefit: int, net_worth: int, job_title: str, client_id: str, client_family: Optional[str], client_status: bool):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.age = age
        self.street_address = street_address
        self.postal_code = postal_code
        self.snn = snn
        self.has_beneficiary = has_beneficiary
        self.beneficiary_name = beneficiary_name
        self.has_life_insurance = has_life_insurance
        self.has_financial_advisor = has_financial_advisor
        self.has_tax_agent = has_tax_agent
        self.income = income
        self.debt = debt
        self.assets = assets
        self.investments = investments
        self.life_insurance_death_benefit = life_insurnace_death_benefit
        self.net_worth = net_worth
        self.job_title = job_title
        self.client_id = client_id
        self.client_family = client_family
        self.client_status = client_status

    def __str__(self):
        return f"{self.first_name} {self.last_name} with client id {self.client_id}"

# Make a financial statement that is tied to a family or client:


class NetWorth:
    def __init__(self, client_id: str, assets: dict[str, int], debt: dict[str, int], investments: dict[str, int]):
        self.client_id = client_id
        self.assets = assets
        self.investments = investments
        self.networth = self.calculate_networth()

        def caclulate_networth(self):
            total_assets = sum(self.assets.value()) +
            sum(self.investments.value())
            total_debts = sum(self.debt.value())
            return total_assets - total_debts

    def __str__(self):
        return f"{self.client_id} has ${self.networth}"

# Make a family class for each client:


class Family:
    def __init__(self, client_id: str, family_id: int, client_family: [str], advisor_first_name: str):
        self.client_id = client_id
        self.client_family = client_family
        self.family_id = family_id
        self.advisor_first_name = advisor_first_name

    def get_family_tree(self):
        for member in self.client_family:
            print(member)
        return self.client_family

    def __str__(self):
        return f"The {', '.join(self.client_family)}'s advisor is {self.advisor_first_name}"


# Make class for cases:

class Case:
    def __init__(self, family_id: int, plan_type: list[str], reason_why_letter: str, investment_risk_assessment: str, investments: dict[str, int], insurance: dict[str, int]):
        self.family_id = family_id
        self.plan_type = plan_type
        self.reason_why_letter = reason_why_letter
        self.investment_risk_assessment = investment_risk_assessment
        self.investments = investments
        self.insurance = insurance

    def __str__(self):
        return f"{self.family_id} is currently on {self.plan_type}"
