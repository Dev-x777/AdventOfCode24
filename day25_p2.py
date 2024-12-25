def parse_input():
    # Read input from the file
    with open("day_25.in", "r") as file:
        data = file.read()

    locks, keys = [], []

    # Split the input into schematics for locks and keys
    for schematic in data.split("\n\n"):
        cur = {i for i, c in enumerate(schematic) if c == "#"}
        if schematic.startswith("#####"):
            locks.append(cur)  # Add to locks if it starts with "#####"
        else:
            keys.append(cur)  # Otherwise, add to keys

    return locks, keys


LOCKS, KEYS = parse_input()


def part_one():
    # Count the locks that have no overlap with any key
    return sum(not lock & key for lock in LOCKS for key in KEYS)


def part_two():
    # Include only the last 50 locks and keys for the final chronicle
    recent_locks = LOCKS[-50:]
    recent_keys = KEYS[-50:]

    # Calculate the compatibility of recent locks and keys
    completed_chronicle = sum(not lock & key for lock in recent_locks for key in recent_keys)

    return completed_chronicle


# Print the results
print(f"Part 1: {part_one()}")
print(f"Part 2: {part_two()}")
