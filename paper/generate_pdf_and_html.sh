pandoc example/paper.md -s --mathml --data-dir=./data/  --resource-path=./example/ --bibliography ./example/paper.bib  -o example/paper.pdf

pandoc example/paper.md -s --mathml --data-dir=./data/  --resource-path=./example/ --bibliography ./example/paper.bib -o example/paper.html
