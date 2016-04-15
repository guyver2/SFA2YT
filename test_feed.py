from PySide import QtGui
import sys
import cv2
import numpy as np
import random
import time
from threading import Thread, Lock

from pykeyboard import PyKeyboard
from characters import *
from Player import Key, Player, RectArea


class myKeyboard(PyKeyboard):
	def __init__(self):
		super(myKeyboard, self).__init__()
		self.mutex = Lock()
	
	def release_key(self, k):
		self.mutex.acquire()
		super(myKeyboard, self).release_key(k)
		self.mutex.release()
	
	def press_key(self, k):
		self.mutex.acquire()
		super(myKeyboard, self).press_key(k)
		self.mutex.release()
	



class KeyOutput:
	def __init__(self, players):
		self.players = dict([(id(p), p) for p in players]) # keep references to players for combos
		self.keys = {}
		for p in players:
			for k in p.keys:
				if 'combo' not in k.key:
					self.keys[k.key] = False
		self.combos = dict([(id(p), None) for p in players])
		self.kb = myKeyboard()


	def reset(self, hard=False):
		for k in self.keys :
			self.kb.release_key(k)
			self.keys[k] = False
		if hard: # hard reset, build new keyboard object
			print "hard reset"
			del self.kb
			self.kb = myKeyboard()
	

	def update(self, newkeys, send=True):
		if send == False :
			self.reset()
		else :
			for k in self.keys :
				# key is present and wasn't pressed before
				if k in newkeys and not self.keys[k]:
					# check if the key belongs to a player performing a combo
					valid = True
					for pid, p in self.players.iteritems():
						if (self.combos[pid] is not None) and (self.combos[pid].isAlive()) and (k in p.listKey) :
							valid = False
					if valid :
						#print "pressing", k
						self.kb.press_key(k)
						self.keys[k] = True
				# key was pressed before but is no longer present
				elif self.keys[k] and not k in newkeys:
					# check if the key belongs to a player performing a combo
					valid = True
					for pid, p in self.players.iteritems():
						if (self.combos[pid] is not None) and (self.combos[pid].isAlive()) and (k in p.listKey) :
							valid = False
					if valid :
						#print "releasing", k
						self.kb.release_key(k)
						self.keys[k] = False

			for pid, p in self.players.iteritems():
				if str(pid)+'_combo' in newkeys and p.SFchar != None:
					# check if player is curently not performing a combo
					if (self.combos[pid] is None) or (not self.combos[pid].isAlive()):
						# cancel all keys for that player
						p.cancelKeys(self.kb, self.keys)
						# launch combos
						combo = random.choice(p.SFchar.combos.keys())
						print "combo", combo, "from", p.SFchar.name,
						self.combos[pid] = Thread(target=p.SFchar.combo, args=(p.SFchar.combos[combo], self.kb, p.lut, self))
						self.combos[pid].start()
					
				
					
		
		


def callKeys(keys):
	
	pass



def initKeyMapSquare(shape):
	keymap = []
	dx = shape[0]/2
	dy = shape[1]/3
	keymap.append(Key(dx*0, dy*0, dx, dy, 'w', 'u'))
	keymap.append(Key(dx*0, dy*1, dx, dy, 's', 'd'))
	keymap.append(Key(dx*0, dy*2, dx, dy, 'a', 'l'))
	keymap.append(Key(dx*1, dy*0, dx, dy, 'd', 'r'))
	keymap.append(Key(dx*1, dy*1, dx, dy, 'z', 'lk'))
	keymap.append(Key(dx*1, dy*2, dx, dy, 'x', 'lp'))
	return keymap
	


def initKeyMapShark(shape):
	keymap = []
	w, h = float(shape[0]), float(shape[1])
	dw = w/20
	dh = h/20
	keymap.append(Key(4*dw, dh, 4*dw, 3.5*dh, 't', 'lk'))
	keymap.append(Key(4*dw, 5.5*dh, 4*dw, 3.5*dh, 'y', 'mk'))
	keymap.append(Key(4*dw, 10*dh, 4*dw, 3.5*dh, 'g', 'lp'))
	keymap.append(Key(4*dw, 14.5*dh, 4*dw, 3.5*dh, 'h', 'mp'))
	keymap.append(Key(8*dw, dh, 4*dw, 3.5*dh, 'l', 'r'))
	keymap.append(Key(8*dw, 5.5*dh, 4*dw, 3.5*dh, 'u', 'hk'))
	keymap.append(Key(8*dw, 10*dh, 4*dw, 3.5*dh, 'j', 'l'))
	keymap.append(Key(8*dw, 14.5*dh, 4*dw, 3.5*dh, 'o', 'hp'))
	keymap.append(Key(12*dw, dh, 4*dw, 6*dh, 'i', 'u'))
	keymap.append(Key(12*dw, 12*dh, 4*dw, 6*dh, 'k', 'd'))
	keymap.append(Key(12*dw, 8*dh, 4*dw, 3*dh, 'combo', 'combo'))
	return keymap




