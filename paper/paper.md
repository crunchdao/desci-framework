---
title: "A Decentralized Science framework for CrunchDAO"
author: [Matteo Manzi]
date: "2022-08-27"
lang: "en"
titlepage: true,
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "360049"
titlepage-rule-height: 0
titlepage-background: "./figures/background.pdf"

header-left: "\\hspace{1cm}"
header-right: "Page \\thepage"
footer-left: "\\thetitle"
footer-right: "\\theauthor"
---

# Introduction 

## Reference Projects

- [DeSci Nodes](https://desci.com/nodes)
- [Peer Review](https://github.com/danielBingham/peerreview)
- [Ants-Review](https://arxiv.org/abs/2101.09378)
- PRINCIPIA: a Decentralized Peer-Review Ecosystem: [paper](https://arxiv.org/pdf/2008.09011.pdf) and [article](https://cordis.europa.eu/article/id/422224-principia-a-new-peer-review-platform-is-here)
- [DeSci World](https://desci.world/)
- [IPLD](https://ipld.io/)
- [Radicle](https://radicle.xyz/)
- [openjournals-draft-action](https://github.com/openjournals/openjournals-draft-action)
- [inara](https://github.com/openjournals/inara)

```java
public class Example implements LoremIpsum {
	public static void main(String[] args) {
		if(args.length < 2) {
			System.out.println("Lorem ipsum dolor sit amet");
		}
	} // Obscura atque coniuge, per de coniunx
}
```

\begin{equation}\label{eq:neighbor-propability}
    p_{ij}(t) = \frac{\ell_j(t) - \ell_i(t)}{\sum_{k \in N_i(t)}^{} \ell_k(t) - \ell_i(t)}
\end{equation}

Test Nr. | Position | Radius | Rot | Grün | Blau | beste Fitness | Abweichung |
|---|---|---|---|---|---|---|---|
1 |  20 % |  20 % |  20 % |  20 % |  20 % |  7,5219 |  0,9115 |
2 |   0 % |  25 % |  25 % |  25 % |  25 % |  8,0566 |  1,4462 |
3 |   0 % |   0 % |  33 % |  33 % |  33 % |  8,7402 |  2,1298 |
4 |  50 % |  20 % |  10 % |  10 % |  10 % |  6,6104 |  0,0000 |
5 |  70 % |   0 % |  10 % |  10 % |  10 % |  7,0696 |  0,4592 |
6 |  20 % |  50 % |  10 % |  10 % |  10 % |  7,0034 |  0,3930 |
7 |  40 % |  15 % |  15 % |  15 % |  15 % |  6,9122 |  0,3018 |

```python
a = 3
for i in range(6):
  print(a)
```
## DeSci framework for decentralized paper writing

In the process of setting this up, document design choices and use them to populate a first paper talking about 
its underlying technology.

- Integrate LaTeX/Markedown + Python.
- Generate papers with github actions.
- Render paper in CrunchDAO website and build UX for easy reviews/comments/pull requests.

- Integrate ResearchRabbit or something like it;
- Integrate SciHub, libgen and others in the backend.
- Integrate knowledge graphs, once out, from [Lateral](https://www.lateral.io/)

## The research paper(s) V1.0: Cover the CrunchDAO investment rationale

- Start from website+documentation, 2 medium articles, CrunchDAO website. 
- Study NumerAI and RocketCapital and understand differences, Judge Research.
- Record long technical deep talk with Jean to understand everything.

- Layer 1 vs Layer 2 in CrunchDAO

### Metamodeling Layer 1

- Understand and document Udit work:
    -  [Barra Risk Factor Analysis](https://www.investopedia.com/terms/b/barra-risk-factor-analysis.asp);
    -  [Idiosyncratic Risk](https://www.investopedia.com/terms/i/idiosyncraticrisk.asp);
    -  [Risk-Adjusted Return](https://www.investopedia.com/terms/r/riskadjustedreturn.asp);
    -  [Sharpe Ratio](https://www.investopedia.com/terms/s/sharperatio.asp);
    - [Spearman's rank correlation coefficient](https://en.wikipedia.org/wiki/Spearman%27s_rank_correlation_coefficient)


- Digest and document "Crowdsourced Investment Research Through Tournaments" and Lopez de Prado more in general;
- How can people add different datasets? 

# Aggregate the scientific community

Filter these in the subsections below:

- Kind of council of elders of top crunchers: identify and engage top scientific profile from the community 
- Allow elders to interact with the research paper in a DeSci way 
- Orchestrate the call for signal and Cherry peek the best signals 

- Work on the definition of KPIs. Some ideas: 
    - Number of interaction on the paper
    - Median signal performance (Sharpe, ROI, DD)
    - Number of interaction with the podcasts.
    - Some way to evaluate the engagement of the syndacate.
    

## NFTs

At the beginning, we gift an NFT to people we want as advisors and having one leads to being able to give a feedback on the paper. See [here](https://www.boffinsociety.xyz/) and [here](https://desci.world/). This will allow people to join the GROUP OF COOL PEOPLE YET TO BE NAMED (Mathematical syndicate?).

The NFTs could be about stochastic processes (video+audio), and about financial models more in general.

Then we vote with tokens to decide whether the pull request on the paper is accepted or not. Voting on the papers shall become part of civil duties. How will be individual decisions be integrated into the final one? More token more power, one head one vote? Or something fancy like ["A Flexible Design for Funding Public Goods"](https://arxiv.org/abs/1809.06421). Or something like [this](https://www.bretthennig.com/reinvigorating_democracy_through_random_selection)?

What is the role of SBTs here? Decentralized Society: Finding Web3’s Soul.

The outcome of the peer review changes your grade in the DAO which changes your access to the APY, Alternative idea, you stake on the pull request and if it is bad you lose.

For all this, we need IPFS + git. See [here](https://radicle.xyz/), maybe.

## Social Presence (Talk with Ben for this)

- Stardust Podcast (or alternative one?) The crunch podcast ? 2 / month? Maybe call it Matteo podcast and talk about CrunchDAO. Talk about the models, talk about the results. 
- LinkedIn
- Twitter
- Medium, or maybe [Mirror](https://mirror.xyz/) better?
- Youtube
- Anchor

# R&D finance

- The research paper(s) V1.0: Cover the CrunchDAO investment rationale 
- Iterate once every 4 weeks on a new update of the paper 
- KPIs
    - MM Sharpe
    - Backtest
        - MM ROI - backtest
        - MM DD - backtest
        - Competition OWEN and Spearman
        
# Markdown primer

Markdown is based on email conventions. It was developed by John Gruber
and Aaron Swartz. This section provides a brief introduction to Markdown
syntax. Certain details or alternatives will be omitted,

If you are already familiar with Markdown, then you may want to skip
this section and continue with the description of [article metadata].

## Inline markup

The markup in Markdown should be semantic, not presentations. The table
below gives a small example.

+---------------------+-------------------------+-----------------------+
| Markup              | Markdown example        | Rendered output       |
+:====================+:=======================:+:=====================:+
| emphasis            | `*this*`                | *this*                |
+---------------------+-------------------------+-----------------------+
| strong emphasis     | `**that**`              | **that**              |
+---------------------+-------------------------+-----------------------+
| strikeout           | `~~not this~~`          | ~~not this~~          |
+---------------------+-------------------------+-----------------------+
| subscript           | `H~2~O`                 | H~2~O                 |
+---------------------+-------------------------+-----------------------+
| superscript         | `Ca^2+^`                | Ca^2+^                |
+---------------------+-------------------------+-----------------------+
| underline           | `[underline]{.ul}`      | [underline]{.ul}      |
+---------------------+-------------------------+-----------------------+
| small caps          | `[Small Caps]{.sc}`     | [Small Caps]{.sc}     |
+---------------------+-------------------------+-----------------------+
| inline code         | `` `return 23` ``       | `return 23`           |
+---------------------+-------------------------+-----------------------+

: Basic inline markup and examples.
### Images

Markdown syntax for an image is that of a link, preceded by an
exclamation mark `!`.

The main use of images in papers is within figures. An image is treated
as a figure if

1. it has a non-empty description, which will be used as the figure
   label and
2. it is the only element in a paragraph, i.e., it must be surrounded by
   blank lines.

### Citations

Bibliographic data should be collected in a file `paper.bib`; it
should be formatted in the BibLaTeX format, although plain BibTeX
is acceptable as well. All major citation managers offer to export
these formats.

Cite a bibliography entry by referencing its identifier:
 will create the reference "[@upper1974]". Omit the
brackets when referring to the author as part of a sentence: "For
a case study on writers block, see @upper1974." Please refer to
the [pandoc manual](https://pandoc.org/MANUAL#extension-citations)
for additional features, including page locators, prefixes,
suffixes, and suppression of author names in citations.
### Footnotes


Syntax for footnotes centers around the "caret" character `^`. The
symbol is also used as a delimiter for superscript text and thereby
mirrors the superscript numbers used to mark a footnote in the final
text.[^markers]

``` markdown
Articles are published under a Creative Commons license[^1].
Software should use an OSI-approved license.

[^1]: An open license that allows reuse.
```

Note numbers do not have to be sequential, they will be reordered
automatically in the publishing step. In fact, the identifier of a note
can be any sequence of characters, like `[^marker]`, but may not contain
whitespace characters.

[^markers]: Although it should be noted that some publishers prefer
    symbols or letters as footnote markers.

The above example results in the following output:

> Articles are published under a Creative Commons license[^1].
> Software should use an OSI-approved license.
>
> [^1]: An open license that allows reuse.


### Lists

Bullet lists and numbered lists, a.k.a. enumerations, offer an
additional method to present sequential and hierarchical information.

- apples
- citrus fruits
  - lemons
  - oranges

Enumerations start with the number of the first item. Using the the
first two [laws of
thermodynamics](https://en.wikipedia.org/wiki/Laws_of_thermodynamics) as
example.

0. If two systems are each in thermal equilibrium with a third, they are
   also in thermal equilibrium with each other.
1. In a process without transfer of matter, the change in internal
   energy, $\Delta U$, of a thermodynamic system is equal to the energy
   gained as heat, $Q$, less the thermodynamic work, $W$, done by the
   system on its surroundings. $$\Delta U = Q - W$$
# Internal references

Markdown has no default mechanism to handle document internal
references, often called "cross-references". This conflicts with goal of
[Open Journals] is to provide authors with a seamless and pleasant
writing experience. This includes convenient cross-reference generation,
which is why a limited set of LaTeX commands are supported. In a
nutshell, elements that were marked with `\label` and can be referenced
with `\ref` and `\autoref`.

## Tables and figures

Tables and figures can be referenced if they are given a *label*
in the caption. In pure Markdown, this can be done by adding an
empty span `[]{label="floatlabel"}` to the caption. LaTeX syntax
is supported as well: `\label{floatlabel}`.

Link to a float element, i.e., a table or figure, with
`\ref{identifier}` or `\autoref{identifier}`, where `identifier`
must be defined in the float's caption. The former command results
in just the float's number, while the latter inserts the type and
number of the referenced float. E.g., in this document
`\autoref{proglangs}` yields "\autoref{proglangs}", while
`\ref{proglangs}` gives "\ref{proglangs}".

: Comparison of programming languages used in the publishing tool.
  []{label="proglangs"}

| Language | Typing          | Garbage Collected | Evaluation | Created |
|----------|:---------------:|:-----------------:|------------|---------|
| Haskell  | static, strong  | yes               | non-strict | 1990    |
| Lua      | dynamic, strong | yes               | strict     | 1993    |
| C        | static, weak    | no                | strict     | 1972    |

## Equations

Cross-references to equations work similar to those for floating
elements. The difference is that, since captions are not supported
for equations, the label must be included in the equation:

    $$a^n + b^n = c^n \label{fermat}$$

Referencing, however, is identical, with `\autoref{eq:fermat}`
resulting in "\autoref{eq:fermat}".

$$a^n + b^n = c^n \label{eq:fermat}$$

Authors who do not wish to include the label directly in the formula can use a Markdown span to add the label:

    [$$a^n + b^n = c^n$$]{label="eq:fermat"}


Hi Benjamin, this equations is about the work we did today:

$$ \rho(x) = 3$$

Wow, also Joseph is here! I am showing you how we can discuss about fractional calculus in html!

# Pandoc

Readers may wonder about the reasons behind some of the choices made for
paper writing. Most often, the decisions were driven by radical
pragmatism. For example, Markdown is not only nearly ubiquitous in the
realms of software, but it can also be converted into many different
output formats. The archiving standard for scientific articles is JATS,
and the most popular publishing format is PDF. Open Journals has built
its pipeline based on [pandoc](https://pandoc.org), a universal document
converter that can produce both of these publishing formats -- and many
more.

A common method for PDF generation is to go via LaTeX. However, support
for tagging -- a requirement for accessible PDFs -- is not readily
available for LaTeX. The current method used ConTeXt, to produce tagged
PDF/A-3, a format suited for archiving [@pdfa3].

# References
