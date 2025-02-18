import numpy as np

def simulation_binomial_test(observed_successes, n, p):
    # observed_successes - фактическое кол-во успешных данных из нашей выборки
    # n - размер выборки для моделирования
    # p - вероятность успеха
    #initialize null_outcomes
    null_outcomes = []
    p = [p, 1-p]
    #generate the simulated null distribution
    for i in range(10000):
        simulated_monthly_visitors = np.random.choice(['y', 'n'], size=n, p=[.1, .9])
        num_purchased = np.sum(simulated_monthly_visitors == 'y')
        null_outcomes.append(num_purchased)   
    #calculate a 1-sided p-value
    null_outcomes = np.array(null_outcomes)
    p_value = np.sum(null_outcomes <= observed_successes)/len(null_outcomes) 

    #return the p-value
    return p_value