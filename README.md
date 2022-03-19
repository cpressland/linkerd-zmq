# linkerd-zmq

Used to help inform differences between Linkerd Viz Dashboard and Buoyant Cloud for Non-HTTP/HTTPS/gRPC traffic.

Most of the code copied from [here](https://zeromq.org/languages/python/) with a few minor modifications to make it easier to run inside kube.

# Usage

- Create a Kubernetes instance locally
    - `kind create cluster`
- Install Linkerd and Linkerd Viz
    - `linkerd install | kubectl apply -f -`
    - `linkerd viz install | kubectl apply -f -`
- Install Buoyant Cloud
    - Get install command from portal
- Install Server
    - `kubectl apply -k deploy/server`
- Install Client
    - `kubectl apply -k deploy/client`

At this point, the Client should be unable to communicate with the Server due to the [Linkerd Server Resource](https://linkerd.io/2.11/reference/authorization-policy/#server) blocking requests, this should be visible on this namespaces section on the Buoyant Cloud.

- Install Authorization
    - `kubectl apply -k deploy/authorization`

The above command installs the [Linkerd Server Authorization Resource](https://linkerd.io/2.11/reference/authorization-policy/#serverauthorization) which should allow traffic to operate normally between these services.

# TODO:
* Update repo with output of differences between Linkerd Viz and Buoyant Cloud
