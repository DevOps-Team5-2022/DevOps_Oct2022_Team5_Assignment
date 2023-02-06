# DevOps_Oct2022_Team5_Assignment
DevOps 2022 Assignment Repo for Team 5

### Team Roles & Responsibilies
|Role|Member|Role Responsibilities|
--- | --- | ---|
|Scrum Master & QA|Kevin|Organize the team, does SCRUM & Sprint documentation|
|Lead Developer|Elgin|Manages the code for the team, is the gatekeeper for releases|
|Quality Assurance|Samuel|Manages the system testing and overall completness of unit tests and automated testing|
|Developer|Tricia|Manages the overall development of the solution. Writes unit test cases|
|Developer|Jun Jie|Manages the overall development of the solution Writes unit test cases|

### Requirements gathering flow
Go through the project scope as a team. Identify areas which will require IT to develop. From the areas break it down to what are the technologies required and its dependencies. Once all is identified the team will generate user stories for the requirements and planning poker will start.
### Backlog issues creation flow
#### Enhancement to be done
1. Create a new issue (Task) with reasonable naming sense
2. Include the label "Enhancement". Add Milestone related to issue eg. upload data
3. Assign the issue to whoever will be completing or wants to complete the task. Refer to Trello if needed
4. Add the description of what the issue is supposed to be
#### New bug discovered
1. Create a new issue with reasonable naming sense
2. Include the "Bug"
3. Assign the issue to who "developed" the bug
4. If help is required assign tech lead to bug also.
### Git usage strategy
#### Dev Strat
1. Pull Dev Branch
2. Create a local branch of Dev Branch
3. Write code 
4. Push code to Dev Branch
#### QA Strat
1. Pull QA Branch
2. Create a local branch of QA Branch
3. Write code 
4. Push code to QA Branch
#### Scrum Master & Tech Lead
1. Pull all branches
2. Create local branch
3. Write code to respective branches
4. Push code
5. End of each sprint pull request from Sprint to Main. 
6. Create a tag
7. Create a release when UAT pass.
#### Branches
1. main - to store code that is awaiting released or released already.
2. sprintBranch - To store code that is being developed for each sprint.
3. QABranch - Code that is written by QA
4. DevBranch - Code that is written by Dev.
#### YAML strategy
CI seesaw effect will happen between QA and Dev where code is extracted from the opposite branch to test. If the tests are successful it will PR to Sprint Branch.
PR will run a CI to test the code again and notify the team that a new bunch of code is entering what branch.

### Change requirement strategy
1. Informing of the scrum master and the tech lead of the required changes of the requirements.
3. Leverage the Change Requirement Timeline which are our sprints. Before we change, make sure that everyone that is affected by the change know about it and to set and communicate goals to relate directly to the change of requirement.
4. After discussion, scrum master and tech lead must approve of the changes of the requirements before proceeding with the changes.

### Deployment strategy
#### Canary Deployments
Canary Deployments are those that new instances is tested before all the old instances are replaced. If the readiness check never succeeeds, the canary instance is removed and the deployment configuration will be automatically cancelled and goes back to the old instance. The readiness check is part of the application code where automatic testing will be done to check if the new instance is ready to be used.
### Delivery strategy
1. A new branch of the main branch will be created every sprint, where all the user stories/tasks for that sprint has to be done before merging back into Main branch
2. 2 sub branches of this **Sprint Branch** will be created, **Dev Branch** and **QA Branch**
3. Developers & QA will clone their respective branches (*Dev Branch* for developers and *QA Branch* for QA), and code/complete the tasks assign to them
4. Once the developers or QA have finished all their tasks, they will trigger a Pull Request on their respective branch to merge it back into the **Sprint Branch**. This will trigger a **CI** to run.
   - If the **CI** fails, the Pull Request will not go through and the Team will be notified to fix it.
6. The Pull Request will *only* go through if it passes the **CI**.
7. At the end of the sprint or once the Team is satisfied with everything in the **Sprint Branch**, a Pull Request will be triggered to merge it with **Main Branch**. This will also trigger a **CI**.
   - If the **CI** fails, the Pull Request will not go through and the Team will be notified to fix it.
8. Once the **CI** passes, it will automatically tag the new version of code in Main.
9. Once everyone in the Team is satisfied, the **Scrum Master** will manually do a release and notify the client
### Communications strategy
- Microsoft Teams
- Telegram

The team's communication strategy consists mainly of **Microsoft Teams** and **Telegram**

For **important** team discussions, the team will communicate through voice call on **Microsoft Teams**. The scrum master will share his/her screen during the team discussion so that the team can get a better understanding on what the scrum master is discussing.

Communication outside of sprint planning & retrospective will be done through text messages via **Telegram**. **Telegram** will be used to schedule team meetings/discussions and generally any small tdiscussions that aren't big enough to warrant a team discussion on **Microsoft Teams**
### Monitoring strategy
- To monitor progress, we will be gauging our metrics for passing or failing with a threshold.
- Threshold will be a maximum of 3 failures and the end of each sprint.
- Scrum master will review at every sprint meeting, if threshold exceeds, team is to communicate through Microsoft Teams meeting to decide on a way to decrease the number of failing test cases.

### Metrics for passing or failing
- To monitor the passing or failing of test cases, we will be using "Defects per test per push" metric.
- The number of test satisfied per push should increase over time.
- This ensures that the development of the program is functional.
- Developers & QA to track the number of failures and passes when running their test cases each sprint.
- Scrum Master to review at every sprint meeting.

### Naming convention
- Function: lower case with underscore for spaces. Eg. def hello_world
- Variable: camel case, do not use short forms unless it is universal understanding. Give the variable adjective if possible.
