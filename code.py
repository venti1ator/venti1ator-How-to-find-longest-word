biglength=int(0)
topword=""
 
for i in range (5):
	word=input()
	if len(word) > biglength:
		biglength=len(word)
		topword=word
print("The longest word was '"+topword+"'")
	
