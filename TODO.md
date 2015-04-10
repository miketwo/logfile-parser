# ToDos

A list of things to make this more production-worthy, if need be.

- Put everything into standard directory structure, following best practices here: http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application
   - split parser between CLI executable and reusuable library, move to /bin and /logfile-parser subdirectories
   - move tests to subdirectory
   - Pipify (add setup.py)
   - add `__init__.py`'s
- Hook tests into build system
- Maybe hook into alerting system or HipChat notifications
