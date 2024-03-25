#include <iostream>

using namespace std;

int main() {
    
    int dx[4]={0,1,0,-1};
    int dy[4]={1,0,-1,0};
    pair<int,int> cur={0,0};
    int n;
    cin>>n;
    char dir=' ';
    int dis, dirn;
    for(int i=0; i<n;i++){
        cin>>dir>>dis;
        if(dir=='N') dirn=0;
        else if(dir=='E') dirn=1;
        else if(dir=='S') dirn=2;
        else dirn=3;
        cur.first += dx[dirn]*dis;
        cur.second += dy[dirn]*dis;
    }
    cout<<cur.first<<" "<<cur.second;
    return 0;
}