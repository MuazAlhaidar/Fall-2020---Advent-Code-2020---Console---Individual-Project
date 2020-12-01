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
