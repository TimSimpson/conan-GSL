#include <gsl.h>

int main() {
    gsl::owner<int *> int_point = new int(256);
    const int exit_code = (*int_point == 256) ? 0 : 1;
    delete p;
    return exit_code;
}
