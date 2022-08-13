pandoc paper.md -s --mathml --data-dir=./data/  --resource-path=./figures/ --bibliography ./paper.bib  -o paper.pdf

pandoc paper.md -s --mathml --data-dir=./data/  --resource-path=./figures/ --bibliography ./paper.bib -o paper.html
