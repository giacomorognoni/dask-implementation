# Dask Distributed Framework Testing

## Overview

This brief project gives and overview of the Dusk framework capabilities for multiprocessing and scheduling.

## Requirements

The project dependencies requirements are defined in the pyproject.toml file. No other software requires to be installed.

The current project is based on using a single machine, therefore, only one worker is configured currently with four threads. If the project is used with multiple core machines then the configuration currently commented out in the cli.py can be commented back in and the load can be better spread.

## Usage

Once dependencies and installed in a relevant virtual environment, the project can be run by cd into the project directory and using the cli. 

```
python cli.py <function name (dask-submit/dask-submit-loop)> --p <parameter (further information can be found on the helper function)> --gather <T/F whether the results want to be gathered, check the helper function>