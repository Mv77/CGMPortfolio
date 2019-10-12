# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # Cocco, Gomes & Maenhout

# %% [markdown]
# # "[Consumption and Portfolio Choice over the Life Cycle](https://academic.oup.com/rfs/article-abstract/18/2/491/1599892)"
#
# - Notebook created by Mateo Velásquez-Giraldo
# - All figures and tables were taken from the linked paper.

# %% [markdown]
# ### Summary
#
#

# %% [markdown]
# ### Overview 
#
#
# #### Rate-of-return heterogeneity
#
#
#
# #### Non-technical methodological overview
#
#
#
# #### The two main effect of wealth taxation
#
#

# %% [markdown]
# ### The model
#
# #### Households/entrepreneurs
#
#
# #### Labor and entrepreneurial productivity
#
# #### The individuals' decision problems
#
# ##### Static production/allocation problem
#
# ##### Dynamic problem
#
# The problem and value function of a household of age $h$ is given by
#
# \begin{align}
#     V_h(a;\mathbf{S}) = &\max_{c,l,a'} u(c,1-l) + \beta\frac{\phi_{h+1}}{\phi_{h}} \mathbb{E}[V_{h+1}(a',\mathbf{S}')|S]\\
#     \text{s.t.} \quad & a' = \mathcal{Y}(a,l;z,e,\kappa;\mathcal{T}) - c(1+\tau_c)\\
#     & a'\geq 0
# \end{align}
#
# where $\mathcal{Y}$ denotes the total disposable income of the individual after production and taxation, $\mathbf{S}$ is the vector of individual exogenous states, and $\mathcal{T}$ represents the tax system.
#

# %% [markdown]
# ### Results
#
# The authors conduct various experiments. We now report the main ones.

# %% [markdown]
# ### Conclusion
#
# In the presence of rate-of-return heterogeneity, capital income taxes disproportionately affect productive entrepreneurs. Switching to wealth taxation moves the tax burden towards unproductive entrepreneurs and increases after-tax return heterogeneity, which elicits a reallocation of capital towards productive entrepreneurs. The increased efficiency and the expanded tax base increase output and allow the government to reduce labor income taxes. The authors therefore conclude that wealth taxation can increase efficiency and output while decreasing consumption inequality.
#
# Through simulation exercises calibrated to match U.S. data, the authors find that the optimal wealth tax rate is around 3%.
