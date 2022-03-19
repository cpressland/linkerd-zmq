# linkerd-zmq

Most of the code copied from [here](https://zeromq.org/languages/python/) with a few minor modifications. Intention is to deploy to Kubernetes cluster to help diagnose why Linkerd Viz seems unable to _see_ traffic between one of our other zmq applications

# Usage

- Create a Kubernetes instance Locally
    - `kind create cluster`
- Install Linkerd and Linkerd Viz
    - `linkerd install | kubectl apply -f -`
    - `linkerd viz install | kubectl apply -f -`
