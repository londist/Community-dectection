# Community-dectection

In order to detect communities, we need to calculate the similarity between any pair of users. In this homework, similarity is measured by the number of common followees for the given pair of users. The following figure illustrates the process.  

The set of followees of A is  {B, C, E} and set of followees of B is {A, C, E}.  There are 2 common followees between A and B (i.e.  C and E). The  similarity between A and B is therefore  2. 

The format of the data file is as follows (different followers separated by space): 

followee_1_id:follower_1_id follower_2_id follower_3_id …. 
followee_2_id:follower_1_id follower_6_id follower_7_id ….

For example, in the above figure, the data is represented as: A:B D B:A C:A B E E:A B C 
The output of the community detection is that for EVERY user, we want to know the TOP K most similar persons. The output format should be (different similar persons separated by space): 
User_1:Similiar_Person_1 Similiar_Person_2 … Similiar_Person_K 
User_2:Similiar_Person_1 Similiar_Person_2 … Similiar_Person_K

 I used mapreduce twice. I only did a medium data set 
test, but theoretically big data sets are also possible. Since it is a bonus, 
I want to save some money. 
 
The first time 
Input format：followee_1_id:follower_1_id follower_2_id follower_3_id 
map : Pair the followers pairwise and enter a format like A-B 1. It 
indicates that A and B have a common followee. 
reduce : Add the value of the same key together (similar to wordcount). 
Then get the output of A-B 4, indicating that A and B have 4 common followee 

The second time 
map : Separate the A-B 4 into A B 4 and B A 4 
reduce : Combine the values of the same key into a list and sort them 
in reverse order. Then the output format is key: value1 value1. Just like 
User_2:Similiar_Person_1 Similiar_Person_2 ... Similiar_Person_K 
