///10687-Amazon UVa
///Santiago Melo Medina

#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
using namespace std;

struct Station {
  int x;
  int y;
};

struct Path {
  float dist;
  int x, y;
  int v;
  void set(float d, int xx, int yy, int vv){
    dist = d, x = xx, y = yy, v = vv;
  }
  bool operator<(Path p2){
    if (dist != p2.dist) return dist < p2.dist;
    else if (x != p2.x) return x < p2.x;
    else return y > p2.y;
  }
};

vector<Station> V;
vector<vector<int>> G;
vector<int> visited;
int counter;

void dfs(int u){
  visited[u] = 1;
  counter++;
  for (int v = 0; v < G[u].size(); v++){
    int node = G[u][v];
    if (!visited[node]){
      dfs(node);
    }
  }
}

float distance(Station s1, Station s2){
  int x1 = s1.x, x2 = s2.x;
  int y1 = s1.y, y2 = s2.y;
  return sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1));
}

void graph(int nodes){
  vector<Path> dists[nodes];
  for (int u = 0; u < nodes; u++){
    for (int v = u+1; v < nodes; v++){
      Path up, vp;
      up.set(distance(V[u], V[v]), V[v].x, V[v].y, v);
      vp.set(distance(V[u], V[v]), V[u].x, V[u].y, u);
      dists[u].push_back(up); dists[v].push_back(vp);
    }
  }
  for (int u = 0; u < nodes; u++){
    sort(dists[u].begin(), dists[u].end());
    vector<int> tmp;
    for (int v = 0; v < 2; v++){
      if (v < dists[u].size()) tmp.push_back(dists[u][v].v);
    }
    G.push_back(tmp);
    tmp.clear();
  }
}

int main(){
  int nodes;
  Station tmp;
  while (cin >> nodes){
    if (nodes){
      for (int n = 0; n < nodes; n++){
        cin >> tmp.x, cin >> tmp.y;
        V.push_back(tmp);
      }
      graph(nodes);
      counter = 0;
      visited.clear();
      for (int n = 0; n < nodes; n++){
        visited.push_back(0);
      }
      dfs(0);
      if (counter == nodes) cout << "All stations are reachable." << endl;
      else cout << "There are stations that are unreachable." << endl;
      V.clear();
      G.clear();
    }
  }
  return 0;
}
