# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

def obtain_parameters():
    annual_salary=float(input("Starting Annual Salary: "))
    portion_saved=float(input("Percentage of Salary Saved: "))
    
    return { 
        'annual_salary': annual_salary, 
        'portion_saved': portion_saved, 
       }

def minimum_house_payment(portion_down_payment, total_cost):
    return portion_down_payment*total_cost

def update_current_savings(current_savings, salary_saved, rate_of_return):
    
    return current_savings+current_savings*rate_of_return/12 + salary_saved


def compute_savings(savings_rate):
    
    cp= {
        'portion_down_payment': .25,
        'initial_savings': 0,
        'rate_of_return': 0.04,
        'annual_salary': 150000, 
        'total_cost': 1000000,
        'semi_annual_raise': 0.07  
        }
    
    current_savings=cp['initial_savings']
    
    def updateSalary(month):
        if (month>=6 and month % 6 == 0):
            cp['annual_salary']=cp['annual_salary']*(1+cp['semi_annual_raise'])
    
    for month in range(1,37):
        updateSalary(month)
        salary_saved=cp['annual_salary']*savings_rate/12
        current_savings = update_current_savings(current_savings, salary_saved, cp['rate_of_return'])
        
    return current_savings


def search():
    
    def savings_rate(current_saving):
        return current_saving/10000
    
    def get_next_savings_mag(low, high):
        return (low+high)/2


    steps = 0
    
    minimum_payment = minimum_house_payment(0.25, 1000000)
    
    low=0
    high=10000
    
    current_saving=get_next_savings_mag(low, high)
    
    final_savings = compute_savings(savings_rate(current_saving))
    
    while(abs(final_savings-minimum_payment)>100):
        steps += 1
        if (final_savings<minimum_payment):
            low=current_saving
        else:
            high=current_saving
            
        current_saving = get_next_savings_mag(low, high)
            
        final_savings = compute_savings(savings_rate(current_saving))
        print(final_savings)

      
    print("Out of while", current_saving, steps)
    
    
def house_hunting():
  
    # calc_params.update(obtain_parameters())
    
    search()

house_hunting()# -*- coding: utf-8 -*-

