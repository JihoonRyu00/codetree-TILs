#include <iostream>

int main() {
    int a=5;
    int b=6;
    int c=7;
    a=b=c;
    std::cout<<a<<" "<<b<<" "<<c;
    return 0;
}