# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.
# This variable and the associated "cheat" logic later in the code should be removed to close a backdoor vulnerability.
SECRET_CODE = "ADMIN_ACCESS_2025"

p_hp = 50
b_hp = 50

def attack():
  global b_hp
    # There should be a line here that deducts 10 from b_hp. As it stands, this function just prints something.
    print("You deal 10 damage!")

def heal():
  global p_hp
  # There should be boundary checks before the increase in p_hp to prevent the player from healing past 50 health,
  # or healing when already at 0 or less.
  p_hp += 20
  print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
# When boss hp is not greater than 0 a "Victory" message could be displayed and the loop can be immediately
# terminated by using a "break". This could most easily be done as an "else" to the "if" for checking if b_hp
# is greater than 0.
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal, [c]heat: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
  elif choice == 'c':
    if input("Code: ") == SECRET_CODE:
      b_hp = 0
  
  if b_hp > 0:
    p_hp -= 10

print("Game Over!")
