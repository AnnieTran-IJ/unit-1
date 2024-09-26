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
  * The users can perform CRUD operations (Create, Read, Update, Delete): view the stored list of passwords, create and add new passwords, update current passwords, or delete passwords (confirmation needed).
  * Passwords will be securely encrypted when stored (using alphabet rotation).
  * The password manager feature will automatically exit after 30 seconds of inactivity to prevent unauthorized access.
  * Save passwords permanently and securely.
#### IV. Others: 
 * The terminal is where users interact with the program.
## Criterion B: Design
### System Diagram
![2025  Project Unit1](https://github.com/user-attachments/assets/e5085606-4396-4691-8c1b-2ab0e40f1103)

**Fig 1.** System Diagram showing the minimal requirement for the hardware and software used for
the proposed solution and subfiles of each program feature. The lock indicates encryption.
### Flow diagrams for algorithms
![Algorithm Diagram 1](https://github.com/user-attachments/assets/925f0b85-1473-4178-98fb-717a621ff26b)
![Algorithm Diagram 2](https://github.com/user-attachments/assets/51486495-dba4-4b26-8200-bfdd0cddfafe)
![Algorithm Diagram 3](https://github.com/user-attachments/assets/0270ef51-cff1-431e-b81b-493c30057ce4)

**Fig ...** Flow diagrams of the top 3 notable functions within the entirety of the program [Link](https://www.figma.com/design/ugJAQwl7TcaKELyPff0Pni/Project-1-Flowchart-of-all-Sorts-%7C-Computer-Science?node-id=0-1&t=8g2uwhpa2hEhhKp9-1)).
### Data storage
![image](https://github.com/user-attachments/assets/b745565b-9535-47f7-8622-ca3b1754a6aa)
**Fig ...** Screenshot of how operational files are stored in the local databases.
### Sketches of the application (wireframe diagrams)
![Frame 1](https://github.com/user-attachments/assets/9ce6c9d5-551a-4e76-8a74-e1ac8c345960)
**Fig ...** UI Wireframe of the application from front (to-do list program) to back (password management) features. (Click on the picture to zoom in, [Link](https://www.figma.com/design/ugJAQwl7TcaKELyPff0Pni/Project-1-Flowchart-of-all-Sorts-%7C-Computer-Science?node-id=0-1&t=8g2uwhpa2hEhhKp9-1))
### Test plan

## Record of Tasks
| Task Number | Planned Action              | Planned Outcome                                                 | Time Estimated | Target Completion Date | Criterion |
|-------------|-----------------------------|-----------------------------------------------------------------|----------------|------------------------|-----------|
| 1           | Consulting with the client about the success criteria and their expectations of the project outcome. | Create a detailed list of requirements and a basic outline of the program. | 25 min | Sep 12 | A |
| 2           | Develop the welcome interface to default mode|  Make sure it's short, concise and there is validation for the user's input.| 10 mins| Sep 19|C|
| 3           | Design and complete system diagram | Create a diagram of minimal requirements for the program and the meaning of the symbol.|10 mins|Sep 16|A|          |
| 4           | Create the first sketch of the application flow and the system diagram |Use simplified blocks with detailed annotation for each feature. |20 mins|Sep 17|B|
|             |                             |                                                                 |                |                        |           |
|             |                             |                                                                 |                |                        |           |

## Criterion C: Development 
