# bsl-random-countdown.py to test yourself on speed.

import time
import random
from tkinter import Tk, Label, Button

MAX_WORD_LENGTH = 50  # Adjust if needed based on your longest line

def show_word(word, remaining_words):
  # Create a new pop-up window
  popup = Tk()
  popup.title(f"British Sign Language Practice ({remaining_words} words remaining)")

  # Calculate window width based on longest word and font size
  window_width = (MAX_WORD_LENGTH + 5) * 10  # Adjust font size multiplier as needed

  # Set fixed window size with padding
  popup.geometry(f"{window_width}x150+100+100")

  # Display the word with a large font
  label = Label(popup, text=word, font=("Arial", 30))
  label.pack(pady=50)

  # Schedule clearing the window after 5 seconds
  popup.after(5000, popup.destroy)

  # Keep the window open until closed (automatically after 5 seconds)
  popup.mainloop()

def get_next_word(words):
  if not words:
    return None  # No more words, indicate completion

  # Randomly choose an index from the remaining words
  word_index = random.randint(0, len(words)-1)
  word = words[word_index]

  # Return the chosen word and remove it from the list
  words.pop(word_index)
  return word

def main():
  # Read words from the text file without modifying it
  try:
    with open("bsl.txt", "r") as f:
      lines = f.readlines()
      words = [line.strip() for line in lines]
      num_words = len(words)
      print(f"Total words: {num_words}")
  except FileNotFoundError:
    print("File bsl.txt not found. Please create it.")
    return

  remaining_words = num_words

  while True:  # Loop until completion (no more words)
    next_word = get_next_word(words)
    if not next_word:  # Check for no more words
      break
    show_word(next_word, remaining_words)
    remaining_words -= 1

  print("All words have been practiced!")

if __name__ == "__main__":
  main()
