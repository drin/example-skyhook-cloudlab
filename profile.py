"""
When this profile is instantiated, the repository is cloned to `/local/repository` on all of the experiment nodes.

Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""

# The Portal object and ProtoGENI library.
import geni.portal as portal
import geni.rspec.pg as pg

# Create a portal context, create a request object, and add a raw PC to the request
portal_context = portal.Context()
request_rspec  = portal_context.makeRequestRSpec()

# Provision client0 (ceph client) hardware
client0 = request_rspec.RawPC("node")
client0.hardware_type = 'c220g5'
client0.disk_image    = 'urn:publicid:IDN+emulab.net+image+emulab-ops//CENTOS7-64-STD'
client_interface      = client0.addInterface('interface-client')


# Provision osd0 (ceph OSD) hardware
osd0 = request_rspec.RawPC("node")
osd0.hardware_type = 'c220g5'
osd0.disk_image    = 'urn:publicid:IDN+emulab.net+image+emulab-ops//CENTOS7-64-STD'
osd_interface      = osd0.addInterface('interface-osd')

# Add services
# client0.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))
# osd0.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))

# Add client0 and osd0 to the same LAN (create a link between them)
cluster_lan = request_rspec.LAN('lan')
cluster_lan.addInterface(client_interface)
cluster_lan.addInterface(osd_interface)

# Print the RSpec to the enclosing page.
portal_context.printRequestRSpec(request_rspec)
