# Parser Generator
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)



Parser Generator is the second phase of my compiler (Genepiler). It's planned to join my _'Oh My Compiler'_ project!


This phase takes the _tokens_ from the [first phase](https://github.com/Hagar-Usama/Lexical) along with the _CFG rules_ and consequently produces _actions file_ to be processed later in the third phase - [Intermediate Code Generator](https://github.com/Hagar-Usama/Intermediate-Code-Generator) 


---

## Tasks
* [ ] interface for LR:
  * [x] convert CFG file into lines. Each is a statement
  * [x] put the statement into a dict [key, value]
  * [ ] build another dict to replace terminals and non-terminals by one char(no need)
* [ ] left Recursion
* [ ] left Factoring
* [X] get first
* [X] get follow
* [x] build parsing table
* [x] walk through the parsing table
* [x] build a parsing tree (see phase 3)
* [x] add arguments (argparse)
* [x] consider module file to add your modules in
* [x] consider adding directory for input and directory for output
* [x] report

---

## [Memory] Plan (schedule)
* Today: 1 May 2020
* Deadline: 5 May 2020

> 3 days to just implement this<br>
> 1 day for the report
