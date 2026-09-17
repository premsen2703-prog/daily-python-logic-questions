import random

# --- GLOBAL SCOPE ---
GAME_NAME = "Function Quest"
player_health = 100


def apply_damage(amount):
    """Demonstrates GLOBAL SCOPE modification."""
    global player_health
    player_health = max(0, player_health - amount)


# --- ARGS & KWARGS / RETURN VALUES ---
def calculate_damage(base_dmg, *multipliers, **bonuses):
    """Calculates final damage using variable arguments and returns it."""
    final_dmg = base_dmg

    # *args is a tuple of multipliers (e.g., critical hits, potion boosts)
    for mult in multipliers:
        final_dmg *= mult

    # **kwargs is a dictionary of flat additions (e.g., equipment bonuses)
    for bonus_name, bonus_val in bonuses.items():
        final_dmg += bonus_val

    return round(final_dmg)


# --- DEFAULT ARGUMENTS ---
def perform_attack(skill_name, base_dmg=15):
    """Executes a combat turn using default arguments."""
    print(f"\n--- You use {skill_name}! ---")

    # Critical hit chance: 20% chance to add a 1.5x multiplier
    crit_multiplier = 1.5 if random.random() < 0.20 else 1.0

    # Calculate final damage output
    damage_dealt = calculate_damage(
        base_dmg, crit_multiplier, weapon_bonus=5, ring_bonus=2
    )

    if crit_multiplier > 1.0:
        print("💥 CRITICAL HIT!")

    print(f"You dealt {damage_dealt} damage to the monster.")

    # Enemy strikes back!
    monster_dmg = random.randint(10, 25)
    apply_damage(monster_dmg)
    print(f"👹 Monster retaliates and deals {monster_dmg} damage to you.")
    print(f"❤️ Your Current Health: {player_health}/{100}")


# --- HIGHER-ORDER & LAMBDA FUNCTIONS ---
def status_effects_engine(effect_modifier, health):
    """A higher-order function that accepts a lambda function."""
    return effect_modifier(health)


# --- MAIN GAME LOOP ---
print(f"Welcome to {GAME_NAME}!")

# 1. Standard attack using the default damage (15)
perform_attack("Slash")

# 2. Heavy attack overriding the default damage (30)
perform_attack("Heavy Smash", base_dmg=30)

# 3. Using Lambdas and Higher-Order Functions for a Healing Potion
# The lambda describes *how* the healing behaves dynamically
heal_potion = lambda hp: min(100, hp + 25)
player_health = status_effects_engine(heal_potion, player_health)

print(f"\n🧪 You drank a Healing Potion! Health restored to: {player_health}")
