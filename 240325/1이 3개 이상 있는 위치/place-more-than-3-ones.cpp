#include <iostream>
using namespace std;
int main() {
    int dx[4]={0,1,0,-1};
    int dy[4]={1,0,-1,0};
    bool arr[101][101]={0,};
    int n;
    cin>>n;
    int a;
    for(int i=1;i<n+1;i++){
        for(int j=1;j<n+1;j++){
            cin>>a;
            if(a==1){
                arr[j][i]=1;
            }
        }
    }
    int cnt=0;
    for(int i=1;i<n+1;i++){
        for(int j=1;j<n+1;j++){
            int tempCnt=0;
            for(int k=0;k<4;k++){
                if(arr[j+dx[k]][i+dy[k]]==1){
                    tempCnt++;
                }
            }
            if(tempCnt>=3){
                cnt++;
            }
        }
    }
    cout<<cnt;

    return 0;
}