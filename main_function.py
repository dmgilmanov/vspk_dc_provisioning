from vspk import v5_0 as vspk
from port_layout import *
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

def delete_cbis_enterprise():
    csproot = start_csproot_session()
    cbis_infra_enterprise = csproot.enterprises.get(filter='name == "{}"'.format(cbis_enterprise_name))[0]
    cbis_infra_enterprise.delete()

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

def delete_leafs():
    csproot = start_csproot_session()
    for leaf_system_ip, leaf_hostname in leaf_data.items():
        leaf = csproot.gateways.get(filter='name == "{}"'.format(leaf_hostname))[0]
        leaf.delete()
    if len(csproot.gateway_templates.get(filter='name == "{}"'.format('wbx_template'))) != 0:
        wbx_template = csproot.gateway_templates.get(filter='name == "{}"'.format('wbx_template'))[0]
        wbx_template.delete()

def create_leaf_ports():
    csproot = start_csproot_session()
    for leaf_system_ip, leaf_hostname in leaf_data.items():
        leaf = csproot.gateways.get(filter='name == "{}"'.format(leaf_hostname))[0]
        for port_name, port_data in port_layout.items():
            new_port = vspk.NUPort(
                vlan_range=port_vlan_range,
                name=port_name,
                physical_name=port_name,
                port_type='ACCESS'
            )
            leaf.create_child(new_port)

def delete_leaf_ports():
    csproot = start_csproot_session()
    for leaf_system_ip, leaf_hostname in leaf_data.items():
        leaf = csproot.gateways.get(filter='name == "{}"'.format(leaf_hostname))[0]
        for leaf_port in leaf.ports.get():
            if leaf_port.port_type == 'ACCESS':
                leaf_port.delete()

def create_leaf_vlans():
    csproot = start_csproot_session()
    cbis_enterprise_id = csproot.enterprises.get(filter='name == "{}"'.format(cbis_enterprise_name))[0].id
    for leaf_system_ip, leaf_hostname in leaf_data.items():
        leaf = csproot.gateways.get(filter='name == "{}"'.format(leaf_hostname))[0]
        for port_name, port_data in port_layout.items():
            port = leaf.ports.get(filter='name == "{}"'.format(port_name))[0]
            for vlan_value, vlan_description in port_data['vlans'].items():
                new_vlan = vspk.NUVLAN(
                    value=vlan_value,
                    description=vlan_description
                    )
                port.create_child(new_vlan)
                new_permission = vspk.NUEnterprisePermission(
                    permitted_entity_id=cbis_enterprise_id,
                    permitted_action='USE'
                    )
                new_vlan.create_child(new_permission)

def delete_leaf_vlans():
    csproot = start_csproot_session()
    for leaf_system_ips, leaf_hostname in leaf_data.items():
        leaf = csproot.gateways.get(filter='name == "{}"'.format(leaf_hostname))[0]
        for port in leaf.ports.get():
            if port.port_type == 'ACCESS':
                for vlan in port.vlans.get():
                    vlan.delete()

def create_l2_domains():
    csproot = start_csproot_session()

    cbis_enterprise = csproot.enterprises.get(filter='name == "{}"'.format(cbis_enterprise_name))[0]
    new_l2_domain_template = vspk.NUL2DomainTemplate(name="L2_domain")
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

    l2_domains_to_create = []
    for port_name, port_data in port_layout.items():
        for vlan_value, vlan_description in port_data['vlans'].items():
            if vlan_description not in l2_domains_to_create:
                l2_domains_to_create.append(vlan_description)
    for new_l2_domain_name in l2_domains_to_create:
        new_l2_domain=vspk.NUL2Domain(
            name=new_l2_domain_name,
            template_id=new_l2_domain_template.id
        )
        cbis_enterprise.create_child(new_l2_domain)
def delete_l2_domains():
    csproot = start_csproot_session()
    cbis_enterprise = csproot.enterprises.get(filter='name == "{}"'.format(cbis_enterprise_name))[0]
    for l2_domain in cbis_enterprise.l2_domains.get():
        l2_domain.delete()
    l2_domain_template = cbis_enterprise.l2_domain_templates.get(filter='name == "{}"'.format('L2_domain'))[0]
    l2_domain_template.delete()

def create_vports():
    csproot = start_csproot_session()
    cbis_enterprise = csproot.enterprises.get(filter='name == "{}"'.format(cbis_enterprise_name))[0]
    for leaf_system_ip, leaf_hostname in leaf_data.items():
        gateway = csproot.gateways.get(filter='name == "{}"'.format(leaf_hostname))[0]
        for port in gateway.ports.get():
            for vlan in port.vlans.get():
                if len(cbis_enterprise.l2_domains.get(filter='name == "{}"'.format(vlan.description))) != 0:
                    l2_domain = cbis_enterprise.l2_domains.get(filter='name == "{}"'.format(vlan.description))[0]
                    new_vport=vspk.NUVPort(
                        name=gateway.name + ' ' + port.name.replace('/','-') + ' ' + str(vlan.value),
                        type="BRIDGE",
                        address_spoofing="ENABLED",
                        vlanid=vlan.id,
                        has_attached_interfaces=True            
                    )
                    l2_domain.create_child(new_vport)
                    new_bridge_interface = vspk.NUBridgeInterface(
                        name=gateway.name + ' ' + port.name.replace('/','-') + ' ' + str(vlan.value)
                    )
                    new_vport.create_child(new_bridge_interface)

def delete_vports():
    csproot = start_csproot_session()
    cbis_infra_enterprise = csproot.enterprises.get(filter='name == "{}"'.format(cbis_enterprise_name))[0]
    for l2_domain in cbis_infra_enterprise.l2_domains.get():
        for vport in l2_domain.vports.get():
            for bridge_interface in vport.bridge_interfaces.get():
                bridge_interface.delete()
            vport.delete()