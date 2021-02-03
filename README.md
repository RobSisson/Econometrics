# Econometrics
Various econometrics functions, including indcies and standard calculations.

# Background
There are a variety of python packages which provide tools which can be used within the economics & statitics space (1 - 3 though this is not an exhaustive list), many of which can be applied to simulation and other forms of modelling. However, there are also a significant quantity of formulas which havent been implemented into these python packages, often relating to ecological/sociological factors (4), or more advanced economics (5). In addition, there is also some missing fundamental economic algorithms, such as price index & balance of payments calculations which also are yet to be made in accessible Pythonic format (6). Although Python is slower than other languages, the used of Cython can overcome the majority of this challenge, placing higher than Java, Julia, (pure) Matlab, R, and Mathematica in comparisons of languages for economics, at 2.13 seconds compared to the fastest (c++) at 1.6 seconds (7)

This package aims to remedy the above issues, by creating a python package which uses Python's low entry barriers to make practical economic, sociology and ecology of all levels more accessible, especially for use by experts in other disciplines, such as computer science and AI.

The formulas used within this package will also be heavily used in EcoSimic Intelligence to measure the effectiveness of simulations for the purposes of reinforcement learning.

1 QuantEcon https://github.com/QuantEcon/QuantEcon.py

2 Statsmodels https://github.com/statsmodels/statsmodels

3 PyEconomics https://github.com/davidrpugh/pyeconomics


4 https://www.frbsf.org/economic-research/files/Rossi-HansbergSlides-VirtualClimate.pdf

5 https://github.com/chrisconlon/applied_metrics


6 https://github.com/JacekBialek/PriceIndices


7 A Comparison of Programming Languages in Economics: An Update - https://www.sas.upenn.edu/~jesusfv/Update_March_23_2018.pdf
