#include <iostream>
using namespace std;

int arr[46]={0,};

int fib(int n){
    if(n==0) return arr[0]=0;
    else if(n==1) return arr[1]=1;
    else if(n==2) return arr[2]=1;
    else{
        if(arr[n]==0){
            return arr[n]=fib(n-1)+fib(n-2);
        }
        else return arr[n];
    }
}

int main() {
    int N;
    cin>> N;
    cout<<fib(N);
    return 0;
}