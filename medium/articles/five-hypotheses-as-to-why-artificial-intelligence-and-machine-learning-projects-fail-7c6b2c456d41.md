[![Alison Doucette](https://miro.medium.com/fit/c/96/96/2*oy2LNzAWuL9njI9TqXwdZw.jpeg)](https://alison-doucette.medium.com/?source=post_page-----7c6b2c456d41--------------------------------)[Alison Doucette](https://alison-doucette.medium.com/?source=post_page-----7c6b2c456d41--------------------------------)[Follow](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fsubscribe%2Fuser%2F9965a65790c2&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ffive-hypotheses-as-to-why-artificial-intelligence-and-machine-learning-projects-fail-7c6b2c456d41&user=Alison+Doucette&userId=9965a65790c2&source=post_page-9965a65790c2----7c6b2c456d41---------------------follow_byline-----------)Aug 23, 2019

·5 min read[Save](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2F7c6b2c456d41&operation=register&redirect=https%3A%2F%2Ftowardsdatascience.com%2Ffive-hypotheses-as-to-why-artificial-intelligence-and-machine-learning-projects-fail-7c6b2c456d41&source=--------------------------bookmark_header-----------)# **Five Hypotheses as to why Artificial Intelligence and Machine Learning projects fail**

![]()There are numerous [articles](https://www.gartner.com/en/newsroom/press-releases/2018-02-13-gartner-says-nearly-half-of-cios-are-planning-to-deploy-artificial-intelligence) and published papers around why AI/Machine Learning/Natural Language Processing projects never make it to “production” or fail to deliver on the value proposed (Gartner predicts that through 2022, 85 percent of AI projects will deliver erroneous outcomes due to bias in data, algorithms or the teams responsible for managing them). The following are a few hypotheses as to why ArtificialIntelligence projects fail and some observations on company reactions (technical and organizational) to AI projects lack of delivered value. Please note these opinions do not reflect on any current or prior employers, but are a synthesis of conversations with data scientists, engineers, product managers and architects across industries.

**Hypothesis #1: Data Science initial models don’t scale or are too experimental to be used by internal or external customers.**

Projects often start here as companies hire on a few data scientists who build their models in Python or R, only to discover quickly that there is a difference in mindset between data scientists and engineers. In the short run this problem is often solved by having machine learning engineers or other software engineers take the code, rewrite it and follow standard dev-ops processes in order to scale and deploy the application. Given the stochastic nature of results, Quality Engineering also needs to scale to the task. During this transition period, business users (and/or their proxy product managers) can be left out of the process and the requirements or underlying data may change.

Organizationally, some companies take the next step of hiring engineers into the data science group to help the data scientists learn more about scaling for production and deployments. The goal with this approach is to alleviate the handoff process. The challenges are that this research/engineering organization can become siloed away from the rest of the production support workflow. “Data Scientists don’t wear pagers on call”.

**Hypothesis #2: Data science/ML models while brilliant and innovative don’t meet the business requirements or are too fragile to respond to change in the supporting data.**

At the recommendation of consulting groups, some companies make the decision that in order to foster innovation, “innovation teams” need to be isolated from the “non-digital” cultures which surround them. But while isolated innovation teams can lead to great opportunities for experimentation and those teams can learn and develop interesting solutions, when the resultant projects then need to be “pushed” to the market or internal customers, there is often minimal adoption. While the solution may meet the specific challenge, the experience for the user is often less than optimal. Lack of a less complex model to fall back upon if the data changes can also present a challenge. On the upside, the research can be published in academic journals read by other data scientists to further overall industry knowledge.

In response to this non-adoption problem, some innovation/data science teams may add product marketers to their organization to “promote” their work internally and to try to market their concepts to customers directly.

**Hypothesis #3: AI initiatives are driven by the company’s internal IT organizations and inherit “waterfall” challenges.**

As part of a “digital transformation”, some companies see AI as part of an overall data warehouse initiative or as part of an automation effort for customer management or marketing applications. The need for “labelled” (appropriately tagged) data in AI or Machine Learning means that companies will also need to have a fairly mature analytics and data capture infrastructure in place. While it may seem rational to approach AI and Machine Learning as part of an overall IT data project, without an accompanying experimental/prototyping initiative, AI projects can be buried as a consequence. Ironically, when the data is finally ready in the data pipelines, the customer needs may have changed completely (ex: optimizing around CD distribution while the company strategy moves to streaming).

**Hypothesis #4: Companies don’t have the patience for the time it takes to deliver on AI/ML projects.**

Given the uncertainty of success and timelines for many proposed AI/ML projects, they may die before they even have a chance to begin. Add to this the newness of the technology and the head-start dominance of Google, Amazon and Microsoft and the result is that non-direct consumer-oriented enterprise companies may talk AI, but start with Business Process Automation tools as their first foray and wait for things to settle (capturing data along the way for the future).

**Hypothesis #5: A lack of a “Product” approach to AI/ML projects is core to project failure and increased risk.**

The role of Product Manager/Owner in Agile software development is clear in software development. Product Managers work as part of a team including UX, Engineering, QA and Project Management. What seems to be missing in AI projects is this same “Product” mindset. Good Product Managers understand how to ask or find the highest value business questions. Experienced Product Managers are experts at managing the uncertainty of product delivery. Seasoned Analytics Product Managers understand where the data is missing or buried. So, the question of the day may not be “Where are all the data scientists we need?”, but rather “Where are all the AI Product Managers who know how to ask the right questions?”

**Summary:**

Fundamentally AI/ML projects will not succeed unless the same “Agile” “Lean” Product approach is taken up by technically savvy product managers to meet the challenges of risk, territory battles and failure to solve or answer the business questions. Data Scientists and Machine Learning Engineers need to be integral to product development teams. Much as “Design Thinking” brought UX on board to software development teams, so “AI thinking” needs to integrate AI research into product development. AI product managers need business executive support to guide the business value evaluation process and to balance technology/data science agendas.

While the shake-up continues in AI Cloud Platforms and while tooling is changing rapidly, companies who step up and train or hire AI Product Managers with the requisite technical or data skills and challenge them to find a business question to answer with a team of UX Designers, Data Scientists, Machine Learning Engineers, Software Engineers, coordinated by a project manager who understands and can communicate uncertainty rationally will be a long ways down the road to leverage AI to success.

Companies who already have tagged data streams like those in e-commerce and finance/payments have a head start and provide good models for others on how to scale, but it will be by asking the right questions and leveraging and scaling ML/NLP/AI to get the right answers that some of them will lead the pack over the next decades.
