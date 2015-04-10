# LogFile Parser
Given a text file with lines that say either 'starting **something**' or
'finishing **something**', emit all **something**'s that were started but not finished.

For instance:

```text
starting task A
starting task B
finishing task B
starting task C
starting task D
finishing task A
```

...would emit:

```text
task C
task D
```

# Installation and Usage
```
git clone https://github.com/miketwo/logfile-parser.git
cd logfile-parser
./parser.py example.txt
```

# Unit tests
```
python test_parser.py
```

# Assumptions and expected behaviour


#### Duplicate starting lines are ignored.
```text
starting task A
starting task A
finishing task A
```
Task A does NOT show up in results. No errors thrown.


#### Duplicate finishing lines are ignored.
```text
starting task A
finishing task A
finishing task A
```
Task A does NOT show up in results. No errors thrown.


#### Order is not checked.
The input file is considered "clean".
```text
finishing task A
starting task A
```
Task A does NOT show up in results. No errors thrown.


#### Task names can be any combination of characters.
The following is totally cool:
```text
starting @&#$&)(*!@*AA123)
```


#### Finishing without starting is ok.
```text
finishing task A
```
Task A does NOT show up in results. No errors thrown.


#### Maliciously-named tasks?  No worry, no cry.
```text
starting task starting task
starting task finishing task
finishing task starting task
```
"task finishing task" shows up in results.


#### The input file is relatively small.

#### The order of tasks in the output doesn't matter.
