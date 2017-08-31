
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
