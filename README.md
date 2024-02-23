# brainfuck+2
Like brainfuck, but with 2 more commands (that's a lie).

## Usage
Download the `.py` file, run it, and enter the code file's path. At the end of execution, you can view the memory.

The memory tape is dynamic; it will add cells to the right if the pointer hits the end of it.

## What's Brainfuck+2?

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*The title of this repository is not correct because of technical limitations. The correct title is actually* **brainfuck+2**.

**Brainfuck+2** is like brainfuck, with the addition of ~~2~~ 3 more commands. It was titled that beacuse Brainfuck+3 was taken on the wiki.

Updated brainfuck:

Command | Description
--- | ---
`+` `-` `<` `>` `[` `]` `,` `.` | Same as brainfuck
`;` | Takes a single number input
`:` | Outputs the current cell as a number. Using `:` on `66` would output `66`, not `B`.
`'` | Toggles overflow mode. If overflow mode is on (it is by default), then cells will behave like standard brainfuck, wrapping around at 0 and 255. If it is off, cells can have any positive integer.

Read the [wiki page](https://esolangs.org/wiki/Brainfuck%2B2) for more information about Brainfuck+2.
