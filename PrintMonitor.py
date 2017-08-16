# imports======================================================
import win32print

wp = win32print

ptypelist = [(wp.PRINTER_ENUM_SHARED,'SHARED'),(wp.PRINTER_ENUM_LOCAL,'LOCAL'),(wp.PRINTER_ENUM_NETWORK,'NETWORK')]

class PMFunc():
	"""docstring for PMFunc"""
	def __init__(self):
		
		self.Plist = []

	def PrinterList(self):
		
		tmpdic = {}
		for pt in ptypelist:
			try:
				for (Flags,pDescription,pName,pComment) in list(win32print.EnumPrinters(pt[0],None,1)):

					tmpdic = {}
					tmpdic['PType'] = pt[1]
					tmpdic['Flags']	= Flags
					tmpdic['Description'] = pDescription
					tmpdic['Name'] = pName
					tmpdic['Comment'] = pComment
					self.Plist.append(tmpdic)
			except:
				pass
		return self.Plist
		# print(self.Plist)
	
	def GetJobList(self,printer):
		
		phandle = win32print.OpenPrinter(printer)
		jlist = win32print.EnumJobs(phandle,0,-1,1)
		win32print.ClosePrinter(phandle)
		return jlist


pm_obj = PMFunc()
for printer in pm_obj.PrinterList():
	try:
		printer_joblist = pm_obj.GetJobList(printer['Name'])
		print(printer_joblist)
	except:
		pass