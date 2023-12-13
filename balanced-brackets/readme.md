# Balanced Brackets Kata

The Balanced Brackets kata is a classic problem in computer science, focusing on using data structures to ensure correct syntax in string expressions. The challenge involves verifying whether a string of brackets is "balanced."

## Problem Description

Given an input string consisting of `X` opening brackets `[` and `Y` closing brackets `]`, arranged in any order, determine whether the string is balanced. A balanced string is one where:

- Every opening bracket `[` is matched and followed by a corresponding closing bracket `]`.
- Brackets must close in the correct order, without any unmatched pairs.

This kata is designed to simulate real-world coding scenarios, requiring you to make decisions as if you were writing production-level code.

## Requirements

- The input will only contain brackets or be an empty string.
- You must verify if the brackets in the string are balanced.

## Examples

- (empty) `""` - OK
- `[]` - OK
- `[][]` - OK
- `[[]]` - OK
- `[[[][]]]` - OK
- `][` - FAIL
- `][][` - FAIL
- `[][]][` - FAIL

## Hint

Start by returning `string.empty` as the default condition. This approach aligns with the red-green-refactor cycle commonly used in Test-Driven Development (TDD). Begin by writing tests that expect failure ('red'), implement the simplest code to pass the test ('green'), and then refactor your solution for efficiency and readability.

## Challenge

The key to solving this kata lies in understanding how to use data structures effectively, such as stacks, to track opening and closing brackets. It's a great exercise to enhance your problem-solving skills and understanding of fundamental programming concepts.

