#include <bits/stdc++.h>
using namespace std;

struct Student{int r; string n; float m;};

int main(){
    Student s[10]={{101,"Alice",85},{102,"Bob",78},{103,"Charlie",92},{104,"David",66},
                   {105,"Eva",88},{106,"Frank",74},{107,"Grace",81},{108,"Hannah",90},
                   {109,"Ian",69},{110,"Jane",95}};
                   for(int i = 0; i < 10; i++) {
    cout << s[i].r << " " << s[i].n << " " << s[i].m << endl;
}
    int k; cout<<"Enter roll no: "; cin>>k;

    // Linear Search
    for(int i=0;i<10;i++)
        if(s[i].r==k){cout<<s[i].r<<" "<<s[i].n<<" "<<s[i].m; return 0;}
    cout<<"Not found";
}
