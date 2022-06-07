
import click
from dask.distributed import Client
from functions.utils import slow_pow, slow_add
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

test_functions = {
        "slow_pow": [slow_pow, 2],
        "slow_add": [slow_add, 2],
    }


@click.group(help="For further information on each function please see functions/utils.py")
def main()->None:
    pass


@main.command(help=f"The available functions and number of parameters that can be run using the Dask framework are: {[(key, value[1]) for key, value in test_functions.items()]}")
@click.option("--function", prompt="Please select function to use with the dask framework",
                type=click.Choice(['slow_pow', 'slow_add'], case_sensitive=False))
@click.option("--parameters","--p", prompt="Please specify the parameters for the chosen function", multiple=True)
@click.option("--gather","--g", prompt="Would you like to gather (T/F)", type=bool)
def dask_submit(function: str, parameters: list, gather: bool)->None:
    if len(parameters) == test_functions[function][1]:
        result = client.submit(test_functions[function][0],parameters)
        while result.status == "pending":
            logger.info(result)
        logger.info("Process complete")
        if gather == True:
            logger.info(f"Gathered using Dask: {client.gather(result)}")
        return None
    else:
        logger.error("Incorrect number of parameters for chosen functions, please check helper for further information.")
        return None

@main.command(help=f"The available functions and number of parameters that can be run using the Dask framework are: {[(key, value[1]) for key, value in test_functions.items()]}")
@click.option("--function", prompt="Please select function to use with the dask framework",
                type=click.Choice(['slow_pow', 'slow_add'], case_sensitive=False))
@click.option("--parameters","--p", prompt="Please specify the iterations for the chosen function", multiple=True)
@click.option("--gather","--g", prompt="Would you like to gather (T/F)", type=bool)
def dask_submit_loop(function: str, parameters: int, gather: bool)->None:
    result = []
    iterations, = map(int, parameters)
    for i in range(1,iterations):
        future = client.submit(test_functions[function][0],(i,10))
        logger.info(future)
        result.append(future)
    logger.info(f"Process complete")
    if gather == True:
        logger.info(f"Gathered using Dask: {client.gather(result)}")
    return None

        
if __name__ == '__main__':
    # client = Client(n_workers=4, threads_per_worker=4) -- can be used with clusters but not worth on single PC
    client = Client(processes=False) # Generate one worker with 4 threads running in parallel
    main()
