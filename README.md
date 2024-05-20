
# Filter Implementation Comparison

This project evaluates the performance and correctness of filter functions implemented in C, C++, and Python, interfacing C and C++ through Python using the `ctypes` library. The goal is to compare how each implementation handles filtering operations, both in terms of speed and output accuracy.

## Prerequisites

- **GCC**: For compiling C and C++ code.
- **Python**: Version 3.6 or newer.
- **NumPy**: Required for array operations in Python.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Compiling the Code

1. **C Implementation**

   Navigate to the project directory and compile the C code using:
   ```bash
   gcc -O3 -Wall -shared -std=c11 -fPIC filter.c -o libfilter_c.so
   ```

2. **C++ Implementation**

   Compile the C++ code using:
   ```bash
   g++ -O3 -Wall -shared -std=c++11 -fPIC filter.cpp -o libfilter_cpp.so
   ```

### Installation

Install the necessary Python packages using pip:

```bash
pip install numpy
```

### Running the Tests

Execute the script to compare performance and verify the correctness of the outputs:

```bash
python main.py
```

## Files

- `filter.c`: Contains the C implementation of the filter function.
- `filter.cpp`: Contains the C++ implementation of the filter function.
- `main.py`: Python script to test and compare the C and C++ implementations.
- `README.md`: Documentation for setting up and running the project.

## Expected Outputs

Upon running the Python script, you will see:

- Timing results for each implementation (C, C++, and Python).
- Validation results checking if all implementations produce identical results.

### Sample Output

```plaintext
C++ version: Mean = 3.372 ms, Std Dev = 0.125248 ms
C version: Mean = 3.125 ms, Std Dev = 0.045240 ms
Python version: Mean = 4.437 ms, Std Dev = 0.042556 ms
----------------------------------------
Comparison between C++ and C outputs: identical
Comparison between C++ and Python outputs: identical
Comparison between C and Python outputs: identical
All implementations produce identical results.
```

## Contributing

Contributions to improve the project are welcome. Feel free to fork this repository and propose changes through pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE) file for details.
