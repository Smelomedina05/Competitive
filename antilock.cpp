#include<iostream>
#include<vector>
#include<tuple>
#include<algorithm>
#include<limits>
#include<map>
using namespace std;

#define full(arr, size) arr.clear(); for(int n = 0; n < size; n++) arr.push_back(n);

typedef tuple<int, int, int, int> node;
typedef tuple<int, int, int> arc;

vector<int> parents;

int weight(int a, int b){
  int maxm = max(a,b), minm = min(a,b);
  return min(maxm-minm, minm+10-maxm);
}

int distance(node u, node v){
  int result = weight(get<0>(u), get<0>(v));
  result += weight(get<1>(u), get<1>(v));
  result += weight(get<2>(u), get<2>(v));
  result += weight(get<3>(u), get<3>(v));
  return result;
}

int find(int n){
  int result = 0;
  if (n == parents[n]){
    result = n;
  } else {
    result = find(parents[n]);
    parents[n] = result;
  }
  return result;
}

int kruskal(vector<arc> G, vector<node> nodes){
  sort(G.begin(), G.end());
  full(parents, nodes.size());
  int result = numeric_limits<int>::max();
  for (node nd:nodes){
    result = min(result, distance(node(0,0,0,0), nd));
  }
  for (arc wuv : G){
    if (find(get<1>(wuv)) != find(get<2>(wuv))){
      parents[find(get<2>(wuv))] = find(get<1>(wuv));
      result += get<0>(wuv);
    }
  }
  return result;
}

node numToNode(int num){
  int nums[] = {(num-num%1000)/1000%10, (num-num%100)/100%10, (num-num%10)/10%10, num%10};
  return node(nums[0], nums[1], nums[2], nums[3]);
}

int main(){
  int cases, n, tmp;
  vector<node> nodes;
  vector<arc> G;
  node node_tmp;
  cin >> cases;
  while (cin >> n){
    for (int s = 0; s < n; s++){
      cin >> tmp;
      node_tmp = numToNode(tmp);
      nodes.push_back(node_tmp);
    }
    for (int u = 0; u < n; u++){
      for (int v = u+1; v < n; v++){
        G.push_back(arc(distance(nodes[u], nodes[v]), u, v));
      }
    }
    cout << kruskal(G, nodes) << endl;
    G.clear();
    nodes.clear();
  }
  return 0;
}
