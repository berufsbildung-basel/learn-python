# python-exercices
Learn the basics of programming in Python

## TODO

- Hide the source repository from students so that the solutions are not visible to them

## Local website testing with Docker

    docker-compose up
    open http://0.0.0.0:4000/pages/bdelacre/python-exercices/


## Testing the solutions

For now the solutions are in their own [./solutions](solutions) folder.

They are excluded from the generated wegbsite by a [config.yml](./_config.yml) statement.

To use them to validate the tests, set `PYTHONPATH=./solutions/` and
you can then run commands like

    python basics/hello_python_test.py