from vspk import v5_0 as vspk
from wbx_data import *
from vsd_data import *
import logging

#Start REST API session towards to VSD
def start_csproot_session():
    session = vspk.NUVSDSession(
        api_url=vsd_api_url,
        username=vsd_api_username,
        password=vsd_api_password,
        enterprise=vsd_api_csp)
    try:
        session.start()
    except:
        logging.error("Unable to start the session")
    return session.user

csproot = start_csproot_session()

def create_cbis_enterprise():
    csproot = start_csproot_session()
    csproot.create_child(vspk.NUEnterprise(
        name=cbis_enterprise_name,
        enterprise_profile_id=csproot.enterprise_profiles.get(filter='name == "{}"'.format(cbis_enterprise_profile_name))[0].id
        ))

def create_leafs():
    csproot = start_csproot_session()
    for leaf_system_ip, leaf_hostname in leaf_data.items():
        if (len(csproot.gateways.get(filter='name == "{}"'.format(leaf_system_ip))) != 0 and    
        len(csproot.gateways.get(filter='name == "{}"'.format(leaf_hostname))) == 0):
            gateway = csproot.gateways.get(filter='name == "{}"'.format(leaf_system_ip))[0]
            if gateway.pending == True: gateway.pending = False
            gateway.save()
            gateway = csproot.gateways.get(filter='name == "{}"'.format(leaf_system_ip))[0]
            gateway.name = leaf_hostname
            gateway.save()
        else:
            if len(csproot.gateway_templates.get(filter='name == "{}"'.format('wbx_template'))) == 0:
                new_wbx_template = vspk.NUGatewayTemplate(
                name='wbx_template',
                personality=wbx_model
                )
                csproot.create_child(new_wbx_template)
            else:
                new_wbx_template = csproot.gateway_templates.get(filter='name == "{}"'.format('wbx_template'))[0]
            new_gateway = vspk.NUGateway(
                name=leaf_hostname,
                system_id=leaf_system_ip,
                template_id=new_wbx_template.id
                )
            csproot.create_child(new_gateway)
    
def create_l2_domains():
    cbis_enterprise = csproot.enterprises.get(filter='name == "{}"'.format(cbis_enterprise_name))[0]
    new_l2_domain_template = vspk.NUL2DomainTemplate(name=l2_domain_template_name)
    cbis_enterprise.create_child(new_l2_domain_template)
    new_l2_domain_template.create_child(vspk.NUEgressACLTemplate(
        name="Egress",
        active=True,
        default_allow_ip=True, 
        default_allow_non_ip=True, 
        default_install_acl_implicit_rules=True
        ))
    new_l2_domain_template.create_child(vspk.NUIngressACLTemplate(
        name="Ingress",
        active=True,
        default_allow_ip=True, 
        default_allow_non_ip=True,
        allow_address_spoof=True
        ))

create_l2_domains()
