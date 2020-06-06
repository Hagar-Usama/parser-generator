# parser-generator

---

## Plan (schedule)
* Today: 5 May
* Deadline: 5 May

> 3 days to just implement this<br>
> 1 day for the report

### Tasks
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
* [x] consider add directory for input and directory for output
* [x] report
