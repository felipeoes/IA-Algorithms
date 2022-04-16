from file_manager import FileManager
from perceptron import Perceptron
import random

file_manager = FileManager("data/problemAND.csv")
df_AND = file_manager.read_csv(
    cols_names=["expression1", "expression2", "result"])
X, y = file_manager.extract_X_y(df_AND)

print(f"X: {X} \n")
print(f"y: {y} \n")


weights = {
    col_num: random.random() for col_num in range(len(df_AND.columns) - 1)
}

bias = random.random()

perceptron = Perceptron(weights, bias)

learning_rates = [0.01, 0.05, 0.1]
learning_rate = random.choice(learning_rates)

accuracy = perceptron.train(X, y, epochs=50, learning_rate=learning_rate)
print("Mean accuracy of model: ", accuracy)

params_dict = {"weights": perceptron.weights,
               "bias": perceptron.bias, "learning_rate": learning_rate}
print(f"Params: {params_dict}")
