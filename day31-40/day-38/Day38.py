#Day 38


# !pip install wandb
#
# !wandb login


import pandas as pd
import wandb


areas = [6.7 , 4.6 , 3.5 , 5.5]
prices = [9.1 , 5.9 , 4.6 , 6.7]

dataset = pd.DataFrame ({
'areas': areas ,
'prices': prices
 })

# forward
def predict (x , w , b ) :
  return x * w + b
# compute gradient
def gradient ( y_hat , y , x ) :
  dw = 2* x *( y_hat - y )
  db = 2*( y_hat - y )
  return ( dw , db )

 # update weights
def update_weight (w , b , lr , dw , db ) :
  w_new = w - lr * dw
  b_new = b - lr * db
  return ( w_new , b_new )

# init weights
b = 0.04
w = -0.34
lr = 0.01
epochs = 10

# init project wandb
wandb . init (
# Set the project where this run will be logged
project ="demo - linear - regression ",
config ={
"learning_rate ": lr ,
"epochs ": epochs ,
} ,
)
wandb . run . log ({" Dataset " : wandb . Table ( dataframe = dataset ) })

X_train = dataset['areas']
Y_train = dataset['prices']
N = len ( X_train )
# parameter
losses = [] # for debug

for epoch in range ( epochs ) :
  for i in range ( N ) :
    # get a sample
    x = X_train [ i ]
    y = Y_train [ i ]
    # predict y_hat
    y_hat = predict (x , w , b )
    # compute loss
    loss = ( y_hat - y ) *( y_hat - y ) / 2.0
    # tracking loss with WandB
    wandb . log ({" loss ": loss })
    # compute gradient
    ( dw , db ) = gradient ( y_hat , y , x )
    # update weights
    (w , b ) = update_weight (w , b , lr , dw , db )
# Mark a run as finished , and finish uploading all data .
wandb . finish ()

# Load the dataset
data = pd.read_csv('/content/drive/MyDrive/Colab Notebooks/Day38/advertising.csv')

# Split the data into features and target
X = data[['TV', 'Radio', 'Newspaper']]
y = data['Sales']

# Define the model functions
def predict(X, w1, w2, w3, b):
    return X['TV'] * w1 + X['Radio'] * w2 + X['Newspaper'] * w3 + b

def gradient(y_hat, y, X):
    dw1 = 2 * X['TV'] * (y_hat - y)
    dw2 = 2 * X['Radio'] * (y_hat - y)
    dw3 = 2 * X['Newspaper'] * (y_hat - y)
    db = 2 * (y_hat - y)
    return (dw1, dw2, dw3, db)

def update_weights(w1, w2, w3, b, lr, dw1, dw2, dw3, db):
    w1_new = w1 - lr * dw1
    w2_new = w2 - lr * dw2
    w3_new = w3 - lr * dw3
    b_new = b - lr * db
    return (w1_new, w2_new, w3_new, b_new)

# Initialize weights and hyperparameters
w1, w2, w3 = 0, 0, 0
b = 1
lr = 0.01
epochs = 1000

# Initialize WandB project
wandb.init(project="linear-regression-advertising",
           config={"learning_rate": lr, "epochs": epochs})

# Log the dataset
wandb.run.log({"Dataset": wandb.Table(dataframe=data)})

# Training loop
losses = []
for epoch in range(epochs):
    # For each epoch
    for i in range(len(X)):
        # Get a sample
        x = X.iloc[i]
        y_true = y.iloc[i]

        # Predict y_hat
        y_hat = predict(x, w1, w2, w3, b)

        # Compute loss
        loss = (y_hat - y_true) ** 2 / 2.0

        # Log the loss with WandB
        wandb.log({"loss": loss})

        # Compute gradients
        (dw1, dw2, dw3, db) = gradient(y_hat, y_true, x)

        # Update weights
        (w1, w2, w3, b) = update_weights(w1, w2, w3, b, lr, dw1, dw2, dw3, db)

# Mark the run as finished
wandb.finish()