#include <bits/stdc++.h>
using namespace std;

struct Student{int r; string n; float m;};

int main(){
    Student s[10]={{101,"Alice",85},{102,"Bob",78},{103,"Charlie",92},{104,"David",66},
                   {105,"Eva",88},{106,"Frank",74},{107,"Grace",81},{108,"Hannah",90},
                   {109,"Ian",69},{110,"Jane",95}};
                   for(int i=0;i<10;i++){
        cout<<"\t"<<s[i].r<<"\t"<<s[i].n<<"\t"<<s[i].m<<"\n";
    }
    sort(s,s+10,[](Student a, Student b){return a.r<b.r;}); // sort by roll no

    int k; cout<<"Enter roll no: "; cin>>k;
    int l=0,r=9;
    while(l<=r){
        int m=(l+r)/2;
        if(s[m].r==k){cout<<s[m].r<<" "<<s[m].n<<" "<<s[m].m; return 0;}
        else if(s[m].r<k) l=m+1;
        else r=m-1;
    }
    cout<<"Not found";
}
