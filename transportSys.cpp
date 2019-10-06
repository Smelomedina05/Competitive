#include<iostream>
#include<vector>
#include<cmath>
#include<tuple>
#include<algorithm>
using namespace std;

#define print(case, a, b, c) cout << "Case #" << case << ": " << a << " " << b << " " << c << endl;
#define full(arr, size) arr.clear(); for (int n = 0; n < size; n++) arr.push_back(n);

typedef tuple<int, int> cord;
typedef tuple<double, int, int> arc;
typedef tuple<int, double, double> res;

vector<int> parents;

int find(int n){
  int result;
  if (n == parents[n]){
    result = n;
  } else {
    result = find(parents[n]);
    parents[n] = result;
  }
  return result;
}

res kruskal(vector<arc> G, vector<cord> nodes, int r){
  sort(G.begin(), G.end());
  full(parents, nodes.size());
  int states = 1;
  double roads = 0.0, rails = 0.0;
  for (arc wuv : G){
    if (find(get<1>(wuv)) != find(get<2>(wuv))){
      parents[find(get<2>(wuv))] = find(get<1>(wuv));
      if (get<0>(wuv) > r){
        states++;
        rails += get<0>(wuv);
      } else {
        roads += get<0>(wuv);
      }
    }
  }
  return res(states, roads, rails);
}

double distance(cord a, cord b){
  return sqrt(pow((get<0>(b)-get<0>(a)), 2)+pow((get<1>(b)-get<1>(a)), 2));
}

int main(){
  int cases, cs = 1, nds, r;
  int x, y;
  vector<cord> nodes;
  vector<arc> G;
  cin >> cases;
  while (cin >> nds >> r){
    for (int n = 0; n < nds; n++){
      cin >> x >> y;
      nodes.push_back(cord(x,y));
    }
    for (int u = 0; u < nds; u++){
      for (int v = u+1; v < nds; v++){
        G.push_back(arc(distance(nodes[u], nodes[v]), u, v));
      }
    }
    res result = kruskal(G, nodes, r);
    print(cs, get<0>(result), round(get<1>(result)), round(get<2>(result)));
    G.clear();
    nodes.clear();
    cs++;
  }
  return 0;
}
