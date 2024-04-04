#include <iostream>
#include <string.h>
using namespace std;

int arr[1001]={0,};

int dp(int n){
    if(n==0||n==1||n==2||n==3) return arr[n];
    if(arr[n]==-1) return arr[n]=(arr[n-2]+arr[n-3])%10007;
    return arr[n];
    
}

int main() {
    int n;
    cin>>n;
    memset(arr,-1,sizeof(arr));
    arr[0]=0;
    arr[1]=0;
    arr[2]=1;
    arr[3]=1;

    cout<<dp(n);
    return 0;
}