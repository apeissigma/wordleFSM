from __future__ import annotations

from enum import Enum, auto
import random


class GameState(Enum):
    WORD_ENTRY = auto()
    CONFIRM = auto()
    SCORE = auto()
    IS_WINNER = auto()
    REVIEW = auto()
    CONFIRM_AFTER_REVIEW = auto()
    DISPLAY = auto()


class Wordle:
    def __init__(self, secret_word: str | None = None) -> None:
        if secret_word is None:
            secret_word = random.choice(["apple", "grape", "slate", "crane", "flint"])
        self.secret_word = secret_word.lower()
        self.attempt_count = 0
        self.has_won = False
        self.attempts: list[str] = []
        self._current_guess = ""

    def Score(self) -> None:
        self.attempt_count += 1

    def IsWinner(self) -> bool:
        self.has_won = self._current_guess == self.secret_word
        return self.has_won

    def _build_feedback(self, guess: str) -> tuple[list[str], list[str]]:
        correct_positions = []
        present_wrong_position = []

        for index, letter in enumerate(guess):
            if letter == self.secret_word[index]:
                correct_positions.append(letter)
            elif letter in self.secret_word:
                present_wrong_position.append(letter)

        return correct_positions, present_wrong_position

    def Display(self) -> None:
        print("\n=== Round Summary ===")
        for number, attempt in enumerate(self.attempts, start=1):
            print(f"Attempt {number}: {attempt}")

        print(f"Total attempts used: {self.attempt_count}/6")
        if self.has_won:
            print("You Won.")
        else:
            print(f"You Lost. The secret word was: {self.secret_word}")

        input("Press Enter to continue...")

    def PlayRound(self) -> None:
        state = GameState.WORD_ENTRY

        while True:
            if state == GameState.WORD_ENTRY:
                guess = input("Enter exactly five letters: ").strip().lower()
                if len(guess) != 5 or not guess.isalpha():
                    print("Invalid input. Please enter exactly five letters.")
                    state = GameState.WORD_ENTRY
                else:
                    self._current_guess = guess
                    state = GameState.CONFIRM

            elif state == GameState.CONFIRM:
                confirm = input(f"Confirm '{self._current_guess}'? (yes/no): ").strip().lower()
                if confirm in {"no", "n"}:
                    state = GameState.WORD_ENTRY
                elif confirm in {"yes", "y"}:
                    state = GameState.SCORE
                else:
                    print("Please respond with 'yes' or 'no'.")
                    state = GameState.CONFIRM

            elif state == GameState.SCORE:
                self.Score()
                self.attempts.append(self._current_guess)
                state = GameState.IS_WINNER

            elif state == GameState.IS_WINNER:
                winner = self.IsWinner()
                if winner:
                    state = GameState.DISPLAY
                elif self.attempt_count >= 6:
                    state = GameState.DISPLAY
                else:
                    state = GameState.REVIEW

            elif state == GameState.REVIEW:
                correct_positions, present_wrong_position = self._build_feedback(self._current_guess)
                print("\nReview:")
                print(f"Correct letter & position: {correct_positions if correct_positions else 'None'}")
                print(
                    "Letters present but wrong position: "
                    f"{present_wrong_position if present_wrong_position else 'None'}"
                )
                state = GameState.CONFIRM_AFTER_REVIEW

            elif state == GameState.CONFIRM_AFTER_REVIEW:
                state = GameState.WORD_ENTRY

            elif state == GameState.DISPLAY:
                self.Display()
                return


def main() -> None:
    while True:
        print("\n=== Wordle FSM Menu ===")
        print("1. Play a round")
        print("2. Leave")
        choice = input("Select an option: ").strip()

        if choice == "1":
            game = Wordle()
            game.PlayRound()
        elif choice == "2":
            print("Thanks for Playing and come back another time!")
            break
        else:
            print("Invalid option. Please choose 1 or 2.")


if __name__ == "__main__":
    main()
