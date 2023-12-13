# Character Copy Kata

![Character Copy Diagram](URL_of_the_diagram)

## Overview
This kata focuses on understanding NSubstitute by writing a character copier class that reads characters from a source and copies them to a destination, one character at a time.

## Task
Create a `Copier` class that interacts with `ISource` and `IDestination` interfaces. `ISource` has a method `ReadChar()` for reading a character, and `IDestination` has a method `WriteChar(char c)` for writing a character. The `Copier` class should have a method `Copy()` that reads from `ISource` and writes to `IDestination`, character by character, until a newline (`'\n'`) character is encountered.

### Interfaces

#### ISource
- **Method**: `char ReadChar()`
  - Reads and returns one character.

#### IDestination
- **Method**: `void WriteChar(char c)`
  - Writes the provided character.

### Copier Class

#### Description
- **Constructor**: Takes instances of `ISource` and `IDestination`.
- **Method**: `void Copy()`
  - Reads characters one at a time from `ISource`.
  - Writes characters to `IDestination`.
  - Stops processing when it encounters a newline character (`'\n'`).
  - The newline character is not written to `IDestination`.

### Note
- Only the `Copier` class should be a concrete class.
- `ISource` and `IDestination` should be implemented using NSubstitute for testing purposes.

