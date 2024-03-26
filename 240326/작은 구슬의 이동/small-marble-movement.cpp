#include <iostream>
using namespace std;

int dr[4]={0,1,0,-1};
int dc[4]={1,0,-1,0};

bool arr[52][52]={0,};

bool isRange(int x, int y, int n){
    return (x>0&&x<n+1&&y>0&&y<n+1);
}

int main() {
    int n,t,r,c,dir;
    char d;
    cin>>n>>t>>r>>c>>d;

    if(d=='R') dir=0;
    else if (d=='D') dir=1;
    else if (d=='L') dir=2;
    else dir=3;

    while(t--){
        if(isRange(r+dr[dir],c+dc[dir],n)){
            r+=dr[dir];
            c+=dc[dir];
        }
        else{
            dir=(dir+2)%4;
        }
    }

    cout<<r<<" "<<c;

    return 0;
}