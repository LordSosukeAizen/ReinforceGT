def is_pure_nash(strategy_profile, payoff_matrix):
    strategies = ['C', 'D']
    s1, s2 = strategy_profile
    print(strategy_profile)
    p1_payoff, p2_payoff = payoff_matrix[(s1, s2)]
    
  
    for alt_s1 in strategies:
        if alt_s1 != s1:
            alt_p1_payoff = payoff_matrix[(alt_s1, s2)][0]
            if alt_p1_payoff > p1_payoff:
                return False

    
    for alt_s2 in strategies:
        if alt_s2 != s2:
            alt_p2_payoff = payoff_matrix[(s1, alt_s2)][1]
            if alt_p2_payoff > p2_payoff:
                return False

    return True


def find_all_pure_nash_equilibria():

    payoff_matrix = {
        ('C', 'C'): (3, 3),
        ('C', 'D'): (0, 5),
        ('D', 'C'): (5, 0),
        ('D', 'D'): (1, 1)
    }

    strategies = ['C', 'D']
    equilibria = []

    for s1 in strategies:
        for s2 in strategies:
            profile = (s1, s2)
            if is_pure_nash(profile, payoff_matrix):
                equilibria.append(profile)

    return equilibria



equilibria = find_all_pure_nash_equilibria()
print("Pure Nash Equilibria:", equilibria)
