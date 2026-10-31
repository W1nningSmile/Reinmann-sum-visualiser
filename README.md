# Riemann Sum Visualizer

A small Python program I wrote in early 2026 while taking Calculus 2 to better understand how integrals worked. (Uploaded to GitHub later)

## What it does

- Approximates the area under a function between two bounds using a **right-endpoint Riemann sum**
- Uses 20,000 subintervals by default, so the approximation is very close to the true value
- Plots the function with the area under the curve shaded, and prints the computed area

By default it integrates sin(x) from -100 to 100. The true value of that integral is 0 but the program can only closely approximate the answer

## How it works

The interval [x1, x2] is split into `n` evenly spaced points. For each point, the program multiplies the width of the step by the function value at the right edge, then adds everything up:

```
area ≈ Σ f(xᵢ) · (xᵢ − xᵢ₋₁)
```

As `n` gets larger, the sum becomes more accurate, which is the core idea behind the definite integral.

## Requirements

- Python 3
- NumPy
- Matplotlib


To try different bounds or a different number of rectangles, edit the last two lines:

```python
test = Integration(-100, 100, n=20000)
test.graphing()
```

To integrate a different function, change the body of `fast_formula(x)`, for example `return x**2`.

## What I learned

- How Riemann sums converge to the integral as the number of rectangles increases
- Using NumPy for vectorized math and Matplotlib for visualizing it

## Possible improvements

- Left-endpoint, midpoint, and trapezoid options
- Letting the user pass in a function instead of editing the source
- Make the program change the value of `n` to find a good balance between accuracy and computation time
