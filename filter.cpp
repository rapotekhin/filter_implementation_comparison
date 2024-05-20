#include <iostream>
#include <vector>

extern "C" {
    void filter(int* arr, bool* idxs, int* out, int size, int& out_size) {
        out_size = 0;
        for (int i = 0; i < size; ++i) {
            if (idxs[i]) {
                out[out_size++] = arr[i];
            }
        }
    }
}