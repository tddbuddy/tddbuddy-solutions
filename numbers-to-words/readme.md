# Numbers to Words

When it comes to writing, there's often a debate among writers about the appropriate use of numerals versus spelling out numbers. While opinions vary, there are some commonly accepted guidelines.

## Rules for Spelling Out Numbers

In this kata, we'll adhere to two specific rules:

1. **Numbers Starting a Sentence:** Numbers that begin a sentence should always be spelled out.
2. **Hyphenation:** Compound numbers ranging from twenty-one to ninety-nine should be hyphenated.

## Implementation for Sentence-Starting Numbers

The aim is to develop a method that converts numeric figures into spelled-out words, particularly for numbers that start a sentence. This function will act like a grammar spell checker, specifically for numerical expressions.

### Parameters

- The method should accept numbers as input.
- It should return the number in spelled-out form.
- Assumes all input numbers initiate sentences.
- The focus is on positive numbers up to four digits.

### Examples

| Digits | Example                   |
|--------|---------------------------|
| 1 digit | 0 = zero                  |
|         | 5 = five                  |
|         | 8 = eight                 |
| 2 digits | 10 = ten                 |
|         | 21 = twenty-one           |
|         | 77 = seventy-seven        |
| 3 digits | 100 = one hundred        |
|         | 303 = three hundred three |
|         | 555 = five hundred fifty-five |
| 4 digits | 2000 = two thousand      |
|         | 3466 = three thousand four hundred sixty-six |
|         | 2400 = two thousand four hundred |

### Hint

Start by solving for one-digit numbers, then progress to two digits, and so on.

## Bonus

For four-digit numbers, opt for simplicity in expression. For instance, instead of spelling out 5300 as "five thousand three hundred", it should be "fifty-three hundred". This simplicity rule applies exclusively to four-digit numbers.

