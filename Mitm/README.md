This is the Readme for mitm
### Development
Firstly I need to create the networks for the containers. An external network connecting 
to the outside internet and internal for only the containers to access

This command creates the internal network only accessabible by the containers
```docker network create --driver=bridge --subnet=10.0.0.0/24 internal```
This command creates the external network where we will forward packets destined outside the internal network
``docker network create --driver=bridge --subnet=10.0.1.0/24 external```

