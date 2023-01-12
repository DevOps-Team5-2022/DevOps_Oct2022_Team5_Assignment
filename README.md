# DevOps_Oct2022_Team5_Assignment
DevOps 2022 Assignment Repo for Team 5


### Requirements gathering flow
### Backlog issues creation flow
- Create a new issue (Task) with reasonable naming sense
- Include the label "Enhancement". Add Milestone related to issue eg. upload data
- Assign the issue to whoever will be completing or wants to complete the task. Refer to Trello if needed
- Add the description of what the issue is supposed to be
### Git usage strategy
### Change requirement strategy
### Deployment strategy
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
### Metrics for passing or failing
### Naming convention
Function: lower case with underscore for spaces. Eg. def hello_world
Variable: camel case, do not use short forms unless it is universal understanding. Give the variable adjective if possible.
