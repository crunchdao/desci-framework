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
abstract: " To be added!"
---

# Staking, Challenges and Solutions

## Introductiion

Holding a tournament like Crunchdao or Numerai is a multifaceted challenge. Here we have two objectives, a performance measure that could determine how good a prediction is and a diversity measure that tells us how different the model will be. It is well-known that a blend (a weighted combination of a set of excellent and diverse models can beat even the best single prediction). 

The tournament's other constraint is keeping the reward system robust to Sybil attacks. One way to do it is to make having multiple accounts costly and futile. One way to do it is to have each participant have skin in the game; he needs to lock some $CRUNCH in a smart contract and reward/punish his model proportional to the amount of his stake. 
The final metamodel would be the weighted average of all models based on their stakes. In mathematical terms, let's say we have $n$ participants and participant $u$ ($P_u$) has staked $C_u$ Crunch tokens where $u$=1, 2, \ldots, $n$ so the amount of involvement of each participant in the metamodel is

\begin{equation*}
w_u = \frac{C_u}{\sum_{u=1}^{n}{C_u}}
\end{equation*}

The final metamodel would be the weighted combination of the predictions submitted by participants. In this case if $S_u$ represents prediction of $P_u$ then final prediction ($S$) is 

\begin{equation*}
S = \sum_{u=1}^{n}{w_u S_u}
\end{equation*}


## Performance Measure

We need to find a meaningful metric to determine how good a model is. We have to take into consideration two things regarding this metric:

* Firstly, it should vary in negative and positive ranges, for example, $[-1, +1]$, because we need this metric for each prediction's burn/earn mechanism.
* Secondly, we should be able to clip it between a reasonable range because some models could have large ups and downs in the short term, but we need a model that will perform consistently for a long time. So, for example, we can clip values to be in $[-0.1, +0.1]$ or $[-0.2, +0.2]$ according to the dataset.

For the metric, we can start with a simple candidate like the daily Spearman Rank Correlation averaged through a period (for example, 30 or 60 days). Then, each model is rewarded based on its correction to the actual labels.  

We can replace this metric with a more complex one, given that it can be used for earning and burning users' stakes.


### Originality Measure

Here we can use [Numerai's metamodel contribution (MMC) score](https://docs.numer.ai/tournament/metamodel-contribution). This score shows how much we gain by including a model in the final model and considering it can prevent heavily staked models from being more diverse, so we don't end up with a few similar predictions dominating others. To calculate a user's (U) MMC for a given round we

 * Select a random 67% of all staking users (with replacement)
 * calculate the stake-weighted predictions of these users
 * transform both the stake-weighted predictions and u's model to be uniformly distributed
 * neutralize u's model with respect to the uniform stake-weighted predictions
 * calculate the covariance between u's model and the targets
 * divide this value by 0.0841 (this step is to bring the expected score up to the same magnitude as the correlation, this can be skipped because we do not need it to be on the same scale as the correlations)
 * the resultant value is an MMC score
 * repeat this whole process 20 times and keep the average MMC score 

## Rewarding as a Multi-objective Optimization Problem

So far, we have been proposing the same as the current metrics used in the Numerai tournament. However, in Numerai, after calculating the performance metric (they call it $TC$) and $MMC$, users can pick a combination of these scores to determine their rewards or punishment. For example, one can choose $1 \times TC$ or $TC + 2 \times MMC$ as a multiplier for his stakings. Here we propose to use another method. 

We treat the problem of combining these metrics as a multiobjective optimization problem where we have two objective functions to maximize. The objectives are
 
* performance metric ($PM$) that determines how good a prediction is;
* and diversity metric ($MMC$) that tells us how much we miss if we don't include a prediction in a metamodel.

There is no single solution to this problem; instead, there are possible solutions called the [Pareto Frontier](https://en.wikipedia.org/wiki/Pareto_front). To find the Pareto frontier for this problem, we need to define a few things: 

* ($PM_u$, $MMC_u$) for user $u$ represents a vector with two elements (each element shows an evaluated objective)
* In a maximization scenario with $k$ objective functions ($f_i(x)$, where $i \in {1, …, k}$), a feasible solution $x_1 \in X$ is said to (Pareto) dominate another solution $x_2 \in X$, if

\begin{align*}
   &\forall  i \in {1, …,k} , f_i(x_1) \ge f_i(x_2),\\
   &\exists i \in {1, …,k} , f_i(x_1) > f_i (x_2).
\end{align*}

* A Pareto optimal solution is a non-dominated vector in all feasible solutions.

## The Proposed Rewarding Method 

For a user $u$, we calculate the ($PM\_u$, $MMC\_u$) and then find the Pareto optimal solutions in the set of all users, so we end up with two sets of dominated and not-dominated solution vectors. Finally, based on the result, we multiply the staking of users with Pareto optimal solutions with a value called $\alpha$ (called the rewarding factor) where $\alpha > 1$. This parameter determines how much we value having high values for both objectives simultaneously rather than just one objective.   

For the user u with $C_u$ amount of Crunch tokens, if his model is not dominated, his staking is multiplied by $\alpha$ so his new $C_u$ would be $C_{u-new}=\alpha \times C_u$  ). This way, users are motivated to increase the accuracy and diversity of their model at the same time. It also keeps the door open for users with not large stakings to participate because if others do not dominate their predictions, their rewards are boosted as if they are given bonuses for their performance. If we do not consider this factor, the whole prize pool will be swept by whales with large amounts of stakings after a while. Additionally, with this mechanism, the population of predictions is motivated to move towards more diverse and promising solutions.

 
##  Attracting and Keeping the Best

The way that rewarding works makes it possible for the DAO to reward  the best (Pareto Optimal) predictions and the users that submmtted them by adjusting $\alpha$, for example an $\alpha=4$ makes it possible for a good user to quadraple his stakes even if he does not have a lot to stake compared to whales. 

## Prize Pool Consideration

At the start, we have a prize pool of $C$ crunches each month (or week, or any other span of time), and each person's reward/punishment is calculated proportionally to his stakes. 

## Alpha Provider Tournament

The same ideas here can be used for the alpha generation tournament. Alpha is just like any other prediction!

## Summary

* We will currently use the average correlation function for the performance metric. Still, in the future, as long as we can burn and earn, we can replace the performance measure with something like TC from Numerai or anything else.
* We are using the same originality measure from the numeral, and we can replace it with any other objects in the future. 
* The way the reward system works based on staking makes Sybil attack impossible.
* Boosting the payouts based on Pareto optimality is very simple and only needs one parameter to tweak. It also motivates small-time stakers to take their chance in the game. 
* Using Pareto optimality also allows the DAO to add new objectives in the future if it sees fit. 
* Payouts are done in cycles and the prize pool is divided by the number of datasets and each dataset has its own payout.  



