#include <iostream>

int main() {
    int a=2;
    int b=5;
    int temp=b;
    b=a;
    a=temp;
    std::cout<<a<<"\n"<<b;
    return 0;
}