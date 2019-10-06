#include<iostream>
#include<vector>
using namespace std;

struct Par{
  int u, v, people;
  void set(int un, int vn, int npeople){
    u = un;
    v = vn;
    people = npeople;
  }
};

#define clean(arr, size) for (int n = 0; n < size; n++) arr[n] = 0;

vector<int> S(20, 0);
vector<Par> A;
int limit, maximum;

bool check(int u, int v, int people){
  bool result = true;
  while (u<v && result){
    result = result && (S[u]+people <= limit);
    u++;
  }
  return result;
}

void travel(int n, int acum){
  maximum = max(maximum, acum);
  int u;
  while (n < A.size()){
    if (check(A[n].u, A[n].v, A[n].people)){
      u = A[n].u;
      while (u < A[n].v){ S[u]+= A[n].people; u++;}
      travel(n+1, acum+A[n].people*(A[n].v-A[n].u));
      u = A[n].u;
      while (u < A[n].v){ S[u]-= A[n].people; u++;}
    }
    n++;
  }
}

int main(){
  int destination, orders;
  Par tmp;
  while (cin >> limit >> destination >> orders){
    if (limit || destination || orders){
      maximum = 0;
      while (orders--){
        cin >> tmp.u >> tmp.v >> tmp.people;
        A.push_back(tmp);
      }
      travel(0,0);
      cout << maximum << endl;
      A.clear();
      clean(S, S.size());
    }
  }
}
