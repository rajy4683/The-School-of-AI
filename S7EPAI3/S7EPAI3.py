def docstringLengthChecker(input_fn, max_doc_len=50):
    """
        Function closure to check if input function 
        has a docstring of atleast 50 characters
    """
    maxlen = max_doc_len
    def inner(*args, **kwargs):
        nonlocal maxlen
        if not isinstance(input_fn.__doc__, str):
            print(f'{input_fn.__name__} has no docstring')
        else:
            docstr_len = len(input_fn.__doc__)
            if (docstr_len < maxlen):
                print(f'{input_fn.__name__} has docstring length {docstr_len} less than {maxlen}')
            else:
                print(f'{input_fn.__name__} has valid docstring length {docstr_len}')
        return input_fn(*args, **kwargs)
    return inner


def generateFibo(start_val=1):
    """
    Returns next fibonacci sequence given a start_val.
    If start_val is not a Fibonacci number then defaults to 1
    """
    sqrt_checker = lambda x : x == int(math.sqrt(x))*int(math.sqrt(x))
    current_fib = start_val if (sqrt_checker(5*start_val*start_val - 4) or sqrt_checker(5*start_val*start_val + 4)) else 1
    def inner_calc():
        nonlocal current_fib
        print(f"Current fib:{current_fib}")
        current_fib = round(current_fib*(1 + math.sqrt(5))/2.0)
        return current_fib
    print(f"New fib:{current_fib}")
    return inner_calc


global_counter={}
def accounterOperations():
    """
    Closure that keeps track of how many times each function was called
    and also updates a global dictionary with the number of function calls
    """
    adder_call_count = 0
    multiplier_call_count = 0
    divider_call_count = 0
    def adder():
        nonlocal adder_call_count
        global global_counter
        adder_call_count += 1
        global_counter['Adder'] = adder_call_count        
        return adder_call_count
    def multiplier():
        nonlocal multiplier_call_count
        global global_counter
        multiplier_call_count += 1
        global_counter['Multiplier'] = multiplier_call_count        
        return multiplier_call_count
    def divider():
        nonlocal divider_call_count
        global global_counter
        divider_call_count += 1
        global_counter['Divider'] = divider_call_count        
        return divider_call_count
    
    return adder, multiplier, divider

# global_counter={}
def accntrOperations(accnt_dict):
    """
    Closure that keeps track of how many times each function was called
    and also updates a user defined dictionary with the number of function calls
    """
    adder_call_count = 0
    multiplier_call_count = 0
    divider_call_count = 0
    accnt_stored_dict = accnt_dict
    def adder():
        nonlocal adder_call_count
        nonlocal accnt_stored_dict
        adder_call_count += 1
        accnt_stored_dict['Adder'] = adder_call_count        
        return adder_call_count
    def multiplier():
        nonlocal multiplier_call_count
        nonlocal accnt_stored_dict
        multiplier_call_count += 1
        accnt_stored_dict['Multiplier'] = multiplier_call_count        
        return multiplier_call_count
    def divider():
        nonlocal divider_call_count
        nonlocal accnt_stored_dict
        divider_call_count += 1
        accnt_stored_dict['Divider'] = divider_call_count        
        return divider_call_count
    
    return adder, multiplier, divider