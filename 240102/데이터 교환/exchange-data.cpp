#include <iostream>

int main() {
    int a=5;
    int b=6;
    int c=7;
    int temp=c;
    c=b;
    b=a;
    a=temp;
    std::cout<<a<<"\n"<<b<<"\n"<<c;
    return 0;
}