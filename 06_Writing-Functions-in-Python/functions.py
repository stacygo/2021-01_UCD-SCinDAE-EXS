import inspect
import time
import numpy as np
import pandas as pd
import contextlib


def count_letter(content, letter):
    """Count the number of times `letter` appears in `content`.

    Args:
        content (str): The string to search.
        letter (str): The letter to search for.

    Returns:
        int

    Raises:
        ValueError: If `letter` is not a one-character string.
    """
    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` must be a single character string.')
    return len([char for char in content if char == letter])


def build_tooltip(function):
    """Create a tooltip for any function that shows the function's docstring.

    Args:
      function (callable): The function we want a tooltip for.

    Returns:
      str
    """
    # Use 'inspect' to get the docstring
    docstring = inspect.getdoc(function)
    border = '#' * 28
    return '{}\n{}\n{}'.format(border, docstring, border)


def standardize(column):
    """Standardize the values in a column.

    Args:
        column (pandas Series): The data to standardize.

    Returns:
        pandas Series: the values as z-scores
    """
    # Finish the function so that it returns the z-scores
    z_score = (column - column.mean()) / column.std()
    return z_score


def _process_pic(n_sec):
    print('Processing', end='', flush=True)
    for i in range(10):
        print('.', end='' if i < 9 else 'done!\n', flush=True)
        time.sleep(n_sec)


def process_with_numpy(p):
    _process_pic(0.1521)


def process_with_pytorch(p):
    _process_pic(0.0328)


def get_image_from_instagram():
    return np.random.rand(84, 84)


@contextlib.contextmanager
def timer():
    """Time how long code in the context block takes to run."""
    t0 = time.time()
    try:
        yield
    except:
        raise
    finally:
        t1 = time.time()
        print('Elapsed: {:.2f} seconds'.format(t1 - t0))


class MockStock:
    def __init__(self, loc, scale):
        self.loc = loc
        self.scale = scale
        self.recent = list(np.random.laplace(loc, scale, 2))

    def price(self):
        sign = np.sign(self.recent[1] - self.recent[0])
        # 70% chance of going same direction
        sign = 1 if sign == 0 else (sign if np.random.rand() > 0.3 else -1 * sign)
        new = self.recent[1] + sign * np.random.rand() / 10.0
        self.recent = [self.recent[1], new]
        return new


@contextlib.contextmanager
def stock(symbol):
    base = 140.00
    scale = 1.0
    mock = MockStock(base, scale)
    print('Opening stock ticker for {}'.format(symbol))
    yield mock
    print('Closing stock ticker')


def mean(data):
    print(data.mean())


def std(data):
    print(data.std())


def minimum(data):
    print(data.min())


def maximum(data):
    print(data.max())


def load_data():
    df = pd.DataFrame()
    df['height'] = [72.1, 69.8, 63.2, 64.7]
    df['weight'] = [198, 204, 164, 238]
    return df


def get_user_input(prompt='Type a command: '):
    command = np.random.choice(['mean', 'std', 'minimum', 'maximum'])
    print(prompt)
    print('> {}'.format(command))
    return command


def has_docstring(func):
    """Check to see if the function
    `func` has a docstring.

    Args:
        func (callable): A function.

    Returns:
        bool
    """
    return func.__doc__ is not None


def load_and_plot_data(filename):
    """Load a data frame and plot each column.

    Args:
      filename (str): Path to a CSV file of data.

    Returns:
      pandas.DataFrame
    """
    df = pd.load_csv(filename, index_col=0)
    df.hist()
    return df


def as_2D(arr):
    """Reshape an array to 2 dimensions"""
    return np.array(arr).reshape(1, -1)


def log_product(arr):
    return np.exp(np.sum(np.log(arr)))


def create_math_function(func_name):
    if func_name == 'add':
        def add(a, b):
            return a + b

        return add
    elif func_name == 'subtract':
        # Define the subtract() function
        def subtract(a, b):
            return a - b

        return subtract
    else:
        print("I don't know that one")


def print_args(func):
    sig = inspect.signature(func)
    def wrapper(*args, **kwargs):
        bound = sig.bind(*args, **kwargs).arguments
        str_args = ', '.join(['{}={}'.format(k, v) for k, v in bound.items()])
        print('{} was called with {}'.format(func.__name__, str_args))
        return func(*args, **kwargs)
    return wrapper


def check_inputs(a, *args, **kwargs):
    for value in a:
        time.sleep(0.01)
    print('Finished checking inputs')


def check_outputs(a, *args, **kwargs):
    for value in a:
        time.sleep(0.01)
    print('Finished checking outputs')


def run_n_times(n):
    """Define and return a decorator"""
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator
