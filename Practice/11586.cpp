#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int main(){
  int t, cm = 0, cf = 0;
  string gender, r;
  cin >> t;
  cin.ignore();
  while(t--){
    getline(cin, gender);
    gender.erase(remove(gender.begin(), gender.end(), ' '), gender.end());
    for (int n = 0; n < gender.size(); n++){
      if (gender.at(n) == 'M') cm++;
      else if (gender.at(n) == 'F') cf++;
    }
    r = (cm == cf && gender.size() > 2) ? "LOOP" : "NO LOOP";
    cm = 0;
    cf = 0;
    cout << r << endl;
  }
  return 0;
}
