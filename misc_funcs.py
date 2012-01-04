import svlgui
from threading import Event, Thread

def select_any(self):
	svlgui.MODE = " "
def resize_any(self):
	svlgui.MODE = " "
def lasso(self):
	svlgui.MODE = "l"
def text(self):
	svlgui.MODE = "t"
def rectangle(self):
	svlgui.MODE = "r"
def ellipse(self):
	svlgui.MODE = "e"
def curve(self):
	svlgui.MODE = "c"
def paintbrush(self):
	svlgui.MODE = "p"
def pen(self):
	svlgui.MODE = "n"
def paint_bucket(self):
	svlgui.MODE = "b"
	
def box(x, y, width, height, fill):
	global objects
	box = svlgui.Shape(x, y)
	box.shapedata = [["M",0,0],["L",width,0],["L",width,height],["L",0,height],["L",0,0]]
	box.fillcolor = svlgui.Color(fill)
	box.linecolor = svlgui.Color("#cccccc")
	box.filled = True
	return box


	
	
# Timer module - not mine

# Copyright (c) 2009 Geoffrey Foster
# 
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
# 
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

class RepeatTimer(Thread):
    def __init__(self, interval, function, iterations=0, args=[], kwargs={}):
        Thread.__init__(self)
        self.interval = interval
        self.function = function
        self.iterations = iterations
        self.args = args
        self.kwargs = kwargs
        self.finished = Event()
 
    def run(self):
        count = 0
        while not self.finished.is_set() and (self.iterations <= 0 or count < self.iterations):
			try:
				self.finished.wait(self.interval)
				if not self.finished.is_set():
					#print self.function
					self.function(*self.args, **self.kwargs)
					count += 1
			except Exception as e:
				self.cancel()
 
    def cancel(self):
        self.finished.set()