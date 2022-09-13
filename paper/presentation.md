---
title: ""
author: ""
date: "2022/09/09"
colorlinks: true,
subject: "Markdown"
keywords: [Markdown, Example]
lang: "en"
...

# Introduction

```python
import pandas as pd
# I will probably use this one at some point..
import xgboost as xgb

attenders = pd.read_csv("attenders.csv")

for row in attenders:
    print(f"Welcome to this DeSci webinar {row["name"]}!")
```

# Introduction

Matteo is a researcher, worked in academia, dropped out of a prestigious PhD in Aerospace Engineering because of the bad monetary incentives in academia. DeSci is trying to solve this.

Blockchain powers peer-to-peer collaboration in an efficient way.

# Structure

- Problem
- Solution
- Why DeSci in CrunchDAO?
- How to kickstart your project in 10 steps!

# Problem

Tragedy of the anticommons: in Europe many research groups work on the same problem using different tools and techniques, working in silos in academia. They are pushed to underline the differences and to avoid building on their common ground: lost opportunities in solving problems using collective intelligence.

we need to:

update of the traditional unit of knowledge: beyond PDFs, reproducibility crisis (in CrunchDAO we tried to reimplement dozen of papers, only a few made sense), limitations of traditional peer-review (difficult to write a bad review to powerful people, unable to update badly peer-reviewed paper, incentive for editors not to accept post-publications revision...), using web3 technologies.

We need:

- Infrastructure to tackle the [tragedy of the anticommons](https://en.wikipedia.org/wiki/Tragedy_of_the_anticommons) (i.e., to incentivise avoiding reinventing the wheel);
- Update of the traditional unit of knowledge: beyond PDFs;
- Tackling the reproducibility crisis: incentive system for replication and validation;
- Overcoming the limitations of traditional peer-review, using web3 technologies [@Tenorio2018].


# Solution

DeSci: Decentralized Autonomous Organization (DAO) are trying to solve scientific problems. DAOs are entities with no central leadership, collectivilty goverened by a specific set of rules enforced on the blockchain.  [[@Buterin_2019]](https://arxiv.org/abs/1809.06421)

In finance, a big step in this direction has been Crowdsourced investment [@Prado2019CrowdsourcedIR]: World Quant, Quantopian, Numerai, Quantconnect.

The impact of crowdsourcing the prediction has been disruptive (>200%).

# CrunchDAO's contribution

[CrunchDAO](https://www.crunchdao.com/) is a Decentralized Autonomous Organization of scientists making use of collective intelligence to predict the stock market.

Financial prediction requires a lot of resources.

CrunchDAO is building more: DeSci Crowdsourced R&D. Our DeSci infrastructure will enable all of us to contribute as researchers, and not only as data scientists, to the DAO.

It would be an open alternative to the current scientific system, as market-driven DAOs would finance science as a public good, and it would be an alternative the current R&D paradigm in companies, being it cheaper. The technology enables scientists to raise funding, run experiments, share data, distribute insights, and more.

Implications:

DAOs enhance the collaboration between individuals and labs. From a finance standpoint, it brings economic certainty to research uncertainty.

# CrunchDAO's contribution

Our DeSci infrastructure will enable all of us to contribute as researchers, and not only as data scientists, to the DAO.

[![IMAGE ALT TEXT HERE](./figures/youtube_preview.png)](https://www.youtube.com/watch?v=tsPmvGHMxrk)

# CrunchDAO's contribution

**"For it is unworthy of distinguished men to waste their time with slavish calculations."**

Gottfried Wilhelm Leibniz, 1672

 ![](figures/leibniz.jpg)







# DeSci in CrunchDAO

CrunchDAO is interested in crowdsourcing research, not only alpha.

- The tokeconomics will be expanded to include scientific contributions.

- We are proposing a research framework in order to foster quality, speed, and transparency.

- This framework will be a tool for the DAO in all the fields of science.

# How to kickstart your project in 10 steps!

- Step 1: Clone the *desci* repository and install the Python package;
- Step 2: Add your code/data to the package;
- Step 3: Use your new codes to produce results and plots;
- Step 4: Document your methodology in the paper, include and discuss your results;
- Step 5: Add your details to the *List of contributors*;
- Step 6: Push with git;
- Step 7: Open a Pull Request;
- Step 8: Merge, get payed and generate the new version of the paper;
- Step 9: Put it to IPFS;
- Step 10: Share it with the DAO!


# Next Steps

Next steps for the paper and tokeconomics integration.

# References