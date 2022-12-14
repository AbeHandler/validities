[![Elad Cohen](https://miro.medium.com/fit/c/96/96/2*X2kzprbLHe9PNAhHMr5EQw.png)](https://elad-cohen.medium.com/?source=post_page-----8132b295bcdb--------------------------------)[Elad Cohen](https://elad-cohen.medium.com/?source=post_page-----8132b295bcdb--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F8bcfe8a3d8b&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Favoiding-the-4-major-pitfalls-of-data-science-projects-8132b295bcdb&user=Elad+Cohen&userId=8bcfe8a3d8b&source=post_page-8bcfe8a3d8b----8132b295bcdb---------------------follow_byline-----------)Mar 21, 2021

·7 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F8132b295bcdb&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Favoiding-the-4-major-pitfalls-of-data-science-projects-8132b295bcdb&source=--------------------------bookmark_header-----------)# Avoiding the 4 Major Pitfalls of Data Science Projects

<person role="Deputy Vice President">
https://www.linkedin.com/in/elad-cohen-ai/?originalSubdomain=il
</person>

## *Working on a data science project, especially with a new stakeholder, can be challenging. Learn how to avoid the main pitfalls.*

![]()Image by [Riskified](https://www.riskified.com/) (used with permission)As data science, machine learning, and AI continue to grow in popularity across business domains, companies are trying to leverage these technologies for new problems. As a data scientist, you know that there’s a high likelihood that your upcoming project might fail. This is especially true if machine learning is only a small aspect of your company’s operations — a feature in the main product or a method for generating valuable business insight. At [Riskified](https://medium.com/riskified-technology), machine learning is at the core of our business, but keeping these pitfalls in mind is always important.

There are countless reasons a project could fail due to unprofessionalism on the data scientist’s side: selection bias, target leakage, data drift, p-hacking, overfitting and more. In this article, however, we’ll focus on some fundamental issues pertaining to collaboration with the business.

Incorporating data science is the same as any change management process — it requires careful consideration and planning to get right. Any significant change process needs a strong coalition of members, including champions who will create a vision, promote it, and remove obstacles. One of the greatest classic change management models is [John Kotter’s 8 step process](https://cio-wiki.org/wiki/Kotter%27s_8-Step_Change_Model), which emphasizes the importance of planning the change process well in advance. Let’s see what can happen when that critical preparation work hasn’t been performed. Hopefully, the tips below can help save your data science project or avoid starting one that’s destined to fail.

# Bad data

If you’re the first data scientist in your organization (or in a business unit that hasn’t used data science before), there’s a good chance you’re either missing crucial data, or the data quality isn’t good enough to get started. Talking with data engineers or DBAs about existing data, getting permissions and access to that data, exploring it to check the features, null rates, consistency, validating how far back it goes, the existence of the predicted label, the accuracy of that label, and other quality issues can take a tremendous amount of time. If your company has been doing pretty well so far, those data providers won’t necessarily understand why they have to meet new stringent demands concerning data quality (“everything worked great so far, no?”).

For the business people outside your line of work, it can seem like no progress is being made during this long stretch of time, as it’s a seemingly never-ending process of data cleaning. If senior management doesn’t understand the significant prep work required to get the data to a minimal working condition, they won’t have the necessary patience and expect results much too soon. In companies that take on a lot of technical debt to move quickly, the data quality will likely be even worse, and their patience even lower as they’re accustomed to fast deliverables.

If you’re in this tricky situation, it’s vital to get access to the data and start some minimal exploration before making any assumptions about how fast you might be able to progress on your project (or whether the project is even feasible). If you’re a stakeholder that wants to incorporate data science for the first time, it’s important to start preparing the data well in advance or risk having an extremely frustrated hire who might leave quickly.

# Lack of buy-in and trust

Your company’s senior management is likely getting bombarded with messages promising miracles by implementing “AI.” You may find a lone senior executive decided to take a chance by introducing machine learning into their organization. The specifics around how AI will actually be leveraged, the business problems it will solve, and the value it can bring are [left as details for you to figure out](https://medium.com/riskified-technology/how-we-choose-what-to-research-57acb835fdd7). While this can work, the organization has to understand both the amount of prep work required to leverage machine learning and the types of problems it excels at solving.

If the organization isn’t ready, you’ll typically see limited buy-in into machine learning throughout the company (i.e., it’s driven top-down by executives), which means you might hit roadblocks with middle-management stakeholders. From the data scientist’s perspective, it might look a little like this: you just completed a project for a new stakeholder who isn’t accustomed to working with machine learning. During one of the final meetings, you don’t get many questions or feedback about the work. As any salesperson knows, it’s easier to work with a ‘no’ than to not get any feedback. Less experienced data scientists might try to prove the value of their solution. However, by the time you’ve hit this point, it’s probably too late. Your stakeholders just aren’t engaged and won’t end up using your project.

Additionally, many companies aren’t truly data-driven. While every company says their decisions are driven by data (in today’s business environment, it’s practically blasphemy to say otherwise), many companies don’t actually operate this way. In many cases, this may stem from not having sufficient data. As a result, they haven’t improved their analytical capabilities, and the company culture may not value the methodical testing of new processes. If a data scientist (or specifically a decision scientist) delivers [unique and critical insight](https://medium.com/riskified-technology/data-vs-insight-the-thin-line-between-good-and-bad-reports-91997d5e9cd) that counters the company’s tribal knowledge, there’s a good chance that intuition will prevail. Employees just won’t feel comfortable enough pushing back and challenging this type of work and if it’s different enough than what they know, they just won’t accept it.

To avoid this, it’s crucial to understand who your stakeholders are and engage them throughout the process. Don’t show up after several weeks of work with a solution and expect them just to accept it. By involving your stakeholders frequently, leveraging their domain expertise, and allowing them to shape your project’s solution, you can utilize the [Ikea effect](https://en.wikipedia.org/wiki/IKEA_effect) — the stakeholder will value the project more once they’ve personally invested time into it.

# Stakeholders who don’t know

Sometimes the stakeholders are interested in leveraging machine learning but don’t know how to use it. You might genuinely have enough engagement and interest at the relevant levels (both executive buy-in and middle management), but they aren’t sure what exactly to expect and lack a clear understanding of the process behind machine learning. They may be expecting immediate results and grow impatient when data scientists keep mentioning data quality issues, lack of required tools and infrastructure, or difficulties deploying their first models within the existing production system.

From the data scientist’s perspective, it could look like this: you’ve started a project with a new stakeholder who has little experience working with data science. They want to tap into that ‘ML magic’ but have a hard time defining their specific problem. You might feel pressured to start exploring the data and ‘see what you can come up with.’ While this can work, it should be avoided whenever possible.

<quote label="metric">
First, pinpoint the specific metric you’d like to try and predict — every moment spent on detailing the metric calculation and the definition of done is time well-spent.
</quote>
This can also help you set expectations from the get-go — some stakeholders might expect the impossible from ML, and it’s much better to be upfront about this before starting the project. Feel free to explore the data first, but don’t be tempted to just start and see how well you can do. It’s also crucial to reiterate the inherent unpredictability of any research project. Issues you didn’t consider will pop up and the performance you were hoping for may not be reached. Be very cautious about committing to specific performance goals or delivery dates.

As the project progresses, continuously run what-if analyzes before advancing too far ahead. For example, if you’ve started with a simple benchmark model, discuss the accuracy metrics with the stakeholders. Is the model already good enough to be valuable? If not, is it even in the right ballpark? Is the complexity feasible for implementation in production? What other constraints need to be taken into account?

It’s good to discuss these issues frequently, especially when the project has advanced and new information needs to be considered.

# When Stakeholders change their mind

In some cases, the stakeholders might be very clear on what they’re asking for and you’ve agreed upon all the expectations before going ahead. As data science projects can take several weeks (or even months), stakeholders may change their request. This can occur due to:

* The original request is no longer relevant. Whenever possible, working with faster incremental deliverables (agile over waterfall) can help reduce these types of issues.
* Success in the original task drives the project in different directions. For example, the stakeholder may have originally requested a very accurate sales forecast. While this sounds straightforward, the solution might involve an ensemble of multiple models, each with various parameters and seasonality. After you have finally improved the model to meet the original threshold and it is being leveraged by the business, the stakeholder now requests the ability to explain the rationale behind each prediction. This can be a much larger request than the stakeholder would imagine, and such a necessity is best discussed at the onset of the project, as it could impact the complexity of the designed solution.
* Stakeholders change — don’t assume that everyone will treat your work similarly. A new stakeholder with less buy-in, limited experience working with machine learning, and a general higher level of skepticism might severely impact your project’s progress. Again, it’s important to strive for incremental quick wins to showcase the value to the business. It’s much easier to greenlight a track that’s demonstrating value than to continue investing in a black box with no clear end date.
As a true professional, you need to consider how your stakeholder views your work and weigh the constraints and limitations that impact your work. Whether you’re working on a project with a new stakeholder or just starting up data science at your company, always plan several steps ahead — manage the expectations, focus on incremental value, and generate the buy-in required for your project to become a success. There’s just too little time and too much work to let an otherwise well-run data science project go to waste. Good luck!

If you’ve gotten this far, you might enjoy my previous blogs:

[## 7 Must-Haves in your Data Science CV

### Looking for a new role? Be sure to check these critical points to stand out of the crowd and pass the CV screen.

towardsdatascience.com](/7-must-haves-in-your-data-science-cv-9316841aeb78)[## 3 Ways to Break Into Data Science

### Starting your journey into Data Science? Choose the right path to increase your odds.

medium.com](https://medium.com/riskified-technology/3-ways-to-break-into-data-science-6a7a8fd679b3)