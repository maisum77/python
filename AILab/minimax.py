import math

class CoinGame:
    def __init__(self, coins):
        self.coins = coins
        self.ai_score = 0
        self.human_score = 0
        self.sequence = []

    def minmax(self, start, end, isMaxTurn, alpha, beta):
        """
        Recursive function to determine the optimal value for the AI
        from the current state (start to end).
        """
        # Base Case: No coins left
        if start > end:
            return 0

        if isMaxTurn:
            # AI's Turn (Maximizer)
            # Option 1: AI takes Left
            val1 = self.coins[start] + self.minmax(start + 1, end, False, alpha, beta)
            # Option 2: AI takes Right
            val2 = self.coins[end] + self.minmax(start, end - 1, False, alpha, beta)
            
            # Choose the maximum value
            res = max(val1, val2)
            
            # Alpha-Beta Pruning
            alpha = max(alpha, res)
            if beta <= alpha:
                return res # Beta cutoff
            return res
        
        else:
            # Human's Turn (Minimizer)
            # Human wants to minimize the AI's total score.
            # If Human takes Left, AI gets points from the remaining sub-array
            val1 = self.minmax(start + 1, end, True, alpha, beta)
            # If Human takes Right
            val2 = self.minmax(start, end - 1, True, alpha, beta)
            
            # Choose the minimum value (Best for Human, Worst for AI)
            res = min(val1, val2)
            
            # Alpha-Beta Pruning
            beta = min(beta, res)
            if beta <= alpha:
                return res # Alpha cutoff
            return res

    def get_best_move(self, start, end, isMaxTurn):
        """
        Helper to evaluate immediate moves using minmax logic.
        """
        # Initialize huge values
        alpha = -math.inf
        beta = math.inf

        if isMaxTurn:
            # Calculate value if AI picks Left
            val_left = self.coins[start] + self.minmax(start + 1, end, False, alpha, beta)
            # Calculate value if AI picks Right
            val_right = self.coins[end] + self.minmax(start, end - 1, False, alpha, beta)
            
            if val_left >= val_right:
                return 'left'
            else:
                return 'right'
        else:
            # Calculate AI's future score if Human picks Left
            val_left = self.minmax(start + 1, end, True, alpha, beta)
            # Calculate AI's future score if Human picks Right
            val_right = self.minmax(start, end - 1, True, alpha, beta)
            
            # Human picks the path that gives AI the LOWEST score
            if val_left <= val_right:
                return 'left'
            else:
                return 'right'

    def play(self):
        start = 0
        end = len(self.coins) - 1
        turn_counter = 1
        is_ai_turn = True # AI starts first

        print(f"Starting Game with Coins: {self.coins}")
        print("-" * 50)

        while start <= end:
            current_coins = self.coins[start : end + 1]
            print(f"Step {turn_counter}:")
            print(f"Current State: {current_coins}")

            # Determine optimal move
            choice = self.get_best_move(start, end, is_ai_turn)

            picked_value = 0
            player_name = ""

            if choice == 'left':
                picked_value = self.coins[start]
                start += 1
            else:
                picked_value = self.coins[end]
                end -= 1

            if is_ai_turn:
                player_name = "AI (Maximizer)"
                self.ai_score += picked_value
            else:
                player_name = "Human (Minimizer)"
                self.human_score += picked_value

            print(f"{player_name} chooses {choice.upper()} coin: {picked_value}")
            self.sequence.append((player_name, picked_value))
            
            # Switch turn
            is_ai_turn = not is_ai_turn
            turn_counter += 1
            print("-" * 30)

        self.display_results()

    def display_results(self):
        print("\n" + "="*50)
        print("GAME OVER")
        print("="*50)
        print(f"Total AI Score:    {self.ai_score}")
        print(f"Total Human Score: {self.human_score}")
        print("-" * 50)
        print("Move Sequence:")
        for i, (player, val) in enumerate(self.sequence, 1):
            print(f"{i}. {player} took {val}")
        print("="*50)

# --- RUNNING THE TASK ---
initial_coins = [4, 7, 2, 9, 5, 2]
game = CoinGame(initial_coins)
game.play()