We will solve this question by using the approach of a cartesian plane:

We will draw position in y axis and time in x axis. The slope will become the speed. If two lines (each line indicating a car) intersects, it means that that'll become a fleet. Once it becomes the fleet, the faster car will slow down to match the slower car's speed. We will create position speed pair and maintain a stack. We will sort the positions to see the realtime positions on the road initially. Then, iterating reverse order (because faster car will cross the car that's in the front and slow down, thus making it easier to iterate), we will append the time (target - pos/speed) in the stack and if the second top element's time to reach target is less than that of the top in the stack, it means that the former is faster than the latter and we'll pop the top from the stack, beacuse it'll become same as the second top element. Finally, return the length of the stack.

  ![image](https://github.com/therealaaryan/data-structures-algo./assets/51379599/b201bf1f-8985-4b63-b020-2bf0d2441e9c)
  ![image](https://github.com/therealaaryan/data-structures-algo./assets/51379599/02c19c4c-fe26-4de0-898d-44760980ced5)


Building the Intuition:

Understand the Problem: Start by thoroughly understanding the problem statement and the goals. In the "Car Fleet" problem, the goal is to determine how many car fleets will reach the target destination.

Identify Relationships: Notice that the problem involves considering the relationship between position, speed, and time. In a sense, each car is like a point on a graph with its position on the y-axis and time on the x-axis.

Explore Different Approaches: When a problem seems challenging, try to think outside the box. Explore different ways you can represent and analyze the given data. Consider if there's any geometrical interpretation that might help.

Connection to Slope and Intersection: Realize that if two cars intersect (i.e., they will be at the same position at the same time), they will form a fleet. The slope of the line connecting the point (position, time) for each car will represent its speed.

Maintaining a Stack: To keep track of potential fleets, you can use a stack. A stack is useful for maintaining the order of cars as you process them.

Signs for Similar Problems:

To recognize when this Cartesian plane approach might be applicable and for similar techniques, look for the following characteristics in the problem:

Intersections or Convergence: Problems where the interaction or convergence of two or more entities is important. This could involve cars, people, signals, etc.

Speed or Rate Consideration: Situations where the speed or rate of entities is relevant. It could be vehicles, moving objects, or processes.

Comparison and Ordering: Problems where you need to compare and order entities based on their properties, such as speed, time, or distance.

Optimization and Fleet Formation: Situations where you need to optimize the arrangement or formation of entities to achieve a certain goal. This could involve minimizing or maximizing something.

Time and Position: Problems where the relationship between time and position is crucial, and you can analyze them in a coordinate system.

Use of Stacks or Queues: Problems where a stack or queue can help maintain order or track certain properties as you process entities.
