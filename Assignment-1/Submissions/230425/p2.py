from cmath import inf


def best_response_calculator(payoff_matrix, player, opponent_action):
    
    strategies_1 = set([s1  for s1, s2 in payoff_matrix.keys()])
    strategies_2 = set([s2  for s1, s2 in payoff_matrix.keys()])
    
    best_action = ''
    best_response_payoff = -inf
    
    if player == 1:
        for s1 in strategies_1:
            if payoff_matrix[(s1, opponent_action)][0] > best_response_payoff:
                best_response_payoff = payoff_matrix[(s1, opponent_action)][0]
                best_action = s1
    
    if player == 2:
        for s2 in strategies_2:
            if payoff_matrix[(opponent_action, s2)][1] > best_response_payoff:
                best_response_payoff = payoff_matrix[(opponent_action, s2)][1]
                best_action = s2
    
    return best_action
    
    
    
payoff_matrix = {
    ('Bach', 'Bach'): (2, 1),
    ('Bach', 'Stravinsky'): (0, 0),
    ('Stravinsky', 'Bach'): (0, 0),
    ('Stravinsky', 'Stravinsky'): (1, 2)
}

player = 1
opponent_action = 'Bach'

best_action = best_response_calculator(payoff_matrix, player, opponent_action)
print(f'best Action for player {player} for opponent action {opponent_action} is {best_action}')
     

    