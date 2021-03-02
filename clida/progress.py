import time


class ProgressBar:
	@staticmethod
	def progressBar(iterable, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
	    """
	    @params:
	        iteration   - Обязательный  : объект по которому нужно интерироваться
	        prefix      - Опцианальный  : префикс (Str)
	        suffix      - Опцианальный  : суффикс (Str)
	        decimals    - Опцианальный  : positive number of decimals in percent complete (Int)
	        length      - Опцианальный  : character length of bar (Int)
	        fill        - Опцианальный  : bar fill character (Str)
	        printEnd    - Опцианальный  : end character (e.g. "\r", "\r\n") (Str)
	    """
	    total = len(iterable)
	    # Progress Bar Printing Function
	    def printProgressBar (iteration):
	        percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
	        filledLength = int(length * iteration // total)
	        bar = fill * filledLength + '-' * (length - filledLength)
	        print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
	    # Initial Call
	    printProgressBar(0)
	    # Update Progress Bar
	    for i, item in enumerate(iterable):
	        yield item
	        printProgressBar(i + 1)
	    # Print New Line on Complete
	    print()

	