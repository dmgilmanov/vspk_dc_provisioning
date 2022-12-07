### VSD access data

vsd_api_url = 'https://localhost:8443'
vsd_api_username = 'USERNAME'
vsd_api_password = 'PASSWORD'
vsd_api_csp = 'csp'

### Infrastructure data
wbx_model = "NUAGE_210_WBX_32_Q"                                ### could also be NUAGE_210_WBX_48_S
leaf_data = {
    '172.16.1.10': 'leaf01.lab.local',
    '172.16.1.11': 'leaf02.lab.local'
}

### VSD CBIS L2 domain variables
cbis_enterprise_name = 'CBIS-Infrastructure-Enterprise'
cbis_enterprise_profile_name = 'Default Profile'
l2_domain_template_name = 'L2 Domain Template'