from PySide.QtGui import QPixmap, QApplication
from PySide.QtCore import QBuffer, QIODevice
import StringIO
import sys
import Image
import cv2
import numpy as np

from BGModel import BGmodel

class Key():
	# area : rectangular area, see class definition bellow
	# k : key that should be sent when area is activated
	def __init__(self, x, y, w, h, k, snesKey):
		self.area = RectArea(x, y, w, h)
		self.key = k
		self.snesKey = snesKey
			

class RectArea():
	def __init__(self, x, y, w, h):
		self.x = int(x)
		self.y = int(y)
		self.w = int(w)
		self.h = int(h)
	
	def isIn(self, x, y):
		return (self.x <= x <= self.x+self.w and self.y <= y <= self.y+self.h)
			
			
			
			
#-------------------------------------------------------------------------------
#
#                                PLAYER CLASS
#
#-------------------------------------------------------------------------------

class Player():
	def __init__(self, name, screenArea, keymapFunc, detector, scale=0.8, threshLum=50, SFchar=None):
		self.name = name
		self.keymapFunc = keymapFunc
		self.keys = None
		self.listKey = [] # list of keyboard keys reserved for this player
		 # look up table to map snes key to keyboard key
		self.lut = dict([(sk, None) for sk in ['u', 'd', 'l', 'r', 'lk', 'mk', 'hk', 'lp', 'mp', 'hp']])
		self.SFchar = SFchar
		self.threshLum = threshLum
		self.screenArea = screenArea
		self.detector = detector
		# morphological structuring element to clean the image
		self.kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
		self.scale = scale
		self.bgmodel = None
		self.idFrame = 0
		self.buffer = QBuffer()
		self.buffer.open(QIODevice.ReadWrite)

	
	
	def grabImg(self):
		self.idFrame += 1	
		wid = QApplication.desktop().winId()
		QPixmap.grabWindow(wid, self.screenArea.x, self.screenArea.y, self.screenArea.w, self.screenArea.h).save(self.buffer, 'png')
		strio = StringIO.StringIO()
		strio.write(self.buffer.data())
		self.buffer.seek(0)
		strio.seek(0)
		pix = np.array(Image.open(strio))
		pix = cv2.resize(pix, (0,0), fx=self.scale, fy=self.scale)
		real_color = cv2.cvtColor(pix, cv2.COLOR_BGR2RGB)
		return real_color
	
	
	def process(self, real_color, draw = True):
		gray = cv2.cvtColor(real_color, cv2.COLOR_RGB2GRAY)
		if self.keys == None:
			self.keys = self.keymapFunc(gray.shape)
			for k in self.keys:
				if 'combo' in k.key:
					k.key = str(id(self))+'_combo'
				else :
					self.listKey.append(k.key)
			# build look up table 
			for sk in self.lut:
				for kk in self.keys:
					if kk.snesKey == sk:
						self.lut[sk] = kk.key
						break
		if self.bgmodel is None:
			self.bgmodel = BGmodel(100, gray.shape)
		
		if self.idFrame%10==0 or not self.bgmodel.ready :
			#print self.idFrame, "adding image"
			self.bgmodel.add(gray)

		BG = self.bgmodel.getModel()
		FG = self.bgmodel.apply(gray)
		
		img = cv2.medianBlur(FG,5)
		ret, bin = cv2.threshold(img, self.threshLum, 255, cv2.THRESH_BINARY)
		
		fgmask = cv2.morphologyEx(FG, cv2.MORPH_OPEN, self.kernel)
		fgmask = cv2.morphologyEx(FG, cv2.MORPH_CLOSE, self.kernel)      
		fgmask = cv2.morphologyEx(FG, cv2.MORPH_CLOSE, self.kernel)
		# blob detection only if we gathered enough images for the background model
		if self.bgmodel.ready or True:
			keypoints = self.detector.detect(FG)
		else:
			keypoints = []
		
		if draw :
			# Draw detected blobs as red circles.
			real_color = cv2.drawKeypoints(real_color, keypoints, np.array([]), (0,0,255), 4)
		return [k.pt for k in keypoints], real_color, BG, FG, bin
		
		
	

	def getKeys(self, draw=True):
		keys = []
		
		ori = self.grabImg()
		blobs, ori, BG, FG, bin = self.process(ori)	
			
		for k in self.keys:
			x, y, w, h = k.area.x, k.area.y, k.area.w, k.area.h
			cv2.rectangle(ori, (y, x), (y+h,x+w), (0,255,0), 1)
			cv2.putText(ori, k.key, (y+10,x+20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0),2)
			for p in blobs:
				if k.area.isIn(p[1], p[0]):
					keys.append(k.key)
					if ori is not None :
						cv2.rectangle(ori, (y, x), (y+h,x+w), (0,0,255), 2)
					break
				
		if draw :
			cv2.imshow(self.name+"_color input", ori)
			cv2.imshow(self.name+"_BG model", BG)
			#cv2.imshow(self.name+"_FG model", FG)
			#cv2.imshow(self.name+"_binary image", bin)

		return keys
		
	# release all keys associated to a player, before a combo
	def cancelKeys(self, kb, keys):
		for k in self.keys :
			if 'combo' not in k.key:
				kb.release_key(k.key)
				keys[k.key] = False

		
	def resetBG(self):
		self.bgmodel = None
