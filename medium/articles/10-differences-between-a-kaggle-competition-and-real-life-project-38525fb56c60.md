[![Sergey Makarevich](https://miro.medium.com/fit/c/96/96/2*_gn-HzBd6axuYmm4K4254Q.png)](https://medium.com/@sergeymakarevich?source=post_page-----38525fb56c60--------------------------------)[Sergey Makarevich](https://medium.com/@sergeymakarevich?source=post_page-----38525fb56c60--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F4bedc0c48f1d&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F10-differences-between-a-kaggle-competition-and-real-life-project-38525fb56c60&user=Sergey+Makarevich&userId=4bedc0c48f1d&source=post_page-4bedc0c48f1d----38525fb56c60---------------------follow_byline-----------)Jan 9, 2020

·4 min read·Member-only

<person role="ML Engineer">
https://www.linkedin.com/in/sergii-makarevych-78b62339/
</person>

[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F38525fb56c60&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2F10-differences-between-a-kaggle-competition-and-real-life-project-38525fb56c60&source=--------------------------bookmark_header-----------)![]()# 10 differences between a Kaggle competition and real life project

There are some very important differences between a Kaggle competition and real life project which beginner Data Scientists should know about. Kaggle creates a fantastic competition spirit. It’s leaderboard drives people to deliver better and better solutions pushing accuracy to the limit. Kaggle’s Notebooks and Discussions make it easy to share knowledge and learn. However real life projects are somewhat different. I hope this article will be helpful for people who consider moving into Data Science starting with Kaggle competitions. I remember I was a little bit overwhelmed when on my first real life project all the models, that typically worked well on Kaggle, miserably failed. I wish I was prepared for this.

**1. Data makes the difference, not a number of models**. In a Kaggle competition you are typically limited to the dataset provided by organisers. In real life there are no limitations like this. You can mine (i.e. collect, prepare) as much new data as you can imagine. Typically it’s data that makes the difference. Also there might be a case when you do not have any dataset at all and you have to define what data you would like to collect. You are starting from scratch which is a topic for another day.

**2. Domain expertise does matter.** When Jeremy Howard said it does not — he actually meant the Kaggle competitions. On Kaggle you have a dataset already created. It is all about understanding the data distribution, crafting features, building and stacking models. You do not need much knowledge about the data domain. However you can benefit a lot from the domain expertise whenever you have some control over the data collection process. It certainly helps you to make better assumptions about the data, which might improve your modelling. I have found that it is much harder to collect proper data than to do the modelling.

**3. Damn, there is no leaderboard.** Kaggle leaderboards make you notice an error you have made. It is really difficult to benchmark your model performances if you are the only Data Scientist working on a project. The leaderboard shows the upper limit of accuracy and you always know how much more you can possibly do to improve your model. Unfortunately, that’s not applicable in real life scenarios.

**4. Data cleaning matters.** There is no one to clean up the data for you. You are all alone with all the errors you made during the data collection process. There are typically plenty of them. And lots of improvement comes from data cleaning.

**5. Solution complexity matters.** In a Kaggle competition you have to reproduce your code only once. In real life, sometimes you have to reproduce your code every 5 or 15 minutes. A new breed of Kaggle competitions (aka Kernel competitions) are there to close that gap but they are rather rare. Model response time is typically very important for predictions made in real-time.

**6. Your test set is dynamic.** Your train set is dynamic. <quote label="data">In a Kaggle competition you perform lots of tests to pick the best features and models. Your environment is fixed most of the time — the train and test sets do not change. Often you won’t have such a comfortable setup. What’s done once in a Kaggle competition will have to be redone over and over again once your train set gets changed. In some domains your train set will change on an hourly basis!</quote> Your whole solution (including features and model selection) should be completely automated.

**7. Testing and refactoring**. Your code’s lifecycle might be longer than 2 months and you are typically going to do several deep refactoring rounds. Good testing blocks will be of help with this one. Take a look at pytest.

**8. Model deployment.** Your trained model is great but useless for the company. It has to be deployed into production in one way or another. Deployed typically means that the model is loaded into memory, has some interface to receive a request, can process it and return a prediction. WEB servers like tornado/flask might be helpful. MOOCs rarely mention that, neither does Kaggle.

**9. Performance control.** Once your model is deployed you need to control its performance. Typically you would like to retrain your model once your dataset has changed significantly or you if have collected new data. Reporting (say open source Dash or RShiny) would not only help you to control model’s accuracy over time but to attract more business attention to data science projects in your company as well. McKinsey’s “Say it with charts” or Dona M. Wong’s “The Wall Street Journal Guide to Information Graphics” are like bibles in a data presentation world.

**10. Logging.** It is typically used on Kaggle only to control the training flow. There is no need to have different logging levels to log every point of your training/prediction pipeline. In real life project anything can happen as the environment is much more complex — it is not limited to 1 notebook on a laptop or server. Good logging practices would help you to spend less time on debugging.

Sergii Makarevych, 08.01.2020, <https://www.linkedin.com/in/sergii-makarevych-78b62339/>

