# Unit 4. Raster and Vector Layers
## Activity No. 3
## Type of Activity Discussion
## Worth 4 points
## Time effort 3 hrs (est.)
## Topic Code Optimization with Raster Data
## Introduction
This unit’s discussion uses a Python script (stats.py) that implements two different ways of reading a raster
layer and computing its average value. Whether one algorithm or another is used is specified in the script
by the value of the variable `version` (Line 12).

Because your machine never uses the exact amount of resources to process the same operation, the
chosen algorithm is run a number of `n_tests` times (Line 11) and summary statistics about the time costs
of the sample of tests are computed.

A function for the retrieval of summary statistics from a list of data is defined in Lines 101-114. This
function can also be used to compute statistical summaries from raster layers, so it is a tool that does not
exist in the Python API for QGIS.

You can run either version of the average algorithm by setting `version` to 1 (first algorithm) or 2 (second
algorithm). You can also use the `n_tests` variable to modify the number of times each algorithm is rerun.
By default, the code runs an algorithm 100 times.

Also, note that the script uses a few new packages for several sorts of quantitative analyses: `Numpy`, `SciPy`,
`Math`, and `Time`.

## Objectives
The discussion requires you to think about two implications of the algorithms included in the script:

1. Notice that, in the script, global parameters are declared in lines 46-59, that is, inside the loop that runs the tests. This means that the global parameters are re-created at the beginning of any run. Given that these parameters remain constant for as long as the entire script is run and have the same values over all the tests, *do you think of a better way to relocate or reorganize the commands in Lines 46-59 so the script can cut down time costs by avoiding to re-create the same parameters at every test start?*
2. Also, by running the two versions of the algorithm you can observe that the first algorithm runs notably slower but it produces a vector of pixel data that could be used to compute any statistical measure about the raster layer. The second option, on the other hand, runs faster and saves up computer resources because it does not keep the entire vector of pixel data in memory, although it fails to provide a proper data format to be reused in additional measurements of the raster layer. *What algorithm is best, if any, or when could one of the algorithms be better than the other depending on the limitations of the computer, the goals of the analysis, and/or time performance objectives?*

## Workflow
1. Answer questions A and B.
2. Comment on the answer of at least one of your classmates. Hopefully, we will be able to
brainstorm collectively and come up with a list of possible strategies to improve the processing
performance of these algorithms.
