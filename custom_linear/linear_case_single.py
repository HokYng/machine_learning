#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Author  :   Hyney
@Software:   PyCharm
@File    :   linear_case_multi.py
@Time    :   2021/3/12 20:21
@Desc    :   单变量数据线性回归
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from custom_linear.linear import LinearRegression


data = pd.read_csv('../data/world-happiness-report-2017.csv')

# 得到训练和测试数据
train_data = data.sample(frac=0.8)
test_data = data.drop(train_data.index)

input_param_name = 'Economy..GDP.per.Capita.'
output_param_name = 'Happiness.Score'

x_train = train_data[[input_param_name]].values
y_train = train_data[[output_param_name]].values

x_test = test_data[input_param_name].values
y_test = test_data[output_param_name].values

plt.scatter(x_train, y_train, label='Train data')
plt.scatter(x_test, y_test, label='test data')
plt.xlabel(input_param_name)
plt.ylabel(output_param_name)
plt.title('Happy')
plt.legend()
plt.show()

num_iterations = 500
learning_rate = 0.01

linear_regression = LinearRegression(x_train, y_train, eta=learning_rate)
theta, all_loss = linear_regression.train()

print(theta)
print ('开始时的损失：', all_loss[0])
print ('训练后的损失：', all_loss[-1])

plt.plot(range(num_iterations), all_loss)
plt.xlabel('Iter')
plt.ylabel('cost')
plt.title('GD')
plt.show()

predictions_num = 100
x_predictions = np.linspace(x_train.min(), x_train.max(), predictions_num).reshape(predictions_num, 1)
y_predictions = linear_regression.predict(x_predictions)

plt.scatter(x_train, y_train, label='Train data')
plt.scatter(x_test, y_test, label='test data')
plt.plot(x_predictions, y_predictions, 'r', label='Prediction')
plt.xlabel(input_param_name)
plt.ylabel(output_param_name)
plt.title('Happy')
plt.legend()
plt.show()