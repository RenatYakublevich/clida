from clida.visualizer import Visualizer
from clida.progress import ProgressBar
import time


prg = ProgressBar()
for _ in prg.progressBar(list(range(1,100))):
	time.sleep(1)



