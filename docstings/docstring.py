import numpy as np
# A docstring is a string written as the first line of a function. Because the usually span multiple lines,
# they are enclosed in tripple quotes.
"""Every docstring has some (although usually not all) of these five key pieces of information: what the function does, what the arguments are, 
what the return value or values should be, info about any errors raised, and anything else you'd like to say about the function. 
"""

def split_and_stack(df, new_names):
    """Split a dataFrame's column into two halves and then stack them verticaly,
    returning a new DataFrame with 'new_names' as the column names

    Args:
        df (Dataframe): The Dataframe to split.
        new_names(iterable of str): The column names for the new DataFrame


    Returns:
        DataFrame
    """
    half = len(df.columns)/2
    left = df.iloc[:, :half]
    right = df.iloc[:, half:]

    new_df = np.vstack([left.values, right.values], cols = new_names)
    return new_df

def count_letter(content, letter):
  """Count the number of times `letter` appears in `content`.

  Args:
    content (str): The string to search.
    letter (str): The letter to search for.

  Returns:
    int

  # Add a section detailing what errors might be raised
  Raises:
    ValueError: If `letter` is not a one-character string.
  """
  if (not isinstance(letter, str)) or len(letter) != 1:
    raise ValueError('`letter` must be a single character string.')
  return len([char for char in content if char == letter])