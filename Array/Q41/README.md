Problem Statement

There are n cities and m one-directional roads connecting city A[i] to city B[i]. We are in the panner-making business. Each city has its own price of paneer. You can buy or sell paneer in the city i for vali rupees. You have to buy paneer from some city u and sell the paneer in another city v. The profit you make is calculated as the selling price minus buying price. Return an integer denoting the maximum profit you can make. NOTE: In all, it is mandatory to buy only 1 paneer, and it is mandatory to sell that paneer in some other city that can be traveled from it.

Input Format

The first line contains n the number of cities.
The next n lines contain the elements of the array val.
The next line contains an integer m.
The next m lines contain the array of elements A.
The next line again contains the integer m.
The next m lines contain the array of elements B.
Constraints

2 <= n <= 105
1 <= m <= 105
1 <= Ai < Bi <= n
Output Format

Return an integer denoting the maximum profit possible.
