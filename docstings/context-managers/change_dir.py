import os
import contextlib
@contextlib.contextmanager
def in_dir(path):
    """ a context manager that changes the current working directory to 
    a specific path and then changes it back after the context block is done

    Args:
        path(filepath): the filepath to work with

    Returns:
        -
    """
    # Save a current working directory
    old_dir = os.getcwd()

    # Switch to new working directory
    os.chdir(path)
    yield
    # Swicth to the prevoius working directory
    os.chdir(old_dir)


with in_dir('/mytext'):
    project_files = os.listdir()

    

# Add a decorator that will make timer() a context manager
@contextlib.contextmanager
def timer():
  """Time the execution of a context block.

  Yields:
    None
  """
  start = time.time()
  # Send control back to the context block
  yield
  end = time.time()
  print('Elapsed: {:.2f}s'.format(end - start))

with timer():
  print('This should take approximately 0.25 seconds')
  time.sleep(0.25)