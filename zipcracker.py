#!/usr/bin/python
# Usages :
usage = "usage: %prog [options] "
# Version
Version="%prog 0.0.1"

import zipfile,optparse,sys,fileinput,time
class main:
	def __init__(self):
		self.extract_input_data()
		self.check_input_conditions()
		self.start_cracking_engine()

	def time_management(self):
		print "[*]      Starting Time ",self.starttime
		print "[*]      Closing  Time ",self.closetime
		print "[*]      Password Try ",self.pwdtries
		print "[*]      Average Speed ",self.pwdtries/(self.closetime-self.starttime)
		return

	def start_cracking_engine(self):
		print "[+]    Loading zipfile....",
		fileload=zipfile.ZipFile(self.filename)
		print "ok"
		if self.dictionery:
			print "[+]  Using Dictionery option...ok"
			print "[+]  Loading Dictionery File...ok"
			print "[+]  Brute Force Started..."
			for i in fileinput.input(self.dictionery):
				pwd=i.strip('\n')
				self.extracting_engine(fileload,pwd)

		if self.crunch:
			print "[+] Connection Stablished as Pipe.... ok"
			print "[+] Brute Force Started..."
			for i in sys.stdin:
				pwd=i.strip('\n')
				self.extracting_engine(fileload,pwd)
		self.show_info_message()

		return

	def check_input_conditions(self):
		if not self.filename:
			print "[Error] Please Provide Zip File Path"
			sys.exit(0)
		print "    ok"

		if not self.dictionery and not self.crunch:
			print "[Error Please Provide Dictionery or crunch or Password option"
			sys.exit(0)
		if self.dictionery and self.crunch:
			print "[Error Please choose any option from dict or crunch"
			sys.exit(0)
		return

	def extracting_engine(self,file,pwd):
		self.pwdresult=None
		try:
			file.extractall(self.output,pwd=str(pwd))
			self.show_info_message(pwd=pwd)
			self.pwdresult=true
		except Exception as e:
			if str(e).find('Permission')!=-1:
				self.show_info_message(pwd=pwd)
				self.pwdresult=True

			else:
				self.pwdresult=None
		self.pwdtries=self.pwdtries+1

		return

	def show_info_message(self,pwd=None):
		if pwd:
			data="\n\t !- Congratulation -! \n\tPassword Found ="+pwd+'\n'
		else:
			data="\n\t Sorry! Password Not Found \n\n"
		print data
		if self.result:
			print "[+] Saving output in ",self.result
			f=open(self.result,'a')
			f.write(data)
			f.close()
		self.closetime=time.time()
		self.time_management()
		if pwd:
			print "[+] Exiting"
			sys.exit(0)
		return

	def extract_input_data(self):
		self.starttime=time.time()
		self.pwdtries=0

		parser = optparse.OptionParser(usage, version=Version)
		parser.add_option("-f", "--file", action="store", type="string", dest="filename",help="Please Specify Path of Zip File", default=None)
		parser.add_option("-d", "--dict", action="store", type="string", dest="dictionery", help="Please Specify Path of Dictionery.", default=None)
		parser.add_option("-o", "--output", action="store", type="string", dest="output", help="Please Specify Path for Extracting", default='.')
		parser.add_option("-r", "--result", action="store", type="string", dest="result", help="Please Specify Path if You Want to Save Result", default=None)
		parser.add_option("-c", "--crunch", action="store", type="string", dest="crunch", help="For Using Passwords Directly from crunch use this arguments: -c True or --crunch True", default=None)
		(option, args)=parser.parse_args()


		print "[+] Extracting Input Data..."
		self.filename=option.filename
		self.dictionery=option.dictionery
		self.output=option.output
		self.result=option.result
		self.crunch=option.crunch
		return

if __name__ == '__main__':
	main()
