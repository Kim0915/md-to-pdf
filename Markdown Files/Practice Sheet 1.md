
# USACO Bronze Level Practice Sheet 1

## Problem 1: Cow Coolers

#### Problem Description
Bessie the cow is hosting a summer party and wants to keep her drinks cool by placing them in coolers. She has N coolers labeled from 1 to N and M drinks labeled from 1 to M.
Each cooler can hold at most one drink, and each drink can be placed in at most one cooler. Bessie wants to minimize the maximum distance between any two drinks and asks for your help.
The distance between two drinks i and j, where i != j, is defined as |Pi - Pj|, where Pi and Pj are the positions of the coolers containing drinks i and j, respectively.
Given the positions of the coolers and drinks, determine the minimum possible maximum distance between any two drinks.

#### Input Specifications
The first line contains two space-separated integers, N and M (1 <= N, M <= 100). The next line contains N space-separated integers, denoting the positions of the coolers. The next line contains M space-separated integers, denoting the positions of the drinks.

#### Output Specifications
Output a single integer, the minimum possible maximum distance between any two drinks.
<div style="page-break-before:always"></div>
#### Example

##### Input
~~~console
5 3
2 4 6 8 10
1 7 9
~~~

##### Output
~~~console
2
~~~

##### Explanation
Bessie can place drink 1 in cooler 2, drink 2 in cooler 6, and drink 3 in cooler 9. The maximum distance between any two drinks is then |2-6| = |6-9| = 2.


<div style="page-break-before:always"></div>



## Problem 2: Cow's Winter

#### Problem Description
Bessie the cow is trying to figure out how much food she needs to buy for the upcoming winter. She has N types of food, labeled from 1 to N, and each type of food has a price and a nutritional value.
Bessie has a budget of B dollars and wants to maximize the total nutritional value of the food she buys while staying within her budget. Each type of food can be bought any number of times.
Given the budget, the prices, and the nutritional values of the N types of food, determine the maximum possible total nutritional value of the food Bessie can buy.

#### Input Specifications
The first line contains two space-separated integers, N and B (1 <= N, B <= 100). The next N lines each contain two space-separated integers, the price and the nutritional value of the i-th type of food, Pi and Vi (1 <= Pi, Vi <= 100).

#### Output Specifications
Output a single integer, the maximum possible total nutritional value of the food Bessie can buy.
<div style="page-break-before:always"></div>
#### Example

##### Input
~~~console
3 8
3 5
4 6
5 7
~~~

##### Output
~~~console
13
~~~

##### Explanation

Bessie can buy two units of the first type of food and one unit of the second type of food for a total cost of 3 * 2 + 4 = 10 dollars, which is within her budget of 8 dollars. The total nutritional value of the food she buys is 2 * 5 + 6 = 16, but she can only consume a maximum of 13 units of nutritional value, which is the maximum possible total nutritional value of the food she can buy.


<div style="page-break-before:always"></div>


## Problem 3: Hay Warehouse

#### Problem Description
Bessie the cow is storing her hay bales in a warehouse. The warehouse is a rectangular prism of dimensions L x W x H, and she has stacked N hay bales in the warehouse. Each hay bale has a length of L_i, a width of W_i, and a height of H_i. Bessie wants to know the minimum height she needs to set the roof of the warehouse at in order to fit all of the hay bales.
Assume that the hay bales are stacked without any gaps and without overlapping.

#### Input Specifications
The input consists of three lines. The first line contains three space-separated integers: L, W, and H (1 <= L, W, H <= 100), representing the dimensions of the warehouse. The second line contains a single integer N (1 <= N <= 100), representing the number of hay bales. The following N lines each contain three space-separated integers: L_i, W_i, and H_i (1 <= L_i, W_i, H_i <= 100), representing the dimensions of each hay bale.

#### Output Specifications
Output a single integer, the minimum height Bessie needs to set the roof of the warehouse at in order to fit all of the hay bales.
<div style="page-break-before:always"></div>
#### Example

##### Input
~~~console
10 10 10
3
7 7 7
6 6 6
5 5 5
~~~

##### Output
~~~console
18
~~~

##### Explanation
The warehouse has dimensions 10 x 10 x 10. Bessie has stacked three hay bales of dimensions 7 x 7 x 7, 6 x 6 x 6, and 5 x 5 x 5. The minimum height Bessie needs to set the roof of the warehouse at in order to fit all of the hay bales is 18.
