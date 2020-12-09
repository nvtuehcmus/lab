from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="10.215.26.170",
    port=830,
    username="admin",
    password="vnpro@149",
    hostkey_verify=False
    )
"""
print("#Supported Capabilities (YANG models):")
for capability in m.server_capabilities:
    print(capability)
"""
"""
netconf_reply = m.get_config(source="running")
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
"""
'''
#Truy xuat mot phan cau hinh
netconf_filter = """
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native" />
</filter>
"""
netconf_reply = m.get_config(source="running", filter=netconf_filter)

print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
'''

#'''
#Cau hinh hostname thiet bi CSR
netconf_hostname = """
<config>
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
     <hostname>csr1000v-abc</hostname>
  </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())


'''
#Tao loopback
netconf_loopback = """
<config>
 <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
  <interface>
   <Loopback>
    <name>1</name>
    <description>[Student Name]\'s loopback</description>
    <ip>
     <address>
      <primary>
       <address>172.10.20.1</address>
       <mask>255.255.255.0</mask>
      </primary>
     </address>
    </ip>
   </Loopback>
  </interface>
 </native>
</config>
"""
netconf_reply = m.edit_config(target="running", config=netconf_loopback)
print(xml.dom.minidom.parseString(netconf_reply.xml).toprettyxml())
'''
