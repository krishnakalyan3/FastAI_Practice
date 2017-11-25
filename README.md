# Course Notes : FastAI


#### AWS

N. Virginia FastAI ami-c6ac1cbc

```
ssh -i krishna.pem ubuntu@54.221.107.220 -L8889:localhost:8889
```

#### Notes

##### Step 1
1. Look at the images
2. See the x, y ranges and channels
3. Histogram of Rowsizes
4. Histogram of Columnsizes

##### Step 2
1. Enable data augmentation, and precompute=True
2. Use lr_find() to find highest learning rate where loss is still clearly improving
3. Fit the model with the best learning rate with 3 epochs
4. plot LR


##### Step 3
1. Train the last layer with precompute = false, epochs = 3 and cycle_len=1
2. Train last layer with data augmentation, recompute=False 2-3 epochs with cycle_len=1
3. Plot the LR

##### Step 2
1. Unfreeze all layers
2. Set earlier layers to 3x-10x lower learning rate than next higher layer
3. Train full network with cycle_mult=2 until over-fitting

Use lr_find() again

Use lr_find() to find highest learning rate where loss is still clearly improving
Train last layer with data augmentation (i.e. precompute=False) for 2-3 epochs with cycle_len=1
Unfreeze all layers
Set earlier layers to 3x-10x lower learning rate than next higher layer
Train full network with cycle_mult=2 until over-fitting