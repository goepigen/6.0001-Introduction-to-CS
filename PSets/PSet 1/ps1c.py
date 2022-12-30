# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

def minimum_house_payment(portion_down_payment, total_cost):
    """
    portion_down_payment : float, proportion of total cost that is down payment
    cost to buy house
    total_cost : float, total cost of house

    returns: float, minimum house payment

    """
    return portion_down_payment*total_cost

def update_current_savings(current_savings, salary_saved, rate_of_return):
    """
    current_savings: float, current amount that has been saved
    salary_saved: float, proportion of monthly salar that is saved
    rate_of_return: float, annual return on invested salary
    
    returns: float, updated savings
    """
    
    return current_savings+current_savings*rate_of_return/12 + salary_saved


def compute_time(cp):
    """
    cp: dict, contains portion_downpayment, initial_savings, rate_of_return, annual_salary
    total_cost, semi_annual_raise, portion_saved
    
    returns: dict, keys are months and final_savings, representing months required
    to make down payment on house, and the final savings reached after months number of
    months
    """
    
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
        
    return {'months': months, 'final_savings': current_savings}

def get_parameters(portion_saved):
    """
    portion_saved: proportion of monthly salary that is saved 
    
    returns: dict, with initial parameters for calculation of time to make down payment
    """
    return  {
        'portion_down_payment': .25,
        'initial_savings': 0,
        'rate_of_return': 0.04,
        'annual_salary': 300000, 
        'total_cost': 1000000,
        'semi_annual_raise': 0.07,
        'portion_saved': portion_saved
        }


def search():
    """
    Performs bisection search on savings rate, which is represented by a number
    between 0 and 100000, in order to find the savings rate that allows one to 
    make down payment on house given parameters. Prints out the results.
    
    returns: None
    """
    def savings_rate(current_saving):
        return current_saving/10000
    
    def get_next_savings_mag(low, high):
        return (low+high)/2
    
    low=0
    high=10000
    
    current_savings_magnitude = get_next_savings_mag(low, high)
    
    cp = get_parameters(savings_rate(current_savings_magnitude))
    
    result = compute_time(cp)
    
    steps = 0
    
    minimum_payment = minimum_house_payment(cp['portion_down_payment'], cp['total_cost'])
    
    while(result['months'] != 36 or abs(result['final_savings']-minimum_payment)>100):

        steps += 1

        if (result['months']>36):
            low=current_savings_magnitude
        else:
          high=current_savings_magnitude
          
        current_savings_magnitude = get_next_savings_mag(low, high)

        result = compute_time(get_parameters(savings_rate(current_savings_magnitude)))
        
    print("Completed in", steps, "steps.")
    print("Savings Rate: ", current_savings_magnitude/10000)
    print("Final Saving:", result['final_savings'])
    print("Months:", result['months'])
    
def house_hunting():
    search()

house_hunting()