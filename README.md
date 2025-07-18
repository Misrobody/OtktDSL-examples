# OtktDSL-examples

This repository has submodules.
Clone it with:
```
git clone --recurse-submodules <url>
```

![Otkt logo](res/otkt_logo.svg)

## About

This repository demonstrates how to instrument Python applications and generate Kieker logs.
Here, 3 examples are given in the `apps` repository:
- helloWorld, a dummy app.
- UXsim, an open-source Python tool for simulating network traffic flow.
- AnyTree, a Python library for creating and manipulating tree data structures.

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
And install the instrumented app. This process varies from app to app. The following should work in most cases.
```
cd apps/<helloWorld|UXsim|anytree>
pip install . --no-build-isolation --no-compile --use-feature=fast-deps
```
Or
```
cd apps/<helloWorld|UXsim|anytree>
python3 -m build .
pip install dist/*.whl -v
cd ../..
```

## Data collection
First, launch the collector.
```
cd otkt-gen
make run
```
In another terminal, launch the app of your choice.
```
python3 <helloWorld|UXsim|anytree>-test.py
```
You should now see the kieker logs collected in /tmp.
```
ll /tmp/kieker*
```
You are now free to use these logs with any of the [Kieker tools](https://kieker-monitoring.readthedocs.io/en/latest/kieker-tools/Kieker-Tools.html)
