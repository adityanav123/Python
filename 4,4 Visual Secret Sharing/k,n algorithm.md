# ALGORITHM - (k,n) secret sharing


Step - 1: For every pixel - 'p' of the original image.

Step - 2: For p, determine its pixel value.
		-> 0 / 255
Step - 3: Color of p - 
	3.a BLACK
		-> Select block for the black pixel in codebook.
		-> randomly select one row from the selected block in the codeblock.
	3.b WHITE
		->  Randomly select one block from the white pixel in codebook.
		-> randomly select one row from the selected block.
	the selected row is to be assigned to vector V.

Step - 4: V = [v1, v2, v3, v4] - 4 shares.
		Share1=v1 Share2=v2 Share3=v3 Share4=v4.

Step - 5: repeat step 1 to 4 for all the pixels.


RECONSTRUCTING THE ORIGINAL IMAGE. >>

(2, 4): sharei XOR sharej ; where i != j and 1 <= i,j <= 4
(3, 4): sharei XOR sharej XOR sharek ; where i != j != k and 1 <= i,j,k <= 4
(4, 4): share1 XOR share2 XOR share3 XOR share4
