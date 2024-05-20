#include <stddef.h>

void filter(const int *arr, const int *indx, int *out, size_t size, size_t *out_size) {
    *out_size = 0;
    for (size_t i = 0; i < size; ++i) {
        if (indx[i]) {
            out[(*out_size)++] = arr[i];
        }
    }
}