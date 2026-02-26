# boss_mini.py
# A tiny combat script for the GitHub Workflow Exam.

p_hp = 50
b_hp = 50

def attack():
  global b_hp
  b_hp -= 10
  print("You deal 10 damage!")

def heal():
  global p_hp
  if p_hp > 0 and p_hp + 20 <= 50:
    p_hp += 20
  elif p_hp + 20 > 50:
    p_hp = 50
  else:
    return
  print(f"Healed! HP is now {p_hp}")

# --- Simple Game Loop ---
while p_hp > 0 and b_hp > 0:
  print(f"\nPlayer: {p_hp} | Boss: {b_hp}")
  choice = input("Action [a]ttack, [h]eal: ").lower()

  if choice == 'a':
    attack()
  elif choice == 'h':
    heal()
  else: # Input protection, if the player enters something invalid, it restarts the loop.
    continue
  
  if b_hp > 0:
    p_hp -= 10
    if p_hp <= 0:
      print("Defeat!")
  else:
    print("Victory!")
    break

print("Game Over!")
