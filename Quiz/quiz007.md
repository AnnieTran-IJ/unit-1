# Quiz 007
Choose one of the flow diagrams on the whiteboard, create the trace table, code it, and upload the proof of work

## Paper Solution (Trace Table):
![image](https://github.com/user-attachments/assets/aad387e7-71b2-420e-a2ab-c8572536e3a3)
![image](https://github.com/user-attachments/assets/4f3a3b84-8ff5-4b62-a213-d5351561eca9)


## Code
```.py
def find_largest_number(N):
    if len(N) == 0:
        return None
    m = N[0]
    for i in N:
        if i > m:
            m = i
    return m

# Example usage
N = [-1, 3, 5, 10, 15]
output = find_largest_number(N)
print("Largest number:", output)
```
## Proof of work
![image](https://github.com/user-attachments/assets/df7f6f6c-935c-4b64-b4de-320a9ea3434b)


