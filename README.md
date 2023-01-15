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
#### New Task/Enhancement to be done
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
#### Branches
1. main - to store code that is awaiting released or released already.
2. sprintBranch - To store code that is being developed for each sprint.
3. QABranch - Code that is written by QA
4. DevBranch - Code that is written by Dev.
#### Usage strategy
QA and Dev will push their code to their respective branches. If QA pushes code through, a CI will run to test QA's code and pull Dev's functions to be tested also, vice versa if Dev push first. In the event that the CI fails, notify the pusher if their code failed or notify Devs if function test failed, code does not enter branch if their own test fails. If Dev function test fails notify Devs. 

Once CI passes pull request from QA/Dev branch into sprint branch.

From Sprint branch at the end of every sprint, Tech Lead/Scrum Master will do a pull request into main branch where automatic tagging will happen. A CDelivery will be triggered and notify the team of the changes. Manual deployment(release) will be done and manual notifying of Owner and team is handled.
### Change requirement strategy
1. Leverage the Change Requirement Timeline which are our sprints. Before we change, make sure that everyone that is affected by the change know about it and to set and communicate goals to relate directly to the change of requirement.
2. Communicate the reason of why there is a need for change of requirements and to be truthful about why it has to be done. There should also be explaination in why this change would result in better end goal.
3. Monitoring and measuring of the change process, keeping a close eye on potential problems, and address any issues that might arise from it.
4. Testing changes in the product to avoid problems that might arise from it and to prevent poor user experience.
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
- To monitor progress, we will be using the "Number of lines of code" metric. 
- Lines of code in source (LOC) is the counting of the number of lines in the program.
- It will be used to track the estimate effort of the developers.
### Metrics for passing or failing
- To monitor the passing or failing of test cases, we will be using "Defects per test per push" metric.
- The number of test satisfied per push should increase over time.
- This ensures that the development of the program is functional.
### Naming convention
- Function: lower case with underscore for spaces. Eg. def hello_world
- Variable: camel case, do not use short forms unless it is universal understanding. Give the variable adjective if possible.
