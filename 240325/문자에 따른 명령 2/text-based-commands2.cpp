#include <iostream>
using namespace std;
int main() {
    int dx[4]={0,1,0,-1};
    int dy[4]={1,0,-1,0};
    
    pair<int,int> cur={0,0};
    string com;
    cin>>com;
    int dir=0;
    for(int i=0;i<com.length();i++){
        
        if(com[i]=='L'){
            dir=(dir+3)%4;
        }
        else if(com[i]=='R'){
            dir=(dir+1)%4;
        }
        else{
            cur.first += dx[dir];
            cur.second += dy[dir];
        }
    }
    cout<<cur.first<<" "<<cur.second;
    return 0;
}