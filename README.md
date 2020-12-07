# Fall 2020 - Advent Code 2020 - Console - Individual Project

This is my attempt at learning python by doing advent code questions.

## Advent Code

[Advent of Code](https://adventofcode.com/)

"_Advent of Code_ is an Advent calendar of small programming puzzles for a variety of skill sets and skill levels that can be solved in [any](https://github.com/search?q=advent+of+code) programming language you like. People use them as a [speed contest](https://adventofcode.com/leaderboard), [interview](https://y3l2n.com/2018/05/09/interview-prep-advent-of-code/) [prep](https://twitter.com/dznqbit/status/1037607793144938497), [company training](https://twitter.com/pgoultiaev/status/950805811583963137), [university](https://gitlab.com/imhoffman/fa19b4-mat3006/wikis/home) [coursework](https://www.gribblelab.org/scicomp2019/), [practice](https://twitter.com/mrdanielklein/status/936267621468483584) [problems](https://comp215.blogs.rice.edu/), or to [challenge each other](https://www.reddit.com/r/adventofcode/search?q=flair%3Aupping&restrict_sr=on)." -- [**Advent of Code About Page (2020)**](https://adventofcode.com/2020/about)

## Challenges Muaz Solved

### Day 1: Report Repair

After saving Christmas [five years in a row](https://adventofcode.com/events), you've decided to take a vacation at a nice resort on a tropical island. Surely, Christmas will go on without you.

The tropical island has its own currency and is entirely cash-only. The gold coins used there have a little picture of a starfish; the locals just call them _stars_. None of the currency exchanges seem to have heard of them, but somehow, you'll need to find fifty of these coins by the time you arrive so you can pay the deposit on your room.

To save your vacation, you need to get all _fifty stars_ by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants _one star_. Good luck!

Before you leave, the Elves in accounting just need you to fix your _expense report_ (your puzzle input); apparently, something isn't quite adding up.

Specifically, they need you to _find the two entries that sum to `2020`_ and then multiply those two numbers together.

For example, suppose your expense report contained the following:

```python
1721
979
366
299
675
1456
```

In this list, the two entries that sum to `2020` are `1721` and `299`. Multiplying them together produces `1721 * 299 = 514579`, so the correct answer is `<em>514579</em>`.

Of course, your expense report is much larger. _Find the two entries that sum to `2020`; what do you get if you multiply them together?_

#### Part 2

The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find _three_ numbers in your expense report that meet the same criteria.

Using the above example again, the three entries that sum to `2020` are `979`, `366`, and `675`. Multiplying them together produces the answer, `241861950`.

In your expense report, _what is the product of the three entries that sum to `2020`?_

### Day 2: Password Philosophy

Your flight departs in a few days from the coastal airport; the easiest way down to the coast from here is via [toboggan](https://en.wikipedia.org/wiki/Toboggan).

The shopkeeper at the North Pole Toboggan Rental Shop is having a bad day. "Something's wrong with our computers; we can't log in!" You ask if you can take a look.

Their password database seems to be a little corrupted: some of the passwords wouldn't have been allowed by the Official Toboggan Corporate Policy that was in effect when they were chosen.

To try to debug the problem, they have created a list (your puzzle input) of _passwords_ (according to the corrupted database) and _the corporate policy when that password was set_.

For example, suppose you have the following list:

```python
1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc
```

Each line gives the password policy and then the password. The password policy indicates the lowest and highest number of times a given letter must appear for the password to be valid. For example, `1-3 a` means that the password must contain `a` at least `1` time and at most `3` times.

In the above example, `<em>2</em>` passwords are valid. The middle password, `cdefg`, is not; it contains no instances of `b`, but needs at least `1`. The first and third passwords are valid: they contain one `a` or nine `c`, both within the limits of their respective policies.

_How many passwords are valid_ according to their policies?

#### Part 2

While it appears you validated the passwords correctly, they don't seem to be what the Official Toboggan Corporate Authentication System is expecting.

The shopkeeper suddenly realizes that he just accidentally explained the password policy rules from his old job at the sled rental place down the street! The Official Toboggan Corporate Policy actually works a little differently.

Each policy actually describes two _positions in the password_, where `1` means the first character, `2` means the second character, and so on. (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) _Exactly one of these positions_ must contain the given letter. Other occurrences of the letter are irrelevant for the purposes of policy enforcement.

Given the same example list from above:

- `1-3 a: abcde` is _valid_: position `1` contains `a` and position `3` does not.
- `1-3 b: cdefg`is _invalid_: neither position`1`nor position`3`contains`b`.
- `2-9 c: ccccccccc` is _invalid_: both position `2` and position `9` contain `c`.

_How many passwords are valid_ according to the new interpretation of the policies?
