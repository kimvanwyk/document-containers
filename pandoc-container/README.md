# pandoc-container

Source files for a Docker container providing pandoc, built on top of [my latex container](https://github.com/kimvanwyk/latex-container) to include several latex packages I find useful for various projects.

## Usage

The container's entrypoint is set to **pandoc** and its working directory */io* is exposed as a volume. Input files should be placed in */io*. Output files will be placed there as well. As an example, to generate a pdf from **/path/to/test.md**, run
``` bash
docker run --rm --name pandoc -v -v /path/to:/io kimvanwyk/pandoc:1.0.0 -o test.pdf test.md
```
The output file will be placed in **/path/to**.

For ease of use, the included script *run_pandoc.py* will execute pandoc for a supplied path and place the produced file into the same path. Python 3 is required to use it. The same example using the script:
``` bash
./run_pandoc.py /path/to/test.tex test.pdf
```
The output file will again be placed in **/path/to**.

## Building

The *build.sh* file builds the container, naming it **kimvanwyk/pandoc** to remain consistent with DockerHub.

## DockerHub
The container is published on DockerHub here: [https://hub.docker.com/r/kimvanwyk/pandoc/](https://hub.docker.com/r/kimvanwyk/pandoc/).
