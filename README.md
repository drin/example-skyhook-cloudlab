This is a *repository-based* Cloudlab profile for https://github.com/drin/decl-mercantile.
Hopefully, this makes the profile a bit easier to track and version, for potential future
convenience.

This profile is forked from https://github.com/lbstoller/my-profile.
The Cloudlab profile that is based on the original repository can be found at
https://www.cloudlab.us/p/PortalProfiles/RepoBased.

### Notes

* Contains a file called `profile.py` (a geni-lib script) in the top level directory,
  which is used to define the cluster topology.

* An experiment may be instantiated from any branch (HEAD) or tag in this repository;
  Cloudlab maintains a cache of your branches and tags and lets you select one when you
  start your experiment. See below for how to update CloudLab's cache.

* When this profile instantiates an experiment, this repository is cloned to each node, in
  the directory, `/local/repository`, which will be checked out as the branch (or tag) that
  is instantiated.

* *Execute* services run **after** the nodes have cloned the repository, so the directory,
  `/local/repository`, may be referenced from a service.

### Sync cloudlab profile

**Manually**. After updating the repository, return to the Cloudlab web interface. On the
`Edit Profile` page, click the **Update** button and Cloudlab will pull from your repository,
update the list of branches and tags, and update the source code on the page if it has changed. 

**Push Webhook**. With a [push webhook](https://developer.github.com/webhooks/), each commit
will notify Cloudlab to fetch the repository and update the profile. This will reflect the
current HEAD of the master branch, although branches and tags are updated as well. When
complete, cloudlab will send an email confirmation.

At the moment, each node will not automatically update its clone of the repository.
