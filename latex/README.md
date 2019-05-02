# latex-container

Source files for a Docker container providing Latex and pdflatex, including several latex packages I find useful for several projects.

## Contents

The container uses an Ubuntu 16.04 base and installs texlive from a PPA which provides the latest texlive (at the time of creation apt sources provided texlive 2017 which results in some trouble down the road with tex repositories).

See the *setup.sh* file for a list of included LaTeX packages.

## Usage

The container's entrypoint is set to **pdflatex** and its working directory */io* is exposed as a volume. Input files should be placed in */io* and the output files will be placed there as well. As an example, to generate a pdf from **/path/to/test.tex**, run
``` bash
docker run --rm --name pdflatex -v /path/to:/io kimvanwyk/latex test.tex
```
The output file will be placed in **/path/to**.

For ease of use, the included script *run_pdflatex.sh* will execute pdflatex for a supplied path and place the produced file into the same path. The **realpath** command is required to use it. The same example using the script:
``` bash
./run_pdflatex.sh /path/to/test.tex
```
The output file will again be placed in **/path/to**.

To run a different texlive tool, override the entrypoint. For e.g. to run **lualatex**:
``` bash
docker run --rm --entrypoint "lualatex" --name lualatex -v /path/to:/io kimvanwyk/latex test.tex
```

## Building

The *build.sh* file builds the container, naming it **kimvanwyk/latex** to remain consistent with DockerHub.

## DockerHub
The container is published on DockerHub here: [https://hub.docker.com/r/kimvanwyk/latex/](https://hub.docker.com/r/kimvanwyk/latex/).
