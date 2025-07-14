from re import L
import yfinance as yf
import numpy as np
# from queue import Queue

stock_ticker = 'AAPL'
start_date = '2022-01-01'
end_date = '2023-01-01'
risk_free_rate = 0.05 

strike_price = 100

class BinomialTreeModel():
    def __init__(self, stock_tickers, start_date, end_date, risk_free_rate, strike_price):
        self.data = yf.download(stock_tickers, start=start_date, end=end_date)
        self.close_data = self.data['Close'].dropna()
        self.stock_ticker = stock_tickers
        self.N = 100  
        self.risk_free_rate = risk_free_rate
        self.T = 1.0  
        self.dt = self.T / self.N
        self.strike_price = strike_price
        self.tree = []
        self._build_parameters()
        
    def _build_parameters(self):
        
        self.compute_volatility()
        self.compute_up_down_factors()
        self.compute_risk_neutral_prob()
        
    def compute_volatility(self):
        log_returns = np.log(self.close_data / self.close_data.shift(1)).dropna()
        log_returns = log_returns[self.stock_ticker]
        self.sigma = np.std(log_returns) * np.sqrt(252) 
        
    def compute_up_down_factors(self):
        self.u = np.exp(self.sigma * np.sqrt(self.dt))
        self.d = 1 / self.u
        
    def compute_risk_neutral_prob(self):
        self.p = (np.exp(self.risk_free_rate * self.dt) - self.d) / (self.u - self.d)
        
    def summary(self):
        print(f"Volatility (annual): {self.sigma}")
        print(f"Time step (dt): {self.dt}")
        print(f"Up factor (u): {self.u}")
        print(f"Down factor (d): {self.d}")
        print(f"Risk-neutral probability (p): {self.p}")
        

    def construct_tree(self)
        starting_price = float(self.close_data.iloc[0])

        for i in range(self.N + 1):
            level_prices = []
            for j in range(i + 1): 
                price = starting_price * (self.u ** j) * (self.d ** (i - j))
                level_prices.append(price)
                
            self.tree.append(level_prices)            
        

        
    def construct_payoff_matrix(self):
        if self.tree == []: 
            self.construct_tree()
        
        terminal_prices = np.array(self.tree[-1])
        payoffs = np.maximum(terminal_prices - self.strike_price, 0)
        return payoffs

    def price_option_game_theoretic(self):
        self.construct_tree()
        payoff_tree = self.construct_payoff_matrix()
        
       
        
        # Initialize value_tree with terminal payoffs
        value_tree = [None] * len(self.tree)
        value_tree[-1] = payoff_tree

        # Backward induction using game-theoretic decision
        for i in range(self.N - 1, -1, -1):  # from second last to root
            level_values = []
            for j in range(i + 1):
                S_ij = self.tree[i][j]
                # Future node values (expected)
                V_up = value_tree[i + 1][j + 1]
                V_down = value_tree[i + 1][j]
                expected_hold = np.exp(-self.risk_free_rate * self.dt) * (
                    self.p * V_up + (1 - self.p) * V_down
                )

                # Immediate exercise value
                immediate_exec = max(S_ij - self.strike_price, 0)

                # Game-theoretic value: best strategy of Player 1
                node_value = max(expected_hold, immediate_exec)
                level_values.append(node_value)

            value_tree[i] = level_values

        return value_tree[0][0] 

model = BinomialTreeModel(stock_ticker, start_date, end_date, risk_free_rate, strike_price)
value = model.price_option_game_theoretic()
print(f"Option Price (Game-Theoretic): {value:.2f}")
