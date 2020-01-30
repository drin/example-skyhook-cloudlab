"""
When this profile is instantiated, the repository is cloned to `/local/repository` on all of the experiment nodes.

Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""

# The Portal object and ProtoGENI library.
from geni.portal import portal
from geni.rspec import pg

# Create a portal context, create a request object, and add a raw PC to the request
portal_context = portal.Context()
request_rspec  = portal_context.makeRequestRSpec()

# Provision client0 (ceph client) hardware
client0 = request_rspec.RawPC("node")
client0.hardware_type = 'c220g5'
client0.disk_image    = 'urn:publicid:IDN+emulab.net+image+emulab-ops//CENTOS7-64-STD'


# Provision osd0 (ceph OSD) hardware
osd0 = request_rspec.RawPC("node")
osd0.hardware_type = 'c220g5'
osd0.disk_image    = 'urn:publicid:IDN+emulab.net+image+emulab-ops//CENTOS7-64-STD'

# Add services
# client0.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))
# osd0.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))

# Add client0 and osd0 to the same LAN (create a link between them)
cluster_lan = request_rspec.Link(members=(client0, osd0))

# Print the RSpec to the enclosing page.
portal_context.printRequestRSpec(request_rspec)

"""
Skyhook cloudlab profile: CentOS 7, 1 OSD
(See https://github.com/uccross/skyhookdm-ceph/wiki/Ceph-SkyhookDM-cluster-setup#use-one-of-our-cloudlab-profiles)
<rspec xmlns="http://www.geni.net/resources/rspec/3"
       xmlns:emulab="http://www.protogeni.net/resources/rspec/ext/emulab/1"
       xmlns:tour="http://www.protogeni.net/resources/rspec/ext/apt-tour/1"
       xmlns:jacks="http://www.protogeni.net/resources/rspec/ext/jacks/1"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.geni.net/resources/rspec/3    http://www.geni.net/resources/rspec/3/request.xsd"
       type="request">

  <node xmlns="http://www.geni.net/resources/rspec/3" client_id="client0">
    <icon xmlns="http://www.protogeni.net/resources/rspec/ext/jacks/1"
          url="https://www.emulab.net/protogeni/jacks-stable/images/server.svg"/>

    <site xmlns="http://www.protogeni.net/resources/rspec/ext/jacks/1" id="Site 1"/>

    <sliver_type xmlns="http://www.geni.net/resources/rspec/3" name="raw-pc">
      <disk_image xmlns="http://www.geni.net/resources/rspec/3"
                  name="urn:publicid:IDN+emulab.net+image+emulab-ops//CENTOS7-64-STD"/>
    </sliver_type>

    <hardware_type xmlns="http://www.geni.net/resources/rspec/3" name="c220g5"/>

    <services xmlns="http://www.geni.net/resources/rspec/3"/>
    <interface xmlns="http://www.geni.net/resources/rspec/3" client_id="interface-2"/>
  </node>
  
  <node xmlns="http://www.geni.net/resources/rspec/3" client_id="osd0">
    <icon xmlns="http://www.protogeni.net/resources/rspec/ext/jacks/1"
          url="https://www.emulab.net/protogeni/jacks-stable/images/server.svg"/>

    <site xmlns="http://www.protogeni.net/resources/rspec/ext/jacks/1" id="Site 1"/>
    <sliver_type xmlns="http://www.geni.net/resources/rspec/3" name="raw-pc">
      <disk_image xmlns="http://www.geni.net/resources/rspec/3"
                  name="urn:publicid:IDN+emulab.net+image+emulab-ops//CENTOS7-64-STD"/>
    </sliver_type>
    <hardware_type xmlns="http://www.geni.net/resources/rspec/3" name="c220g5"/>
    <services xmlns="http://www.geni.net/resources/rspec/3"/>
    <interface xmlns="http://www.geni.net/resources/rspec/3" client_id="interface-1"/>
  </node>

  <link xmlns="http://www.geni.net/resources/rspec/3" client_id="link-0">
    <interface_ref xmlns="http://www.geni.net/resources/rspec/3" client_id="interface-1"/>
    <interface_ref xmlns="http://www.geni.net/resources/rspec/3" client_id="interface-2"/>
    <site xmlns="http://www.protogeni.net/resources/rspec/ext/jacks/1" id="undefined"/>
  </link>

  <rspec_tour xmlns="http://www.protogeni.net/resources/rspec/ext/apt-tour/1">
    <description type="markdown">c220g5-01osds-centos7</description>
</rspec_tour>

</rspec>
"""
