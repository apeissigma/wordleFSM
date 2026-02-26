# Run the game

Run the game from the terminal: python wordle_fsm.py
To play:

1. Select option "1" to play a round
2. Enter 5-letter guesses
3. Confirm each guess
4. Review feedback after each guess
5. Try to find the word within 6 attempts

# Testing Performed

I conducted manual tests using the provided wordle_fsm_test.py file to test core functionality.

## Three key test cases

### Score Tracking

Verifies that the Score() method correctly increments the attempt counter when a guess is submitted. This ensures the 6-guess limit functions properly.
def test_score_increments_attempt_count():
game = Wordle(secret_word="apple")
game.Score()
assert game.attempt_count == 1

### Win Condition Detection

Confirms that IsWinner() correctly identifies when a player's guess exactly matches the secret word, triggering the win condition.
def test_is_winner_true_when_guess_matches_secret():
game = Wordle(secret_word="apple")
game.\_current_guess = "apple"
assert game.IsWinner() is True

### Letter Position Analysis

Validates the core scoring logic that determines if letters are either in the correct position, present but in the wrong position, or absent from the word entirely.
def test_score_guess_handles_positions():
game = Wordle(secret_word="apple")
assert game.\_score_guess("grape") == ["A", "A", "P", "P", "C"]
