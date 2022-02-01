class Router:
	def __init__(self,ip,network):
		self.ip = ip
		self.network=network

	def getip(self):
		print(self.ip)
	def getname(self):
		print(self.name)
	def getnetwork(self):
		print(self.network)
	def __repr__(self):
		kvps = [f"{k} {v}" for k, v in vars(self).items()]
		return f"{type(self).__name__}({', '.join(kvps)})"

class Switch(Router):
	def __init__(self,ip,network,layer):
		Router.__init__(self,ip,network)
		self.layer=layer
		self.vlans=[]
	def addvlan(self,vlan):
		self.vlans.append(vlan)
	def getvlans(self):
		print(self.vlans)
	def getlayer(self):
		print(self.layer)
	def __repr__(self):
		kvmps = [f"{k} {v}" for k, v in vars(self).items()]
		return f"{type(self).__name__}({', '.join(kvmps)})"

routers=[]
switches=[]
while(True):
	rors = ""
	while(rors != "router" and rors!= "switch" and rors != "0"):
		rors = input("router or switch? 0 to exit: ")
	if(rors=="router"):
		routers.append(Router(input("enter ip: "),input("enter network: ")))
	elif(rors=="switch"):
		switches.append(Switch(input("enter ip: "),input("enter network: "),input("layer?: ")))
		stop="1"
		while(stop != "0"):
			stop=input("enter 1 to continue, 0 to stop adding vlans: ")
			if(stop=="0"):
				break
			switches[len(switches)-1].addvlan(int(input("add vlan: ")))
	elif(rors == "0"):
	    break
	else: print("input error")

print(switches)
print(routers)
