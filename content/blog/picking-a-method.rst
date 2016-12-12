Picking a Method
################

:date: 2015-02-15 10:20
:modified: 2015-02-15 10:20
:tags: thats, awesome
:slug: picking-method
:authors: Peter B Winter
:summary: Over the course of my research, I've collected thousands of time-series on the movement and behavior of worms under different conditions. To frame my research in a general sense: I want to know why some experimental conditions change the behavior of the worms and what those behavioral changes are. My research sits in a very specific niche, filled with details about worm biology, tracking objects under noisy conditions, and behavioral analysis. Despite this mess of details, I also have to solve a problem familiar to any data-scientist: the problem of Picking a Method.

Over the course of my research, I've collected thousands of time-series on the movement and behavior of worms under different conditions. To frame my research in a general sense: I want to know why some experimental conditions change the behavior of the worms and what those behavioral changes are. My research sits in a very specific niche, filled with details about worm biology, tracking objects under noisy conditions, and behavioral analysis. Despite this mess of details, I also have to solve a problem familiar to any data-scientist: the problem of Picking a Method.

This problem has a thousand faces. Which clustering method should I use? What features are important in this time series? If you have data and you don't have a clear story, chances are that you are in some phase of Picking (and implementing) a Method. What makes this problem so hard is that every type of data has its own peculiarities that might invalidate the assumptions of a your favorite method. You are left trying to find an optimum in some cost function involving how effective a method is for your data (reproducible and accurate), how easy it is to implement, how quickly it runs, and how understandable the process is.

Ideally, you want to pick a method that is powerful but quick to implement. However, there's no one best strategy for figuring this out. Some of the ways I've tried to Pick a Method have been asking an expert, finding papers that analyze similar data, reading a textbook chapter, Googling all combinations of keywords with which I could describe my data, searching for winning entries in related data analysis contests, and trying every related module in the Python Package Index... The list could continue.

Although the current state of Picking a Method resembles a messy dark art, I don't think that this state will continue.

I recently read a paper that compared tens of thousands of equally-spaced univariate time-series and several thousand techniques for analyzing them. The paper proposed several potential uses for this type of data, however, one feature in particular caught my eye. By sweeping a dataset with a comprehensive set of analysis methods, the results could be used to suggest a few key methods that might be worth pursuing. Although this type of analysis is not new, (researchers have long been using gold-standard test-sets by which to compare methods) its scale gives it a different quality.

It seems like a new type of search is on the verge of becoming widely available. We are hitting a critical-mass in three factors: (1) the number of freely available online datasets (2) the amount of open-source methods that can be downloaded and easily implemented (3) and the speed of processing a large number of methods. Even so, it will be a lot of work for anyone to set up a user-friendly platform for evaluating which computational methods are usable for a given data set.

Give it five to ten years, but Picking a Method will be trivial.
