#include <iostream>
using namespace std;

int n;
int top_row[201];
int bottom_row[201];

void turn(int t){
    for(int i=0;i<(t%(2*n));i++){
        int temp1=top_row[n-1];
        for(int tr=n-1;tr>0;tr--){
            top_row[tr]=top_row[tr-1];
        }
        int temp2=bottom_row[n-1];
        for(int br=n-1;br>0;br--){
            bottom_row[br]=bottom_row[br-1];
        }
        top_row[0]=temp2;
        bottom_row[0]=temp1;
    }
}

int main() {
    int t;
    cin>>n>>t;
    for(int tr=0;tr<n;tr++){
        cin>>top_row[tr];
    }
    for(int br=0;br<n;br++){
        cin>>bottom_row[br];
    }
    turn(t);
    for(int tr=0;tr<n;tr++){
        cout<<top_row[tr]<<" ";
    }
    cout<<"\n";
    for(int br=0;br<n;br++){
        cout<<bottom_row[br]<<" ";
    }
    return 0;
}