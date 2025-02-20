# Efficient Frontier Simulation

This repository presents a simulation of the efficient frontier inspired by the Modern Portfolio Theory developed by Harry Markowitz. After learning that diversifying a portfolio with a mix of equities and bonds helps balance risk and return, I decided to explore this concept further by replicating it in Python.

## Background

Modern Portfolio Theory proposes that investors can optimize their portfolios by diversifying across various assets to achieve the best trade-off between return and risk. The goal is to construct a portfolio that lies close to the **efficient frontier**, where no other portfolio offers a higher return for the same level of risk, or a lower risk for the same return.

## Tools Used

- **NumPy**  
  A fundamental library for numerical computations in Python. It is used to generate data, compute means, covariances, and perform essential matrix operations required for simulating different portfolios.

- **Matplotlib**  
  A powerful plotting library used for creating visualizations. In this project, it is employed to plot the efficient frontier and to highlight optimal portfolios (for example, the portfolio with the highest Sharpe ratio).

## How to Use

Run the provided Python script to generate a simulation of various portfolios and visualize the efficient frontier. You can modify the code to use your own data (number of simulated portfolios, assets, observations)and further explore portfolio optimization strategies.
