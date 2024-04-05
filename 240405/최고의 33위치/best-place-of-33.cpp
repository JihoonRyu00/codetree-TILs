#include <iostream>
using namespace std;

int arr[21][21]={0,};

int max_coin=0;

int solve(int n){
    int temp=0;
    for(int r=1;r<n-1;r++){
        for(int c=1;c<n-1;c++){
            for(int rr=r;rr<r+3;rr++){
                for(int cc=c;cc<c+3;cc++){
                    temp+=arr[rr][cc];
                }
            }
            max_coin=max(max_coin,temp);
            temp=0;
        }
    }
    return max_coin;
}

int main() {
    int n;
    cin>>n;
    for(int r=1;r<n+1;r++){
        for(int c=1;c<n+1;c++){
            cin>>arr[r][c];
        }
    }
    cout<<solve(n);
    return 0;
}