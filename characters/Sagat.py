import time

class Sagat:
	def __init__(self):
		self.name = "Sagat"
		self.combos = {
					   "tiger shot":self.tiger_shot,
					   "ground_tiger_shot":self.ground_tiger_shot,
					   "tiger_blow":self.tiger_blow,
					   "tiger_crush":self.tiger_crush,
					   "tiger_cannon":self.tiger_cannon,
					   "tiger_raid":self.tiger_raid,
					   }
	
	def tiger_shot(self, kb, lut):
		r = lut['r']
		l = lut['l']
		d = lut['d']
		lp = lut['lp']
		#--------------------
		time.sleep(0.3)
		print ">> tiger shot !"
		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(r)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)
		kb.press_key(lp)
		time.sleep(0.1)
		kb.release_key(lp)
		kb.release_key(r)

		time.sleep(0.3)
		print "<< tiger shot !"
		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(l)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)
		kb.press_key(lp)
		time.sleep(0.1)
		kb.release_key(lp)
		kb.release_key(l)
		
		
	def ground_tiger_shot(self, kb, lut):
		r = lut['r']
		l = lut['l']
		d = lut['d']
		lk = lut['lk']
		#--------------------
		time.sleep(0.3)
		print ">> ground tiger shot !"
		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(r)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)
		kb.press_key(lk)
		time.sleep(0.1)
		kb.release_key(lk)
		kb.release_key(r)

		time.sleep(0.3)
		print "<< ground tiger shot !"
		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(l)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)
		kb.press_key(lk)
		time.sleep(0.1)
		kb.release_key(lk)
		kb.release_key(l)
		
		
	def tiger_blow(self, kb, lut):
		r = lut['r']
		l = lut['l']
		d = lut['d']
		lp = lut['lp']
		#-----------------------
		time.sleep(0.3)
		print ">> tiger_blow !"
		kb.press_key(r)
		time.sleep(0.05)
		kb.release_key(r)
		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(r)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)
		kb.press_key(lp)
		time.sleep(0.1)
		kb.release_key(lp)
		kb.release_key(r)
	
		time.sleep(0.3)
		print "<< tiger_blow !"
		kb.press_key(l)
		time.sleep(0.05)
		kb.release_key(l)
		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(l)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)
		kb.press_key(lp)
		time.sleep(0.1)
		kb.release_key(lp)
		kb.release_key(l)
		
	def tiger_crush(self, kb, lut):
		r = lut['r']
		l = lut['l']
		d = lut['d']
		lk = lut['lk']
		#-----------------------
		time.sleep(0.3)
		print ">> tiger_crush !"
		kb.press_key(r)
		time.sleep(0.05)
		kb.release_key(r)
		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(r)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)
		kb.press_key(lk)
		time.sleep(0.1)
		kb.release_key(lk)
		kb.release_key(r)
	
		time.sleep(0.3)
		print "<< tiger_crush !"
		kb.press_key(l)
		time.sleep(0.05)
		kb.release_key(l)
		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(l)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)
		kb.press_key(lk)
		time.sleep(0.1)
		kb.release_key(lk)
		kb.release_key(l)
		
		
		
	def tiger_cannon(self, kb, lut):
		r = lut['r']
		l = lut['l']
		d = lut['d']
		lp = lut['lp']
		#--------------
		time.sleep(0.3)
		print ">> tiger_cannon !"
		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(r)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)
		kb.release_key(r)

		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(r)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)

		kb.press_key(lp)
		time.sleep(0.1)
		kb.release_key(lp)
		kb.release_key(r)
	
		time.sleep(0.3)
		print "<< tiger_cannon !"
		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(l)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)
		kb.release_key(l)

		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(l)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)

		kb.press_key(lp)
		time.sleep(0.1)
		kb.release_key(lp)
		kb.release_key(l)
		
		
	def tiger_raid(self, kb, lut):
		r = lut['r']
		l = lut['l']
		d = lut['d']
		lk = lut['lk']
		#--------------
		time.sleep(0.3)
		print ">> tiger_raid / genocide !"
		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(r)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)
		kb.release_key(r)

		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(r)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)

		kb.press_key(lk)
		time.sleep(0.1)
		kb.release_key(lk)
		kb.release_key(r)
	
		time.sleep(0.3)
		print "<< tiger_raid /genocide !"
		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(l)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)
		kb.release_key(l)

		kb.press_key(d)
		time.sleep(0.05)
		kb.press_key(l)
		time.sleep(0.05)
		kb.release_key(d)
		time.sleep(0.05)

		kb.press_key(lk)
		time.sleep(0.1)
		kb.release_key(lk)
		kb.release_key(l)
		
		
	
		
	
