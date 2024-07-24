# Learning Python
Learn the basics of programming in Python

## Local website testing with Docker

    docker-compose up
    open http://0.0.0.0:4000/learn-python/


## Testing the solutions

The solutions are found in the private
[learn-python-solutions](https://github.com/berufsbildung-basel/learn-python-solutions)
repository, to hide them from the students.

If you create new exercices, please also add solutions there, the `test-all.sh` script
allows for running all the tests to validate them.

To test the solutions you can add that repository to your Python
path, assuming you checkout both repos under the same parent folder:

    export PYTHONPATH=../learn-python-solutions/solutions/
