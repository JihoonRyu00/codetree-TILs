#include <iostream>
using namespace std;

int arr[102][102]={0,};
int dr[4]={0,1,0,-1};
int dc[4]={1,0,-1,0};

int main() {
    int n,m;
    cin>>n>>m;

    for(int i=0;i<m+2;i++){
        arr[0][i]=1;
        arr[n+1][i]=1;
    }
    for(int i=0;i<n+2;i++){
        arr[i][0]=1;
        arr[i][m+1]=1;
    }

    int dir=0;
    int curr=1;
    int curc=1;
    arr[1][1]=1;
    int cnt=0;
    for(int i=2;i<n*m+1;i++){
        if(arr[curr+dr[dir]][curc+dc[dir]]!=0){
            dir=(dir+1)%4;
        }
        curr+=dr[dir];
        curc+=dc[dir];
        arr[curr][curc]=i;
    }

    for(int r=1;r<n+1;r++){
        for(int c=1;c<m+1;c++){
            cout<<arr[r][c]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}