def print_args(func):
    def print_vals():
        print('{} was called with {}'.format(func.__name__, [cell.cell_contents for cell in print_vals.__closure__]))

    return print_vals
