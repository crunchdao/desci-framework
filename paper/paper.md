---
title: "CrunchDAO Staking Proposal"
author: [Kain]
date: \today
lang: "en"
colorlinks: true
titlepage: true
titlepage-text-color: "FFFFFF"
titlepage-rule-color: "360049"
titlepage-rule-height: 0
titlepage-background: "./figures/cover.pdf"
header-left: "\\hspace{1cm}"
header-right: "Page \\thepage"
footer-left: "CrunchDAO Staking Proposal"
abstract: "Decentralized science (DeSci) aims to build infrastructure for creating, reviewing, crediting, storing, and disseminating scientific knowledge using the Web3 stack. In order to maximize its efficiency and prevent the tragedy of anti-commons, CrunchDAO proposes here a set of tools and best practices for Research and Development in a Decentralized Autonomous Organization."
---

# A Decentralized Science (DeSci) Framework

## Introductiion

Here we have two objectives: a performance measure that could determine how good a prediction is and a diversity measure that tells us how different the model will be. It is well-known that a blend (a weighted combination of a set of good and diverse models can beat even the best single prediction). So the goal is to make the tournament robust to Sybil attacks and reward originality.

To do this, we need to define two performance measures, one for how accurate a model is and the other for how different it is compared to other predictions.

To block Sybil attack, it is mandatory to make having multiple accounts costly and futile. One way to do it is to have each participant have skin in the game, lock some $CRUNCH in a smart contract, and reward/punish his model proportional to the amount of his stake. 
The final meta-model would be the weighted average of all models based on their stakes. In mathematical terms, let's say we have n participants and particpant i (P~i~) has staked C~i~ Crunch tokens where i=1, 2, \ldots, n so the amount of involvement of each participant in the metamodel is

\begin{equation*}
w_i = \frac{C_i}{\sum_{i=1}^{n}{C_i}}
\end{equation*}

The final meta model would be the weighted combination of the predictions submitted by participatnt. In this case if S~i~ represents prediction of P~i~ then final prediction (S) is 

\begin{equation*}
S = \sum_{i=1}^{n}{w_i S_i}
\end{equation*}

## Performance Measure

To determine how good a model is, we need to find a meaningful metric. We have to take into consideration two regarding this metric:

* Firstly, it should vary in negative and positive ranges, for example [-1, +1], because we need this metric for each prediction's burn/earn mechanism.
* Secondly, we should be able to clip it between a reasonable range because some models could have large ups and downs in the short term, but we need a model that will perform consistently for a long time. So, for example, we can clip values to be in [-0.1, +0.1] or [-0.2, +0.2] according to the dataset.

For the metric, we can start with a simple candidate like the daily Spearman Rank Correlation averaged through a period  of time (for example, 30 or 60 days). Then, each model is rewarded based on its correction to the actual labels.  

We can replace this metric in the future with a more complex one, given that it can be used for earning and burning users' stakes.


### Originality Measure

Here we can use [Numerai's meta-model contribution (MMC) score](https://docs.numer.ai/tournament/metamodel-contribution). This score shows how much we gain by including a model in the final model and considering it can prevent heavily staked models from being more diverse so we don't end up with a few similar predictions dominating others. To calculate a user's (U) MMC for a given round we

 * select a random 67% of all staking users (with replacement)
 * calculate the stake weighted predictions of these users
 * transform both the stake weighted predictions, and U's model to be uniformly distributed
 * neutralize U's model with respect to the uniform stake weighted predictions
 * calculate the covariance between U's model and the targets
 * divide this value by 0.0841 (this step is to bring the expected score up to the same magnitude as correlation, this can skipped because we do not need it to be as the same scale as the correlations)
 * the resultant value is an MMC score
 * repeat this whole process 20 times and keep the average MMC score 


# References
