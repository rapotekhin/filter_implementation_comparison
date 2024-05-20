import ctypes
import numpy as np
import timeit

# Load the C++ library
lib_cpp = ctypes.CDLL('./libfilter_cpp.so')
filter_cpp = lib_cpp.filter
filter_cpp.restype = None
filter_cpp.argtypes = [np.ctypeslib.ndpointer(dtype=np.int32),  # arr
                   np.ctypeslib.ndpointer(dtype=bool),   # idxs
                   np.ctypeslib.ndpointer(dtype=np.int32),  # out
                   ctypes.c_int,                            # size
                   ctypes.POINTER(ctypes.c_int)]            # out_size

# Load the shared library
lib_c = ctypes.CDLL('./libfilter_c.so')
filter_c = lib_c.filter
filter_c.restype = None
filter_c.argtypes = [
    np.ctypeslib.ndpointer(dtype=np.int32, ndim=1),
    np.ctypeslib.ndpointer(dtype=np.int32, ndim=1),
    np.ctypeslib.ndpointer(dtype=np.int32, ndim=1),
    ctypes.c_size_t,
    ctypes.POINTER(ctypes.c_size_t)            # Adjusted to c_size_t
]

# Pre-create arrays
arr = np.random.randint(-1000, 1000, (1024 * 1024,)).astype(np.int32)
indx = np.random.choice([True, False], size=(1024 * 1024,))
indx_c = indx.astype(np.int32)  # Ensure indx_c is created correctly from indx
out = np.empty_like(arr)
out_size_cpp = ctypes.c_int()
out_size_c = ctypes.c_size_t()  # Adjusted to c_size_t

def cpp_filter():
    filter_cpp(arr, indx, out, arr.size, ctypes.byref(out_size_cpp))
    return out[:out_size_cpp.value]

def c_filter():
    filter_c(arr, indx_c, out, arr.size, ctypes.byref(out_size_c))
    return out[:out_size_c.value]

def python_filter():
    return arr[indx]

# Collect multiple timing results
cpp_times = [timeit.timeit(cpp_filter, number=1) for _ in range(500)]
c_times = [timeit.timeit(c_filter, number=1) for _ in range(500)]
python_times = [timeit.timeit(python_filter, number=1) for _ in range(500)]

# Calculate mean and standard deviation using numpy
cpp_mean = np.mean(cpp_times)
cpp_std = np.std(cpp_times)
c_mean = np.mean(c_times)
c_std = np.std(c_times)
python_mean = np.mean(python_times)
python_std = np.std(python_times)

print(f"C++ version: Mean = {1000*cpp_mean:.3f} ms, Std Dev = {1000*cpp_std:.6f} ms")
print(f"C version: Mean = {1000*c_mean:.3f} ms, Std Dev = {1000*c_std:.6f} ms")
print(f"Python version: Mean = {1000*python_mean:.3f} ms, Std Dev = {1000*python_std:.6f} ms")

print("--"*20)
# Assuming the following functions are correctly defined and available
# cpp_filter, c_filter, python_filter

# Running the functions
output_cpp = cpp_filter()
output_c = c_filter()
output_python = python_filter()

# Convert to numpy arrays if not already (for ease of comparison)
output_cpp = np.array(output_cpp)
output_c = np.array(output_c)
output_python = np.array(output_python)

# Checking if all outputs are identical
compare_cpp_c = np.array_equal(output_cpp, output_c)
compare_cpp_python = np.array_equal(output_cpp, output_python)
compare_c_python = np.array_equal(output_c, output_python)

# Print the results
print(f"Comparison between C++ and C outputs: {'identical' if compare_cpp_c else 'different'}")
print(f"Comparison between C++ and Python outputs: {'identical' if compare_cpp_python else 'different'}")
print(f"Comparison between C and Python outputs: {'identical' if compare_c_python else 'different'}")

# If all are true, you can safely assume the implementations are consistent
if compare_cpp_c and compare_cpp_python and compare_c_python:
    print("All implementations produce identical results.")
else:
    print("There are discrepancies between the implementations.")