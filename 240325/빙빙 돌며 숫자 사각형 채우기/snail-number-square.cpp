#include <iostream>
using namespace std;
int main() {
    int dr[4]={-1,0,1,0};
    int dc[4]={0,1,0,-1};
    
    int arr[101][101]={0,};
    int n,m;

    cin>>n>>m;
    for(int i=0;i<m+1;i++){
        arr[0][i]=1;
        arr[n+1][i]=1;
    }
    for(int i=0;i<n+1;i++){
        arr[i][0]=1;
        arr[i][m+1]=1;
    }

    int dir=1;
    int c=1;
    int r=1;

    arr[1][1]=1;
    for(int i=2;i<n*m+1;i++){
        if(arr[r+dr[dir]][c+dc[dir]]!=0){
            dir=(dir+1)%4;
        }
        if(arr[r+dr[dir]][c+dc[dir]]!=0){
            break;
        }
        c+=dc[dir];
        r+=dr[dir];
        arr[r][c]=i;
    }
    for(int i=1;i<n+1;i++){
        for(int j=1;j<m+1;j++){
            cout<<arr[i][j]<<" ";
        }
        cout<<"\n";
    }
    return 0;
}