import re


def modified_for_chassis_read_doc (file_name):
	doc = []
	for line in open(file_name, 'r').readlines():
		if "PID" in line:
			line = "  "+ line
		doc.append(line)
	return doc

def strip_duke_energy_com(line):
	start_of_duke = re.search("[.][dD][uU][kK][eE]?[-]?[eE]?[nN]?[eE]?[rR]?[gG]?[yY]?[.]?[cC]?[oO]?[mM]?", line)
	
	if start_of_duke == None:
		return (line)
	else:
		temp_name = line[:start_of_duke.start()]
		return temp_name

#def find_SFP_type(interface,show_int_stat_file):


def split_interface(interface):
	num_index = interface.index(next(x for x in interface if x.isdigit()))
	str_part = interface[:num_index]
	num_part = interface[num_index:]
	return [str_part,num_part]

def normalize_interface_names(non_norm_int):
	tmp = split_interface(non_norm_int)
	interface_type = tmp[0]
	port = tmp[1]
	for int_types in interfaces:
		for names in int_types:
			for name in names:
				if interface_type in name:
					return_this = int_types[1]+port
					return return_this
	return "normalize_interface_names Failed"
			
sfps = [

	[["1000BaseSX"],"GLC-SX-MMD"],
	[["1000BaseLX"],"GLC-LH-SMD"],
	[["10/100BaseTX","10/100/1000-TX"],"GLC-T"],
	[[1],"GLC-GE-100FX"],
	[[1],"SFP-10G-SR"],
	[[1],"SFP-10G-LR"],
]

interfaces = [
	[["Ethernet","Eth"],"Eth"],
	[["FastEthernet"," FastEthernet","Fa","interface FastEthernet","FastEthernet"],"Fa"],
	[["GigabitEthernet","Gi"," GigabitEthernet","interface GigabitEthernet"],"Gi"],
	[["TenGigabitEthernet","Te"],"Te"],
	[["Port-channel","Po"],"Po"],
	[["Serial"],"Ser"],
	[["Vlan","interface Vlan"],"Vlan"],
	[["Port","Port ",],"Port"]
]
