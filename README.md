# OtktDSL-examples

This repository has submodules.
Clone it with:
```
git clone --recurse-submodules <url>
```

![Otkt logo](res/otkt_logo.svg)

## About

This repository demonstrates how to instrument and generate Kieker Analysis material for Python applications.
Here, 3 examples are given in the `apps` repository:
- helloWorld, a dummy app.
- UXsim, an open-source Python tool for simulating network traffic flow.
- AnyTree, a Python library for creating and manipulating tree data structures.

The Kieker graphs demonstrated here is the following:
- Deployment Component Dependency Graph
- Deployment Sequence Diagrams (one for each trace in a given log)
- Aggregated Deployment Call Tree

Please refer to the [Kieker userguide]{https://oceanrep.geomar.de/id/eprint/16537/79/kieker-1.14-userguide.pdf} for further instructions on how to generate other diagram types.

## Setup

### Build the collector and monitoring probe
(Already done)
```
 java -jar tools/otkt-jar-with-dependencies.jar src/demo.otkt
```

### Install the collector and monitoring probe
```
cd otkt-gen
make
cd ..
```

## Instrument
Instrument the app of your choice.
```
./tools/instrument.sh <helloWorld|UXsim|anytree>
```
And install the instrumented app.
```
pip install apps/<helloWorld|UXsim|anytree>
```

## Data collection
First, launch the collector.
```
./tools/collector.sh
```
In another terminal, launch the app of your choice.
```
python3 <helloWorld|UXsim|anytree>-test.py
```
You should now see the kieker logs collected in /tmp.
```
ll /tmp/kieker*
```
   
## Analysis
Now, run the analysis of your choice.
```
./tools/analysis <output directory> <component|sequence|calltree>
```
The diagrams generated as pdfs can be opened with the following command:
```
gio open ./bin/<output directory>/<filename>.pdf
```
