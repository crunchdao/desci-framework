---
title: "A DECENTRALIZED SCIENCE FRAMEWORK" 
subtitle: "BY CRUNCHDAO"
author: [Matteo Manzi, Enzo Caceres]
date: "2022/08/27"
lang: "en"
colorlinks: true
titlepage: true
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "360049"
titlepage-rule-height: 0
titlepage-background: "./figures/cover.pdf"
header-left: "\\hspace{1cm}"
header-right: "Page \\thepage"
footer-left: "A Decentralized Science framework"
footer-right: "CrunchDAO"
abstract: "Decentralized science (DeSci) aims to build infrastructure for creating, reviewing, crediting, storing, and disseminating scientific knowledge using the Web3 stack. In order to maximize its efficiency and prevent the tragedy of anti-commons, CrunchDAO proposes here a set of tools and best practices for Research and Development in a Decentralized Autonomous Organization."
---

# A Decentralized Science (DeSci) Framework

## DeSci: an Overview

"[Decentralized Science (DeSci)](https://ethereum.org/en/desci/), which recently came into play, refers to the communities of scientists, builders, advocates, and organizers that create infrastructure and advocate for distributed coordination to support scientific progress. It can advance the conditions of scientists worldwide and creates systems for scientists to recapture the value they create. Even in science, the success of a decentralized ecosystem depends on the community incentives structure and the microeconomy created around these incentives".

In the setup of this framework, several existing projects have been used as references for guiding our design choices. While in our context this infrastructure should enable us to collaborate, to avoid the so-called [tragedy of the anticommons](https://en.wikipedia.org/wiki/Tragedy_of_the_anticommons), and always be reproducible, and this is a means for us as a DAO to perform well in the financial market, the scope of this project is much broader and its potential in the public sector should not be neglected. Worth mentioning, for example, [the General Index](https://archive.org/details/GeneralIndex), and [Impact Certificates](https://impactmarkets.io/).

The entry point for us has been [DeSci Labs](https://desci.com/), and their work on the development of DeSci Nodes, a new unit of knowledge going beyond PDF: "DeSci Nodes creates an inventory of research artifacts, an incentive system for replication, a mechanism for validation, and a connection point embedded into your preprint."

Our design choices have also been driven by the lessons learned by Open Science, and Open-source Software Development, proposing an alternative to Academic Publishers [@Oligopoly2015]: the ["Open Journals"](https://github.com/openjournals) organization, on which also the [Julia Ecosystem](https://juliacon.github.io/proceedings-guide/author/) is building on, is the most relevant here.

One of the requirements here was to go beyond traditional peer review, using Web3 technologies. The reference project, for this, have been Ants-Review [[@Antsreview]](https://arxiv.org/pdf/2101.09378.pdf) and [@decentralizing2021]: "peer-review is a necessary and essential quality control step for scientific publications, but it lacks adequate incentives. In fact, the process, which is very costly in terms of time and intellectual investment, is not only not remunerated by journals but is not even openly recognized by the academic community as a relevant scientific achievement for a researcher. Therefore, scientific dissemination suffers in terms of timeliness, quality, and fairness."

Other reference projects have been [PRINCIPIA](https://cordis.europa.eu/article/id/422224-principia-a-new-peer-review-platform-is-here) [[@principia]](https://arxiv.org/pdf/2008.09011.pdf) and the "[Peer Review](https://github.com/danielBingham/peerreview)" repository.

Other interesting projects, in the space, are [Lateral](https://www.lateral.io/), working on the construction of knowledge graphs, [Radicle](https://radicle.xyz/) and [gitopia](https://gitopia.com/whitepaper.pdf), building on Git to enable decentralized code collaboration, [DeSci World](https://desci.world/), looking into the use of Non-Fungible Tokens for science.

## Design Choices

We are here proposing a DeSci framework, making use of IPFS, that can help perform research, outreach, and education.

The first requirement has been to expose the user as little as possible to LaTeX, giving the possibility to write in Markdown, a language developed by John Gruber and Aaron Swartz: the backend takes care of generating the unit of knowledge (not necessarily a PDF), using *pandoc*.

The paper backend lives in [this repository](https://github.com/crunchdao/desci) also containing a Python package: in this way, the symbiosys between codes and plain language can be leveraged to foster reproducibility. For example, there is a command called ```desci helloplot```:

```python
    """Hello Plot."""
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.2)

    # red dashes, blue squares, and green triangles
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.savefig('figures/helloplot.png')
```

 which can be used to produce the contents of the paper (Figure \ref{fig:helloplot}):

 ![The figure in the paper is generated by scripts living in the same repository: each version of the paper is associated with a version of the underlying scripts.\label{fig:helloplot}](figures/helloplot.png)

The paper is generated, using a [docker image](https://hub.docker.com/r/crunchdao/desci-pandoc), by the Actions of our repository: in this way, the principles of Continuous Integration/Continuous Development not only apply to software but also to the overlying scientific unit of knowledge. A similar approach has been followed in [Stencila](https://stenci.la/).

In fact, currently, scientists must be trusted to provide a true and useful representation of their research results in their final publication; blockchain would make much larger parts of the research cycle open to scientific self-correction. This bears the potential to be a technical solution to the current reproducibility crisis in science and could reduce waste and make more research results true [@Bartling2019].

Finally, an intuitive User Interface will be set up at [desci.crunchdao.com](https://desci.crunchdao.com/): contributors of these units of knowledge won't have to be skilled software developers. If you nevertheless prefer to work on your editor, you can open a pull request at the public repository \url{https://github.com/crunchdao/desci}.

It is therefore possible to make use of IPFS to create an immutable copy of each version [@Tenorio2018]: the IPFS nodes mirror the evolution of the main *git* branch. This enables the integration and recognition of micropublications and the setup of a retroactive funding framework. Moreover, this makes it possible to build around the concept of machine readability, and self-describing metadata, as the technology has the capacity to make digital goods immutable, transparent, externally provable, decentralized, and distributed.

In the context of CrunchDAO, the incentive structure is also implicit in the fact that, challenging problematic assumptions in the metamodeling and portfolio optimization, i.e., all the steps between the tournament and the production of a signal, increases its performance, leading to an increase in the value of the DAO in the market. This integration is crucial to mitigate major flows of other Crowdsourced Investment frameworks [[@openscience]](https://doi.org/10.1177/0306312718772086), also tackling issues associated with the current public funding of science [[@Buterin_2019]](https://arxiv.org/abs/1809.06421). As an example, the introduction of the [True Contribution](https://medium.com/numerai/alien-stock-market-intelligence-numerais-true-contribution-6bc7652bd6ac) has the risk of leading to an ill-defined tournament, as its players are in this way incentivised to converge to the Nash equilibrium of an imperfect information game, whose rules change as a function of the behaviour of the other tournament players.

# References
