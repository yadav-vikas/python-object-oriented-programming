A queue is a data structure which contains an ordered set of data.

Queues provide three methods for interaction:

Enqueue - adds data to the “back” or end of the queue
Dequeue - provides and removes data from the “front” or beginning of the queue
Peek - reveals data from the “front” of the queue without removing it

This data structure mimics a physical queue of objects like a line of people buying movie tickets. Each person has a name (the data). The first person to enqueue, 
or get into line, is both at the front and back of the line. As each new person enqueues, they become the new back of the line.

When the cashier serves someone, they begin at the front of the line (or people would get very mad!). 
Each person served is dequeued from the front of the line, they purchase a ticket and leave.

If they just want to know who is next in line, they can peek and get their name without removing them from the queue.

The first person in the queue is the first to be served. Queues are a First In, First Out or FIFO structure.

##Implementation

Queues can be implemented using a linked list as the underlying data structure.
The front of the queue is equivalent to the head node of a linked list and the back of the queue is equivalent to the tail node.
