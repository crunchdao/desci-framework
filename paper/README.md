# inara

Tools to create JOSS/JOSE publishing artifacts.

The package is designed to be usable either via its Makefile, or
through a Docker image.

Generated output formats are HTML, PDF, JATS, and Crossref XML.

## Usage via Docker

The directory of the paper, or one of its parent directories,
must be mounted on path `/data`. The path to the paper, relative to
the mounted folder, is expected as the only argument.

- The Docker image will generate PDF and JATS files by default. To
select specific output formats to be generated use the `-o` flag.
Supported options are: `pdf`, `jats`, `html`, and `crossref`. To get multiple outputs
use a comma separated list.
- By default PDF files will be compiled in _draft mode_ to include a draft
watermark and linenumbers. To create a _production_ PDF add the `-p` flag.

**Example:**

    docker run --rm -it \
        -v $PWD:/data \
        -u $(id -u):$(id -g) \
        openjournals/inara \
        -o pdf,crossref \
        path/relative/to/current/directory/paper.md

The resulting PDF and Crossref-XML files will be named `paper.pdf` and `paper.crossref` and placed next to the
input file.

## Usage via make

The `make` command should be run from the project's root directory.
It expects the article source to be passed via the `ARTICLE`
variable. So if the paper Markdown source is in file
`/my/path/paper.md`, then make should be called with

    make ARTICLE=/my/path/paper.md

All supported publishing formats are generated by default, but you
can select a specific format to be generated by passing it as an
argument. Available options: `html`, `pdf`, `jats`, and `crossref`.

E.g., to generate only a PDF file, the command would be

    make pdf ARTICLE=/my/path/paper.md

The generated output will be written to folder
`publishing-artifacts`.