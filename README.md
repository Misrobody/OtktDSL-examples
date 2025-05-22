# OtktDSL-examples

This repository has submodules.
Either clone it with:
```
git clone --recurse-submodules <url>
```
Or run:
```
git submodule update --remote --recursive
```

## About

This repository demonstrates how to instrument and generate Kieker Analysis material for Python applications.
Here, 5 examples are given in the `apps` repository:
- helloWorld, a dummy app designed to generate simple diagrams.
- UXsim, an open-source Python tool for simulating network traffic flow.
- Potnia, converts Romanized transliterations into native Unicode scripts.
- AnyTree, a Python library for creating and manipulating tree data structures.
- AixWeather, a Python tool for generating weather data for building energy system simulations.

The Kieker generated material based of off these apps demonstrated here is the following:
- Deployment Component Dependency Graph
- Deployment Sequence Diagrams (one for each trace in a given log)
- Aggregated Deployment Call Tree

Please refer to the [Kieker userguide]{https://oceanrep.geomar.de/id/eprint/16537/79/kieker-1.14-userguide.pdf} for further instructions on how to generate other diagram types.

## Usage

 * First, launch the collector.
```
./tools/collector.sh
```

 * In another terminal, launch the app of your choice.
```
./tools/launch.sh <helloWorld|UxSim|potnia|anytree|AixWeather>
```

 * You should now see the kieker logs collected in the `bin` directory. Now, run the analysis of your choice.
```
./tools/analysis <output directory> <component|sequence|calltree>
```

 * The diagrams generated as pdfs can be opened with the following command:
```
gio open ./bin/<output directory>/<filename>.pdf
```

## Avanced Usage

If something doesn't work as intended, please try the following.

### Buiding the collector
```
cd otkt/otkt-gen/collector
mvn clean package
cd ../../..
```

## Misc.

### How to build UXsim

```
python3 -m build
pip install dist/uxsim-1.7.5.tar.gz
```

### How to build Potnia

```
poetry install
```

### How to build Anytree

```
python3 -m build
pip install dist/anytree-2.13.0+d20250505.tar.gz
```

## Author

- Daphné Larrivain <daphne.larrivain@ecole.ensicaen.fr>
