"""
This program is a portfolio project and is meant to demonstrate ability, not to be an all-purpose error logging tool. If you wish to use it as such, make sure the error types you wish to catch are included in the function below. I would also recommend a bit of cleaning of output text format, as it could always be prettier! 
"""

import datetime as dt
import os

txt_log_location = os.path.dirname(os.path.abspath(__file__))  # file path base for debug_log.txt


# Decorator definition for "Function Logger"
def function_logger(func):
    def logged_function(*args,**kwargs):
        log_file = open(f"{txt_log_location}/debug_log.txt","a+")
        try:
            results = func(*args,**kwargs)
            with log_file as f:
                f.write(f"{dt.datetime.now()}:    Method {func.__name__} called with {args} as Args and {kwargs} as KWArgs. \n")
                f.write(f"{dt.datetime.now()}:    Results of {func.__name__} are:  {results}. \n\n\n")
            return results
        except TypeError:
            with log_file as f:
                f.write(f"{dt.datetime.now()}:    Method {func.__name__} experienced a error! \n                               TypeError occurred when called with {args} as Args and {kwargs} as KWArgs.  \n")
            return "<TypeError raised and logged>"
        except ValueError:
            with log_file as f:
                f.write(f"{dt.datetime.now()}:    Method {func.__name__} experienced a error! \n                               ValueError occurred when called with {args} as Args and {kwargs} as KWArgs.  \n")
            return "<ValueError raised and logged>"
        except:
            with log_file as f:
                f.write(f"{dt.datetime.now()}:    Method {func.__name__} experienced a error! \n                               (Unspecified Error) occurred when called with {args} as Args and {kwargs} as KWArgs.  \n")
            return "<(Unspecified Error) occured and was logged>"
    return logged_function
