# python-exercices
Learn the basics of programming in Python

## Local website testing with Docker

    docker-compose up
    open http://0.0.0.0:4000/learn-python/


## Testing the solutions

The solutions are found in the private
[learn-python-solutions](https://github.com/berufsbildung-basel/learn-python-solutions)
repository.

That repository is mounted here as a submodule, so you can
develop and test the solutions here by setting

    export PYTHONPATH=./submodules/learn-python-solutions/solutions/

and using [git submodule](https://git-scm.com/book/en/v2/Git-Tools-Submodules)
commands to keep them in sync.