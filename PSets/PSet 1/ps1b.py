# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

def obtain_parameters():
    annual_salary=float(input("Starting Annual Salary: "))
    portion_saved=float(input("Percentage of Salary Saved: "))
    total_cost=float(input("Total Cost of Home: "))
    semi_annual_raise=float(input('Semi-annual Raise: '))
    
    return { 
        'annual_salary': annual_salary, 
        'portion_saved': portion_saved, 
        'total_cost': total_cost,
        'semi_annual_raise': semi_annual_raise
       }

def minimum_house_payment(portion_down_payment, total_cost):
    return portion_down_payment*total_cost

def update_current_savings(current_savings, salary_saved, rate_of_return):
    
    return current_savings+current_savings*rate_of_return/12 + salary_saved


def compute_time(cp):
    current_savings=cp['initial_savings']
    
    minimum_payment = minimum_house_payment(cp['portion_down_payment'], cp['total_cost'])
        
    months = 0
    
    def updateSalary(month):
        if (month>=6 and month % 6 == 0):
            cp['annual_salary']=cp['annual_salary']*(1+cp['semi_annual_raise'])
    
    while (current_savings <= minimum_payment):
        months += 1
        updateSalary(months)
        salary_saved=cp['annual_salary']*cp['portion_saved']/12
        current_savings = update_current_savings(current_savings, salary_saved, cp['rate_of_return'])
        
    return months
    
    
def house_hunting():
    
    calc_params= {
        'portion_down_payment': .25,
        'initial_savings': 0,
        'rate_of_return': 0.04,
        }
  
    calc_params.update(obtain_parameters())
    
    months = compute_time(calc_params)
    
    print("Number of months:", months)

house_hunting()