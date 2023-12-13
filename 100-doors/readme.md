# 100 Doors Kata

This kata explores an intriguing problem involving 100 doors in a row, all initially closed. The challenge involves multiple passes through these doors, toggling their state in a specific manner.

## Problem Description

Imagine a long corridor with 100 doors, all closed. You make 100 passes by these doors, altering their state each time you pass:

- **First Pass**: You visit every door and open it.
- **Second Pass**: You only visit every second door (door #2, #4, #6, ...) and close it.
- **Third Pass**: You visit every third door (door #3, #6, #9, ...) toggling its state. If it's closed, you open it; if it's open, you close it.
- **Subsequent Passes**: Continue this pattern until the 100th pass, where you only visit the 100th door.

Your task is to determine the state of each door after 100 passes.

## Requirements

- Represent each door's state with a symbol: `@` for an open door, `#` for a closed door.
- After completing the 100th pass, print the state of each door as a single string.

## Example

For a quick grasp, consider the first six doors after following the described process:
- The expected state would be `@@##@@##`.

This pattern emerges from the unique toggle sequence each door experiences. Your goal is to extend this logic to all 100 doors.

## Challenge

Determine the final state of each door and understand the underlying pattern. This exercise is excellent for honing logic and pattern recognition skills in programming.

