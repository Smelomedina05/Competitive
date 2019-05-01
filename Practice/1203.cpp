#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

struct Registry{
  int qnum;
  int period;
  bool operator<(const Registry& a) const {
    return qnum < a.qnum;
  }
};

int main(){
  Registry r;
  vector<Registry> rs;
  //vector<int> rsp;
  int k, counter = 0, stable = 1;
  string name;
  cin >> name;
  while (name != "#"){
    cin >> r.qnum >> r.period;
    rs.push_back(r);
    //rsp.push_back(r.period);
    cin >> name;
  }
  sort(rs.begin(), rs.end());
  //sort(rsp.begin(), rsp.end());
  cin >> k;
  while (counter < k){
    for (int n = 0; n < rs.size(); n++){
      if (stable%rs.at(n).period == 0){
        cout << rs.at(n).qnum << endl;
        counter++;
        if (counter >= k) return 0;
      }
    }
    stable++;
  }
  return 0;
}
