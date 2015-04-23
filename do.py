#
# do.py

import getopt
import sys
from java.io import FileInputStream

def manageTasks(taskList):
	while true:
		allDone=true
		print "\n==="
	   	for task in taskList:
			running=task.isRunning()
			print "\n", task, "\n", running, task.getDescription(), task.getStatus(), "\n", task.getError()
	   		if running<>0:
				allDone=false
		if allDone:
	   		break
		java.lang.Thread.sleep(10000)

def manageProgress(progress):
	while progress.isRunning():
		print "\n==="
		progress.getMessage()
		progress.printStatus()
		java.lang.Thread.sleep(10000)
	if progress.isFailed():
		print "ERROR", progress.getMessage(), progress.printStatus()
		sys.exit(2)
	
		

def actionStartServer(conf, serverList):
	connect(conf["admsrv.login"], conf["admsrv.password"],conf["admsrv.url"])
	taskList=[]
	for serverName in serverList:
		print "serverName", serverName
		taskList.append(start(serverName, 'Server', block='false'))
	manageTasks(taskList)
	disconnect()


def actionStopServer(conf, serverList):
	connect(conf["admsrv.login"], conf["admsrv.password"],conf["admsrv.url"])
	domainRuntime()
	taskList=[]
	for serverName in serverList:
		   taskList.append(cmo.lookupServerLifeCycleRuntime(serverName).shutdown())
	manageTasks(taskList)
	disconnect()


def actionDeployApp(conf, app, fileName, stageMode, appVersion):
	connect(conf["admsrv.login"], conf["admsrv.password"],conf["admsrv.url"])
	edit()
	startEdit()
	progress=deploy(app, fileName, targets=",".join(appsToServerList(app)), stageMode=stageMode, upload='true', versionIdentifier=appVersion)
	save()
	activate()
	manageProgress(progress)
	disconnect()

def actionUndeployApp(conf, app):
	connect(conf["admsrv.login"], conf["admsrv.password"],conf["admsrv.url"])
	edit()
	startEdit()
	progress=undeploy(app)
	save()
	activate()
	manageProgress(progress)
	disconnect()


def appsToServerList(apps):
	#translate apps to target servers
	servers = []
	for atemp in app.split(","):
		atarget=conf["app.%s.target" % (atemp)]
		print atemp, "->", atarget
		for target in atarget.split(","):
			if target not in servers:
				servers.append(target)
	print "Server list:", servers
	return servers

def printHelp():
	print """
Options:
 "-h", "--help"		Prints help
 "-c", "--config"	Path to config file containing basic domain info
 "-a","--action"	start, stop, deploy, undeploy
 "-s","--server"	target managed server name (start, stop)
 "--app"		target app name (start, stop, deploy, undeploy)
 "-f", "--file"		Path to Java EE application to be deployed
 "--stage"		Staging mode ("stage","nostage","external_stage") default "stage"
 "--appVersion"		versionIdentifier for Java EE application to be deployed
"""

#-----------------

configFile=""
action=""
app=""
fileName=""
serverList=""
stageMode="stage"
appVersion=""

conf = Properties()
	
try:
	opts, args = getopt.getopt(sys.argv[1:],"hc:a:s:f:",["help","config=","action=","server=","app=","file=","stage=","appVersion="])
	print "o", opts
except getopt.GetoptError:
	print 'Error - wrong option'
	printHelp()
	sys.exit(2)

for opt, arg in opts:
	print "*",opt,arg
	if opt in ("-h", "--help"):
		printHelp()
		sys.exit()
	elif opt in ("-c", "--config"):
		configFile = arg
	elif opt in ("-a","--action"):
		action = arg
	elif opt in ("-s","--server"):
		serverList = arg
	elif opt in ("--app"):
		app = arg
	elif opt in ("-f", "--file"):
		fileName = arg
	elif opt in ("--stage"):
		if arg not in ("stage","nostage","external_stage"):
			print 'ERROR - "--stage" must be in one of ["stage","nostage","external_stage"]'
			sys.exit(2)
		stageMode = arg
	elif opt in ("--appVersion"):
		appVersion = arg
		
if configFile<>"":
	print "Loading [%s]..." % (configFile)
	conf.load(FileInputStream(configFile))
	print "Done."
else:
	print 'ERROR - "--config" is required'
	printHelp()
	sys.exit(2)

if action=="start":
	if serverList<>"":
		actionStartServer(conf, serverList.split(","))
	elif app<>"":
		actionStartServer(conf, appsToServerList(app))
	else:
		print 'ERROR: action "start" requires either "--server" or "--app"'
		sys.exit(2)
elif action=="stop":
	if serverList<>"":
		actionStopServer(conf, serverList.split(","))
	elif app<>"":
		actionStopServer(conf, appsToServerList(app))
	else:
		print 'ERROR: action "start" requires either "--server" or "--app"'
		sys.exit(2)
elif action=="deploy":
	if file<>"" and app<>"":
		actionDeployApp(conf, app, fileName, stageMode, appVersion)
	else:
		print 'ERROR: action "deploy" requires "--file" and "--app"'
		sys.exit(2)
elif action=="undeploy":
	if app<>"":
		actionUndeployApp(conf, app)
	else:
		print 'ERROR: action "undeploy" requires "--app"'
		sys.exit(2)
else:
	print "Unknows action"
	sys.exit(2)



