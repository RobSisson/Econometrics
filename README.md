# Econometrics
Various econometrics functions, including indices and standard calculations.

# Background
There are a variety of python packages which provide tools which can be used within the economics & statistics space (1 - 3 though this is not an exhaustive list), many of which can be applied to simulation and other forms of modelling. However, there are also a significant quantity of formulas which haven't been implemented into these python packages, often relating to ecological/sociological factors (4), or more advanced economics (5). In addition, there is also some missing fundamental economic algorithms, such as price index & balance of payments calculations which also are yet to be made in accessible Pythonic format (6). 

# Why Python?
Although Python is slower than other languages, the used of Cython can overcome the majority of this challenge, placing higher than Java, Julia, (pure) Matlab, R, and Mathematica in comparisons of languages for economics, at 2.13 seconds compared to the fastest (c++) at 1.6 seconds (7). Although run time may be out classed by C++ or other languages the ease of access to Python will reduce development time, especially in beginners, meaning that overall results may still be produced at a quicker rate. 

Python also is renowned for its excellent machine learning capabilities, and a lot of the state of the art code in this category, for example BERT or other transformer networks are written in this language. This means that not only will be it more convenient to use these packages already made, but it will likely be the go-to language for machine learning in at least the near future, and building a package such as this will help to make developments in economics, sociology and ecology (and ultimately policy design) be a part of the inevitable ML advancements which this language will see. Finally, Python has one of the largest user bases of all languages concerned (8), which means there is a larger potential for community involvement and activity, helping this project, and ultimately this field, develop more quickly.

# Aim

This package aims to remedy the above issues, by creating a python package which uses Python's low entry barriers to make practical economic, sociology and ecology of all levels more accessible, especially for use by experts in other disciplines, such as computer science and AI.

The formulas used within this package will also be heavily used in EcoSimic Intelligence to measure the effectiveness of simulations for the purposes of reinforcement learning.

# References


1 QuantEcon https://github.com/QuantEcon/QuantEcon.py

2 Statsmodels https://github.com/statsmodels/statsmodels

3 PyEconomics https://github.com/davidrpugh/pyeconomics


4 https://www.frbsf.org/economic-research/files/Rossi-HansbergSlides-VirtualClimate.pdf

5 https://github.com/chrisconlon/applied_metrics


6 https://github.com/JacekBialek/PriceIndices


7 A Comparison of Programming Languages in Economics: An Update - https://www.sas.upenn.edu/~jesusfv/Update_March_23_2018.pdf

8 Statistica https://www.statista.com/statistics/793628/worldwide-developer-survey-most-used-languages/

# Discussion
There are a multitude of items which still need to be added to this package, as detailed below, along with applicable caveats.

- <b> Economic Policy Uncertainty </b><br>
  <br>
  <u>Discussion</u>:<br>
  Although EPU is a vital indicator, relating to a wide variety of fields, caution should be aired when using certain methods to avoid overzealous acclamation of causation. <br> <br>
  For instance, when using newspaper coverage frequency (see Ref.i), awareness of the potential ulterior motives which could drive the coverage media should be maintained, as this could result in sensationalisation, especially around negative events (Ref.2), to increase sales/attention acquisition, falsely swaying indicators.<br><br>
  Evading this in general should be done by attempting to acquire additional data to weight these metrics, potentially by creating relevant indexes if they are not already available. (for the above example, development of such an index using language modelling would be perfectly possible given sufficient time/processing power.<br><br>
  <u>Data Sources</u>:<br>
  1. <a>https://www.policyuncertainty.com/index.html</a><br>
  <br>
  <u>References</u>:<br>
  1. <a>https://academic.oup.com/qje/article/131/4/1593/2468873</a><br> 
  2. <a>https://journals.sagepub.com/doi/10.1177/1748048512459143</a><br> 

  <br>
- <b> Trade Statistics </b><br>
  <br>
  <u>Discussion</u>:<br>
  Ideally getting to the point where near real-time stats are available, enabling a solid understanding of macro factors and AI supported trend analysis.<br>
  <br>
  <u>Data Sources</u>:<br>
  1. ComTrade Portal - <a>https://comtrade.un.org/data/dev/portal/</a><br>
  
  <br>
  <u>References</u>:<br>
  1. Manual on Statistics of International Trade in Services 2010 - <br><a>https://unstats.un.org/unsd/publication/seriesm/seriesm_86rev1e.pdf</a> <br>
  2. International Merchandise Trade Statistics: Compilers Manual, Revision 1 2010 - <br><a>https://unstats.un.org/unsd/trade/publications/seriesf_87Rev1_e_cover.pdf</a> <br>
  3. Balance of Payments and International Investment Position Manual - <br><a>https://www.imf.org/external/pubs/ft/bop/2007/pdf/bpm6.pdf</a> <br>
  
  <br>
- <b> National Statistics </b><br>
  <br>
  <u>Discussion</u>:<br>
  Developing and updating the Good Country Index, developing algorithms to enable near real time calculations. <br> 
  <br>
  <u>Data Sources</u>:<br>
  1. Good Country Index - <a>https://www.goodcountry.org/index/source-data/</a><br>
  2. Index of Economic Freedom - <a>https://www.heritage.org/index/?version=668</a><br>
  3. National Government Statistics - including company concentration/start ups by industry, education, agriculture, etc<br>
  4. Additional NGO Statistics - including pollution, soil type, wildlife species, traffic, etc<br>
  <br>
  
  [comment]: <> (  <br>)

[comment]: <> (- <b>  </b><br>)

[comment]: <> (  <br>)

[comment]: <> (  <u>Discussion</u>:<br>)

[comment]: <> (  <br>)

[comment]: <> (  <u>Data Sources</u>:<br>)

[comment]: <> (  1.  - <a></a><br>)
  
[comment]: <> (  <br>)

[comment]: <> (  <u>References</u>:<br>)

[comment]: <> (  1.  - <a></a><br>)
