---
title: RStudio Workbench Load Balancing Changes
people:
  - Melissa Barca
date: '2021-09-21'
slug: rstudio-workbench-load-balancing-changes
tags:
  - RStudio IDE
description: As we’re putting the finishing touches on the RStudio Workbench 2021.09.0 "Ghost Orchid" release, we’d like to share one of the new sets of features we’re most excited about. We’ve revisited and revamped the administration experience for load balancing clusters.
resources:
  - name: thumbnail
    src: thumbnail.jpg
    title: Thumbnail of three piles of balancing rocks against blue sky
  - name: hero
    src: image.jpg
    title: Three piles of balancing rocks against blue sky
blogcategories:
- Products and Technology
alttext: Rock towers
events: blog
image: thumbnail.jpg
ported_from: rstudio
port_status: raw
---
<sup>
Photo by <a href="https://unsplash.com/@davidclode?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText" target="_blank" rel="noopener noreferrer">David Clode</a> on <a href="https://unsplash.com/?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
</sup>

As we're putting the finishing touches on the RStudio Workbench 2021.09.0 "Ghost Orchid" release, we'd like to share one of the new sets of features we're most excited about. We've revisited and revamped the administration experience for load balancing clusters.

Specifically, we've worked to improve the cluster management and troubleshooting. To make this possible, cluster data is now stored within the internal database. The load balancing configuration file no longer requires a list of each node in the cluster. In fact, the file can be completely empty - though its presence is required. This means nodes can join and leave the cluster without bringing down and re-configuring every node - scaling your cluster has never been easier!

When provided an empty configuration file, RStudio Workbench predicts the address that other nodes can reach each node at. For more complicated configurations, we've included an escape hatch through the new `www-host-name` option which be can included in the file to instruct RStudio Workbench to use a specified hostname. A detailed explanation of the approach taken to determine each node's address and the new option can be found in the <a href="https://docs.rstudio.com/ide/server-pro/latest/load_balancing/configuration.html" target = "_blank" rel = "noopener noreferrer">Admin Guide</a>.

Furthermore, we've added several new commands to the `rstudio-server` admin tool to improve load balancing cluster management. 

The first command, `rstudio-server list-nodes` displays each node and information about its current status. It is intended to be use in conjunction with the existing status endpoint (accessed through `curl http://localhost:8787/load-balancer/status`) to monitor the status of your nodes and aid in identifying and addressing issues. 

The following is an example of this output:

```
$ sudo rstudio-server list-nodes
Cluster
-------
Protocol
Http

Nodes
-----
ID  Host           IPv4           Port  Status                     Last Seen
1   rsw-primary    172.98.8.241   80    Online                     2021-Sep-20 17:08:53
2   rsw-secondary  172.98.14.255  80    Invalid secure cookie key  2021-Sep-20 17:10:25
3   rsw-tertiary   172.98.6.205   80    Offline                    2021-Sep-20 17:10:34
```

Because load balancing now makes use of the internal database, each node validates its secure cookie key and configured protocol against the database before coming online. The first node online sets the values used for validation. The results of that validation are stored in the database and easily retrievable through the `rstudio-server list-nodes` command, allowing for easy troubleshooting when encountering unexpected issues with your cluster.

We've added the command `rstudio-server reset-cluster` to reset the cluster's state used for validation. This should be run after replacing the secure cookie key on each node or after updating the protocol the cluster is using (`http`, `https`, or `https-no-verify`). Again, the first node brought online or restarted after this reset will determine the configuration used for validation.

Finally, the command `rstudio-server delete-node <node-id>` allows you to easily remove nodes from the cluster. The required `node-id` parameter can be retrieved from the output of the `rstudio-server list-nodes` command. When a node is deleted, the other nodes in the cluster will no longer try to contact that node; there is no need to restart the active nodes after running this. This command should only be used for nodes that are offline and will not be coming back online. 

There are many more features coming with this release. If you're interested in giving them a try, check out the <a href="https://www.rstudio.com/products/rstudio/download/preview/" target = "_blank" rel = "noopener noreferrer">RStudio 2021.09.0 Preview</a> for the latest installers and release notes.
