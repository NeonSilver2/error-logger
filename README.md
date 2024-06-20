# error-logger
Intent:   portfolio project for resume; logs in text file function calls, args, and kwargs, and also reports on errors


I am including 2 files: 
A) The decorator that logs the functions it's tagged on with a brief description of what it's called and what args and kwargs were passed to it, as well as what the result of that function call was, or the errors that the function expereiences or raises.
B) A sample of code that imports the first file and uses it, as a demonstration to use with the first file.

The logger will write to a file called "debug_log.txt" in the same directory that you download and run the file containing the logger code. It is done as an append to the file, so if you already have a file by that name, it will log the information at the end of the file and should not damage any existing data. If you do not already have a "debug_log.txt" at that directory, it will make one.

- NeonSilver2 (Jun 20, 2024)
