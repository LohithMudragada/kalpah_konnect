import win32print
import shutil
import time

wp = win32print

ptypelist = [(wp.PRINTER_ENUM_SHARED,'SHARED'),(wp.PRINTER_ENUM_LOCAL,'LOCAL'),(wp.PRINTER_ENUM_NETWORK,'NETWORK')]
cmds = {'Pause':wp.JOB_CONTROL_PAUSE,'CANCEL':wp.JOB_CONTROL_CANCEL,'RESUME':wp.JOB_CONTROL_RESUME,'prior_low':wp.MIN_PRIORITY,'prior_high':wp.MAX_PRIORITY,'prior_normal':wp.DEF_PRIORITY}
status = {'deleting':wp.JOB_STATUS_DELETING,'error':wp.JOB_STATUS_ERROR,'offline':wp.JOB_STATUS_OFFLINE,'paper out':wp.JOB_STATUS_PAPEROUT,'paused':wp.JOB_STATUS_PAUSED,'printed':wp.JOB_STATUS_PRINTED,'printing':wp.JOB_STATUS_PRINTING,'spooling':wp.JOB_STATUS_SPOOLING}

class PMFunc():
	"""docstring for PMFunc"""
	def __init__(self):

		self.PList = []

	def PrinterList(self):

		tmpdic = {}
		for pt in ptypelist:
			try:
				for (Flags,pDescription,pName,pComment) in list(win32print.EnumPrinters(pt[0],None,1)):
					tmpdic = {}
					tmpdic['PType'] = pt[1]
					tmpdic['Flags'] = Flags
					tmpdic['Description'] = pDescription
					tmpdic['Name'] = pName
					tmpdic['Comment'] = pComment
					self.PList.append(tmpdic)

			except:
				pass
		return self.PList
	def GetJobList(self,printer):

		phandle = win32print.OpenPrinter(printer)
		jlist = win32print.EnumJobs(phandle,0,-1,1)
		win32print.ClosePrinter(phandle)
		return jlist

	def GetJobInfo(self,printer,jobID):
		phandle = win32print.OpenPrinter(printer)
		ilist = win32print.GetJob(phandle,jobID,1)
		win32print.ClosePrinter(phandle)
		return ilist

	# def CopyandClear(self,printer,jobID):
		
	# 	if(jobid < 10):
	# 		jobid = '0000'+ str(jobid)
	# 	else:
	# 		if(jobid<100):
	# 			jobid = '000'+ str(jobid)
	# 		else:
	# 			if(jobid<1000):
	# 				jobid = '00'+ str(jobid)
	# 			else:
	# 				if(jobid<10000):
	# 					jobid = '0'+ str(jobid)
	# 				else:
	# 					jobid = str(jobid)
	# 	source_path = r"C:\\Windows\\System32\\spool\\PRINTERS"+jobid+".SPL"
	# 	dest_path = r"C:\Spool"+jobid+".SPL"
	# 	shutil.copy(source_path,dest_path)
	# 	print(copied)
while 1:
		
	def print_job():

		pm_obj = PMFunc()
		for printer_name in pm_obj.PrinterList():
			try:
				printer_joblist = pm_obj.GetJobList(printer_name['Name'])
				for job_info in printer_joblist:
					# print(pm_obj.GetJobInfo(printer_name['Name'],w['JobId']))
					f = pm_obj.GetJobInfo(printer_name['Name'],job_info['JobId'])
					print(f['TotalPages'],f['PagesPrinted'])
					if(f['TotalPages'] == f['PagesPrinted']):
						print(f['JobId'])
						# CopyandClear(f['Name'],f['JobId'])
			except:
				pass

	# x = print_job()
	# print(x)