def initKeyMapRotonde(shape):
	keymap = []
	w, h = float(shape[0]), float(shape[1])
	dw = w/20
	dh = h/20
	keymap.append(Key(2*dw, dh, 4*dw, 3.5*dh, 'z', 'lk'))
	keymap.append(Key(2*dw, 5.5*dh, 4*dw, 3.5*dh, 'x', 'mk'))
	keymap.append(Key(2*dw, 10*dh, 4*dw, 3.5*dh, 'c', 'lp'))
	keymap.append(Key(2*dw, 14.5*dh, 4*dw, 3.5*dh, 'v', 'mp'))
	keymap.append(Key(7*dw, dh, 5*dw, 3.5*dh, 'd', 'r'))
	keymap.append(Key(7*dw, 5.5*dh, 5*dw, 3.5*dh, 'e', 'hk'))
	keymap.append(Key(7*dw, 10*dh, 5*dw, 3.5*dh, 'a', 'l'))
	keymap.append(Key(7*dw, 14.5*dh, 5*dw, 3.5*dh, 'q', 'hp'))
	keymap.append(Key(13*dw, dh, 5.5*dw, 6*dh, 'w', 'u'))
	keymap.append(Key(13*dw, 12*dh, 5.5*dw, 6*dh, 's', 'd'))
	keymap.append(Key(12*dw, 8*dh, 6.5*dw, 3*dh, 'combo', 'combo'))
	return keymap


#------------   BLOB detector parametrization
def initDetectorRotonde():
	# Setup SimpleBlobDetector parameters.
	params = cv2.SimpleBlobDetector_Params()
	 
	# Change thresholds
	params.filterByColor = False;
	#params.minThreshold = 10;
	#params.maxThreshold = 255;
	 
	# Filter by Area.
	params.filterByArea = True
	params.minArea = 30
	params.maxArea = 1400
	 
	# Filter by Circularity
	params.filterByCircularity = False
	#params.minCircularity = 0.70
	 
	# Filter by Convexity
	params.filterByConvexity = True
	params.minConvexity = 0.70
	 
	# Filter by Inertia (how round the object is)
	params.filterByInertia = False
	#params.minInertiaRatio = 0.1
	#params.maxInertiaRatio = 0.5
	 
	# Create a detector with the parameters
	ver = (cv2.__version__).split('.')
	if int(ver[0]) < 3 :
		detector = cv2.SimpleBlobDetector(params)
	else : 
		detector = cv2.SimpleBlobDetector_create(params)
	
	return detector


def initDetectorShark():
	# Setup SimpleBlobDetector parameters.
	params = cv2.SimpleBlobDetector_Params()
	 
	# Change thresholds
	params.filterByColor = False;
	#params.minThreshold = 10;
	#params.maxThreshold = 255;
	 
	# Filter by Area.
	params.filterByArea = True
	params.minArea = 200
	params.maxArea = 1400
	 
	# Filter by Circularity
	params.filterByCircularity = False
	#params.minCircularity = 0.70
	 
	# Filter by Convexity
	params.filterByConvexity = True
	params.minConvexity = 0.70
	 
	# Filter by Inertia (how round the object is)
	params.filterByInertia = False
	#params.minInertiaRatio = 0.1
	#params.maxInertiaRatio = 0.5
	 
	# Create a detector with the parameters
	ver = (cv2.__version__).split('.')
	if int(ver[0]) < 3 :
		detector = cv2.SimpleBlobDetector(params)
	else : 
		detector = cv2.SimpleBlobDetector_create(params)
	
	return detector


#-------------------------------------------------------------------------------
#            Main window
#-------------------------------------------------------------------------------

class MainWindow(QtGui.QMainWindow):
	def __init__(self, players):
		super(MainWindow, self).__init__()
		self.state = False
		self.players = players
		self.but1 = QtGui.QPushButton("Turn On", self)
		self.butReset = QtGui.QPushButton("Reset", self)
		self.mainWidg = QtGui.QWidget(self)
		layout = QtGui.QHBoxLayout(self.mainWidg)
		layout.addWidget(self.but1)
		layout.addWidget(self.butReset)
		self.mainWidg.setLayout(layout)
		self.setCentralWidget(self.mainWidg)
		self.but1.pressed.connect(self.butPressed)
		self.butReset.pressed.connect(self.butResetPressed)
	
	def butResetPressed(self):
		for p in self.players:
			p.resetBG()

	def butPressed(self):
		if self.state:
			self.but1.setText("Turn On")
			self.state = False
		else :
			self.but1.setEnabled(False)
			# add delay to let the use click on the window
			time.sleep(3)
			self.but1.setText("Turn Off")
			self.but1.setEnabled(True)
			self.state = True




#-------------------------------------------------------------------------------
#
#                                 MAIN
#
#-------------------------------------------------------------------------------




if __name__=="__main__":
	
	app = QtGui.QApplication(sys.argv)

	rotondeArea = RectArea(3,196,639,359)
	rotonde = Player('rotonde', rotondeArea, initKeyMapRotonde, initDetectorRotonde(), 0.8, 50, Ryu())
	
	sharkArea = RectArea(682,196,639,359)
	shark = Player('shark', sharkArea, initKeyMapShark, initDetectorShark(), 0.8, 120, Sagat())
	
	players = [shark, rotonde]

	win = MainWindow(players)
	win.show()
	
	keyOut = None

	
	while True:
		keys = []
		for p in players:
			keys.extend(p.getKeys())
			
		if keyOut == None:
			keyOut = KeyOutput(players)
		#print '#######', keys
		keyOut.update(keys, win.state)
		#if win.state :
		#	callKeys(keys)
		
		ch = 0xFF & cv2.waitKey(1)
		if ch == 27 or ch == ord('q') : # escape 
			break
		elif ch == ord('r'): # reset background model
			for p in players :
				p.resetBG()
			
	cv2.destroyAllWindows()	
	del app

