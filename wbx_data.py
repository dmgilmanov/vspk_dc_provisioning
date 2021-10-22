wbx_model = "NUAGE_210_WBX_32_Q"                                ### could also be NUAGE_210_WBX_48_S
leaf_data = {
    '10.43.16.0': 'hel-labra2-ds511',
    '10.43.16.1': 'hel-labra2-ds512'
}
### Port data
port_vlan_range = '0,512-4094'                                  ### default range for CBIS deployments                                 
port_layout = {
    '1/1/17': {
        'description': 'Compute-6 (U25)',
        'vlans': {
            '0': 'Provisioning',
            '513': 'Internal_API',
            '514': 'Storage',
            '515': 'Storage_Management'
        }
    },
    '1/1/18': {
        'description': 'Compute-6 (U25)',
        'vlans': {
            '0': 'Provisioning',
			'516': 'Tenant_VXLAN'
        }
    },
    '1/1/19': {
        'description': 'Compute-7 (U26)',
        'vlans': {
            '0': 'Provisioning',
            '513': 'Internal_API',
            '514': 'Storage',
            '515': 'Storage_Management'
        }
    },
    '1/1/20': {
        'description': 'Compute-7 (U26)',
        'vlans': {
            '0': 'Provisioning',
			'516': 'Tenant_VXLAN'
        }
    },
    '1/1/21': {
        'description': 'Controller-1 (U18)',
        'vlans': {
            '0': 'Provisioning',
            '512': 'External',
            '513': 'Internal_API',
            '514': 'Storage',
            '515': 'Storage_Management',
        }
    },
    '1/1/22': {
        'description': 'Controller-1 (U18)',
        'vlans': {
            '0': 'Provisioning',
            '516': 'Tenant_VXLAN',
        }
    },
    '1/1/23': {
        'description': 'Controller-2 (U17)',
        'vlans': {
            '0': 'Provisioning',
            '512': 'External',
            '513': 'Internal_API',
            '514': 'Storage',
            '515': 'Storage_Management',
        }
    },
    '1/1/24': {
        'description': 'Controller-2 (U17)',
        'vlans': {
            '0': 'Provisioning',
            '516': 'Tenant_VXLAN',
        }
    },
    '1/1/25': {
        'description': 'Compute-8 (U27)',
        'vlans': {
            '0': 'Provisioning',
            '513': 'Internal_API',
            '514': 'Storage',
            '515': 'Storage_Management'
        }
    },
    '1/1/26': {
        'description': 'Compute-8 (U27)',
        'vlans': {
            '0': 'Provisioning',
			'516': 'Tenant_VXLAN'
        }
    },
    '1/1/27': {
        'description': 'Compute-9 (U28)',
        'vlans': {
            '0': 'Provisioning',
            '513': 'Internal_API',
            '514': 'Storage',
            '515': 'Storage_Management'
        }
    },
    '1/1/28': {
        'description': 'Compute-9 (U28)',
        'vlans': {
            '0': 'Provisioning',
			'516': 'Tenant_VXLAN'
        }
    },
    '1/1/29': {
        'description': 'Controller-3 (U16)',
        'vlans': {
            '0': 'Provisioning',
            '512': 'External',
            '513': 'Internal_API',
            '514': 'Storage',
            '515': 'Storage_Management',
        }
    },
    '1/1/30': {
        'description': 'Controller-3 (U16)',
        'vlans': {
            '0': 'Provisioning',
            '516': 'Tenant_VXLAN',
        }
    },
    '1/1/31': {
        'description': 'Undercloud Server (U15)',
        'vlans': {
            '0': 'Provisioning',
            '512': 'External'
        }
    },
    '1/1/32': {
        'description': 'Undercloud Server (U15)',
        'vlans': {
            '0': 'Provisioning',
        }
    },
    '1/1/33': {
        'description': 'Compute-10 (U29)',
        'vlans': {
            '0': 'Provisioning',
            '513': 'Internal_API',
            '514': 'Storage',
            '515': 'Storage_Management'
        }
    },
    '1/1/34': {
        'description': 'Compute-10 (U29)',
        'vlans': {
            '0': 'Provisioning',
			'516': 'Tenant_VXLAN'
        }
    },
    '1/1/37': {
        'description': 'Compute-1 (U14)',
        'vlans': {
            '0': 'Provisioning',
            '513': 'Internal_API',
            '514': 'Storage',
            '515': 'Storage_Management'
        }
    },
    '1/1/38': {
        'description': 'Compute-1 (U14)',
        'vlans': {
            '0': 'Provisioning',
			'516': 'Tenant_VXLAN'
        }
    },
    '1/1/39': {
        'description': 'Compute-2 (U13)',
        'vlans': {
            '0': 'Provisioning',
            '513': 'Internal_API',
            '514': 'Storage',
            '515': 'Storage_Management'
        }
    },
    '1/1/40': {
        'description': 'Compute-2 (U13)',
        'vlans': {
            '0': 'Provisioning',
			'516': 'Tenant_VXLAN'
        }
    },
    '1/1/45': {
        'description': 'Compute-3 (U12)',
        'vlans': {
            '0': 'Provisioning',
            '513': 'Internal_API',
            '514': 'Storage',
            '515': 'Storage_Management'
        }
    },
    '1/1/46': {
        'description': 'Compute-3 (U12)',
        'vlans': {
            '0': 'Provisioning',
			'516': 'Tenant_VXLAN'
        }
    },
    '1/1/47': {
        'description': 'Compute-4 (U11)',
        'vlans': {
            '0': 'Provisioning',
            '513': 'Internal_API',
            '514': 'Storage',
            '515': 'Storage_Management'
        }
    },
    '1/1/48': {
        'description': 'Compute-4 (U11)',
        'vlans': {
            '0': 'Provisioning',
			'516': 'Tenant_VXLAN'
        }
    },
    '1/1/53': {
        'description': 'Compute-5 (U10)',
        'vlans': {
            '0': 'Provisioning',
            '513': 'Internal_API',
            '514': 'Storage',
            '515': 'Storage_Management'
        }
    },
    '1/1/54': {
        'description': 'Compute-5 (U10)',
        'vlans': {
            '0': 'Provisioning',
			'516': 'Tenant_VXLAN'
        }
    },
    '1/2/7': {
        'description': 'Storage-1 (U5-U6)',
        'vlans': {
            '0': 'Provisioning',
            '514': 'Storage',
            '515': 'Storage_Management'
        }
    },
    '1/2/15': {
        'description': 'Storage-2 (U3-U4)',
        'vlans': {
            '0': 'Provisioning',
            '514': 'Storage',
            '515': 'Storage_Management'
        }
    },
    '1/2/23': {
        'description': 'Storage-3 (U2-U1)',
        'vlans': {
            '0': 'Provisioning',
            '514': 'Storage',
            '515': 'Storage_Management'
        }
    }
}
