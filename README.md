# Normalize-Cisco-interface-names

Just feed "normalize_interface_names()" a non normalized port name "normalize_interface_names(non_norm_int)" and it will spit out a normalized for port name.

One of the main issues I have run into has been that Cisco calls interfaces different things all over the freaking place. Such as Gi vs GigabitEthernet. Making it very difficult to match up info from different commands about the same interface.  For those that are interested these will normalize your interface names without regex so it's easy for anyone to update it incase there is some way the router referes to an interface that that a normal regex would miss. It's probably not how is probably should be done, but this makes it super easy to update when Cisco decides to change what it's standard is this week. Just feed "normalize_interface_names" your interface name and it will spit out a normalized interface name for you, if it fails it will spit out "normalize_interface_names Failed". It's fairly easy, for example a FA port, it runs though the list and if anything matches it returns "Fa" (The string outside the list)
["FastEthernet"," FastEthernet","Fa","interface FastEthernet"],"Fa"].

