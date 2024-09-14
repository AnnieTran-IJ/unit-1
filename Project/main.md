# Project Unit 1

## Criterion A: Planning
### Problem definition: 
My client is a vacation home management company, **Elite Haven Management**, located in Karuizawa, a town popular with tourists. The company is responsible for overseeing and maintaining multiple vacation homes in the area. Most of their customers, who are vacation home owners, belong to the upper-middle class or the high-working class. Consequently, they have high expectations for the maintenance and management of their properties. The company has a fixed group of employees, including property managers, maintenance staff, and temporary workers, who are responsible for managing specific sets of houses. These employees often need to access confidential information, such as security system passwords, Wi-Fi networks, private customer accounts, and private itineraries. It's essential that this sensitive information be handled discreetly. As the company expands to manage more houses during the holiday seasons, the size of their databases also grows. Currently, all of the company's employees have access to the same database, which poses a security risk. Therefore, the company has a need to **create an updated management program for their database.**

### Proposed solution: 
Thus, I proposed to develop a custom-built, multi-functional tool for the company. It serves as both a task-tracking application and, upon entering the designated code, transitions into a basic password manager. This program enables authorized employees of each house within the organization to securely access passwords without attracting unnecessary attention or compromising security.
### Success Criteria
#### I. Task Tracking Mode (Default Mode):
  * The users can input new tasks, mark tasks as done, and view the total list of tasks
#### II. Secret Code for Switching Modes:
  * When the user enters the secret code (e.g., open123), the program will switch from task tracking to password manager mode.
  * The program will automatically exit after the third incorrect attempt.
  * No visible indication that the password manager exists unless the correct code is entered.
#### III. Password Manager Mode (Secure Mode):
  * The users can view the total list of passwords, create new passwords, update current passwords, or delete passwords (confirmation needed).
  * Passwords will be securely encrypted when stored (using alphabet rotation).
  * The password manager feature will automatically exit after 30 seconds of inactivity to prevent unauthorized access.
#### IV. Others: 
## Criterion B: Design
### System Diagram
### Flow diagrams for algorithms
### Data storage
### Sketches of the application (wireframe diagrams)

### Test plan

## Record of Tasks
| Task Number | Planned Action              | Planned Outcome                                                 | Time Estimated | Target Completion Date | Criterion |
|-------------|-----------------------------|-----------------------------------------------------------------|----------------|------------------------|-----------|
| 1           | Consulting with the client about the success criteria and their expectations of the project outcome. | Create a detailed list of requirements and basic outline of the program. | 25 min | Sep 12 | A |
| 2           | Develop the welcome interface to default mode|  Make sure it's short, concise and there is validation for the user's input| 10 mins| Sep 19        |
|             |                             |                                                                 |                |                        |           |
|             |                             |                                                                 |                |                        |           |
|             |                             |                                                                 |                |                        |           |
|             |                             |                                                                 |                |                        |           |

## Criterion C: Development 
