use bigint;
$max = 19293949596979899;
$n = sqrt($max) + 1;  # make sure this is odd
do { $n-=2 } until ($n*$n)=~/^1\d2\d3\d4\d5\d6\d7\d8\d9/; #pattern to match 1_2_3_ ... _9
 
print "Answer to PE206 = ",$n*10; #add the trailing zero
