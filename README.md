# DSA Interview Prep

A collection of data structure and algorithm practice problems and reusable implementations.

## Problem solutions

Solutions in `problems/` are organized by their primary topic. A solution belongs to one topic
folder even when it uses ideas from several topics; different approaches to the same problem stay
together under that topic rather than being duplicated across categories.

For curated problem sets, the source and difficulty are kept below the topic:

```text
problems/
|-- Arrays/
|   |-- CSES/
|   `-- NeetCode150/
|       |-- Easy/
|       `-- Medium/
|-- BinarySearch/
|-- LinkedLists/
|-- Trees/
`-- ...
```

The topic folders currently include `Arrays`, `Backtracking`, `BinarySearch`, `BitManipulation`,
`DynamicProgramming`, `Graphs`, `Greedy`, `Hashing`, `LinkedLists`, `Math`, `Queues`, `Recursion`,
`Sorting`, `Stacks`, `Strings`, and `Trees`. CSES, NeetCode150, and USACO solutions are filed
under their topic instead of in separate top-level problem collections.

Most files are standalone practice solutions and can be run from the repository root with Python,
for example:

```sh
python problems/Arrays/concatenationofarray.py
```

## Reusable implementations

The `src/dsa_interviewprep/` directory contains reusable data structure and algorithm
implementations, separate from individual problem solutions.