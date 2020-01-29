"""
When this profile is instantiated, the repository is cloned to `/local/repository` on all of the experiment nodes.

Instructions:
Wait for the profile instance to start, then click on the node in the topology and choose the `shell` menu item. 
"""

# The Portal object and ProtoGENI library.
import geni.portal as portal
import geni.rspec.pg as pg

# Create a portal context, create a request object, and add a raw PC to the request
pc      = portal.Context()
request = pc.makeRequestRSpec()
node    = request.RawPC("node")

# Install and execute a script that is contained in the repository.
node.addService(pg.Execute(shell="sh", command="/local/repository/silly.sh"))

# Print the RSpec to the enclosing page.
pc.printRequestRSpec(request)
