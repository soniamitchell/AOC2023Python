# AOC2022Python



## Miniconda

Create, activate, and deactivate the virtual environment:

```
conda create --name aoc2023_env
source activate aoc2023_env
source deactivate
```

Install packages in the virtual environment:

```
conda install numpy
```

## Poetry

Activate virtual environment:

```
poetry shell

# Dectivate environment but stay within shell:
poetry deactivate

# Exit shell and environment
exit
```

Add dependencies:

```
poetry add numpy
```

Install dependencies:

```
poetry install

# Update dependencies
poetry update
```

Run script in virtual environment:

```
poetry run python script.py
```

