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