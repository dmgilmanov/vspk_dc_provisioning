from main_function import *

# Deploy everything from scratch
create_cbis_enterprise()
create_leafs()
create_leaf_ports()
create_leaf_vlans()
create_l2_domains()
create_vports()

# Delete everything from scratch
delete_vports()
delete_leaf_vlans()
delete_leaf_ports()