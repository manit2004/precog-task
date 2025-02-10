For Task 1:

To generate use task_1-datagen.py. We are generating 100 random words and per word we are generating 5 easy images (5 fonts) and then 45 hard images using 2 fonts shown in the docs (present in /fonts). Texts present in the images vary from 4-8 characters and are of size 128*32. (exponents of 2 are used)

Data for Task 1 are present in task-1_data folder.

Now after running task-1-cnn.ipynb with a train-test split of 80 and 20% having batch size is 32, after 10 epochs we get test accuracy of 97.34

For Task 2:

To generate data for easy set I am using dataset_0.py and for hard set dataset_1.py. I am generating 30000 easy images that are stored in dataset_0 folder and 35000 hard images in dataset_1 folder. In the task-2.ipynb I am implementing a CRNN model with CTC loss. My batch size is 20 and epoch is 30. After running for 30 epochs I am getting 95.96% character accuracy on easy and the model is saved as task-2_data_0.pth and on hard set I am getting 92.84% accuracy and the model is saved as task-2_data_1.pth