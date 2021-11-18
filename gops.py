def compute_next_num(c_num):
	i=1
	t = p_table[c_num][0]
	while(t in cards_played):
		t = p_table[c_num][i]
		i=i+1
	cards_played.append(t)
	return t

p_table = {'1':[2,3,1,4,5,6], '2':[4,2,3,1,5,6], '3':[5,4,3,2,1,6], '4':[5,3,1,6,2,4], '5':[6,4,2,1,5,3], '6':[6,2,3,1,4,5]}
cards_played=[]

for i in range(6):
	c_num = input("Current #:")
	play = compute_next_num(c_num)
	print("Play:{}".format(play))

