Code for Summer 2019 Harvard Pre-college Presentation on Differential Privacy
=============================================================================

We will discuss and evaluate some methods for ensuring the privacy
of individuals in datasets that will be used for statistical analysis.
Differential privacy is a mathematical notion of individual-level data privacy that has
recently become more widely adopted (by companies such as Google and Apple) as a standard
notion of statistical privacy. We will attempt to motivate the definition which draws from
fields such as cryptography and statistics. The presentation will also include real-world examples
(and some code) of how to ensure that “present" and “future" statistical analysis satisfies
differential privacy.

In this repository, we provide some code that *YOU* can use and modify to try out differential privacy
on your personal computer.

Example Mechanisms for Differential Privacy
-------------------------------------------

1. Laplace Mechanism.

2. Gaussian Mechanism.

3. Exponential Mechanism.

4. Geometric Mechanism.

Main Files
----------

Here's some python [code](https://github.com/alabid/pre_college_2019/blob/master/code/laplace.py)
containing implementations of the Laplace mechanism on simple synthetic datasets.
And the accompanying Jupyter [notebook](https://github.com/alabid/pre_college_2019/blob/master/code/Laplace.ipynb).

Talk slides are [here](https://github.com/alabid/pre_college_2019/blob/master/slides.pdf).
