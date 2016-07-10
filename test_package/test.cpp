#include <gsl.h>

int main() {
    gsl::owner<int *> owned_integer = new int(256);
    const int exit_code = (*owned_integer == 256) ? 0 : 1;
    delete owned_integer;
    return exit_code;
}
