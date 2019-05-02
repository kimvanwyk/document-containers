docker run --rm --name pdflatex -v $(dirname $(realpath $1)):/io kimvanwyk/latex:1.0.0 $(basename $(realpath $1))
