#include <iostream>
using namespace std;

int arr[101][101]={0,};
int dp[101][101]={0,};
int do_dp(int r,int c){
    if((r==1&&c==1)||r==0||c==0) return dp[r][c];

    return dp[r][c]=max(do_dp(r-1,c),do_dp(r,c-1))+arr[r][c];
}

int main() {
    int n;
    cin>>n;
    for(int r=1;r<n+1;r++){
        for(int c=1;c<n+1;c++){
            cin>>arr[r][c];
        }
    }
    dp[1][1]=arr[1][1];
    cout<<do_dp(n,n);
    return 0;
}