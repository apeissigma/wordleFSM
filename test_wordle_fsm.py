from wordle_fsm import Wordle


def test_score_increments_attempt_count():
    game = Wordle(secret_word="apple")
    game.Score()
    assert game.attempt_count == 1


def test_is_winner_true_when_guess_matches_secret():
    game = Wordle(secret_word="apple")
    game._current_guess = "apple"
    assert game.IsWinner() is True


def test_is_winner_false_when_guess_does_not_match_secret():
    game = Wordle(secret_word="apple")
    game._current_guess = "grape"
    assert game.IsWinner() is False


def test_score_guess_handles_positions():
    game = Wordle(secret_word="apple")
    assert game._score_guess("grape") == ["A", "A", "P", "P", "C"]


def test_format_guess_row_uses_non_letter_for_absent():
    game = Wordle(secret_word="apple")
    assert game._format_guess_row("grape") == "[-] [-] [a] [p] [E]"
