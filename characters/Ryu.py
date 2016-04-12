import time

class Ryu:
	def __init__(self):
		self.name = "Ryu"
		self.combos = {
					   "hadouken":self.hadouken,
					   "shoryuken":self.shoryuken,
					   "senpuu kyaku":self.senpuu_kyaku,
					   "sakotsu wari":self.sakotsu_wari,
					   "shinkuu hadouken":self.shinkuu_hadouken,
					   "shinkuu tatsumaki senpuukyaku":self.shinkuu_tatsumaki_senpuukyaku,
					   }

	
	
	def shinkuu_hadouken(self, kb, lut):
		r = lut['r']
		l = lut['l']
		d = lut['d']
		lp = lut['lp']
		#--------------
		time.sleep(0.3)
		print ">> Shinkuu hadouken !"
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
		print "<< Shinkuu hadouken !"
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
	


	def shinkuu_tatsumaki_senpuukyaku(self, kb, lut):
		r = lut['r']
		l = lut['l']
		d = lut['d']
		lk = lut['lk']
		
		time.sleep(0.3)
		print ">> Shinkuu Tatsumaki Senpuukyaku !"
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

		time.sleep(0.3)
		print "<< Shinkuu Tatsumaki Senpuukyaku !"
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
	
	
	
	def sakotsu_wari(self, kb, lut):
		r = lut['r']
		l = lut['l']
		mp = lut['mp']
		
		time.sleep(0.3)
		print ">> sakotsu wari"
		kb.press_key(r)
		time.sleep(0.05)
		kb.press_key(mp)
		time.sleep(0.1)
		kb.release_key(r)
		kb.release_key(mp)

		time.sleep(0.3)
		print ">> sakotsu wari"
		kb.press_key(l)
		time.sleep(0.05)
		kb.press_key(mp)
		time.sleep(0.1)
		kb.release_key(l)
		kb.release_key(mp)
	
	
	def senpuu_kyaku(self, kb, lut):
		r = lut['r']
		l = lut['l']
		mk = lut['mk']
		
		time.sleep(0.3)
		print ">> senpuu kyaku"
		kb.press_key(r)
		time.sleep(0.05)
		kb.press_key(mk)
		time.sleep(0.1)
		kb.release_key(r)
		kb.release_key(mk)
	
		time.sleep(0.4)
		print "<< senpuu kyaku"
		kb.press_key(l)
		time.sleep(0.05)
		kb.press_key(mk)
		time.sleep(0.1)
		kb.release_key(l)
		kb.release_key(mk)
	
	
	def hadouken(self, kb, lut):
		r = lut['r']
		l = lut['l']
		d = lut['d']
		lp = lut['lp']
		#--------------------
		time.sleep(0.3)
		print ">> hadouken !"
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
		print "<< hadouken !"
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
	
	def shoryuken(self, kb, lut):
		r = lut['r']
		l = lut['l']
		d = lut['d']
		lp = lut['lp']
		#-----------------------
		time.sleep(0.3)
		print ">> shoryuken !"
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
		print "<< shoryuken !"
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
