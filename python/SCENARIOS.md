
## Scenario 1
You need a Python service which is tasked with starting/stopping VMs based on the number of documents existing in a firebase collection. It must ensure that 1 VM is running for every 3 documents in a collection. This means, if 3+ docs are added, 1 new VM should be started. If 3+ documents are removed, a process should be terminated. 

### Question: 
At a high level, how might you go about doing this?

### Required knowledge: 
- Python
- Threading, or maybe async/await?

### Potential notes:
- Watch the queue collection
- Keep track of current # procs
- start/stop procs when necessary to match queue length/3
