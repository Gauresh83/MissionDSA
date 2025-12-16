const int N=161 ,N4=161*4;
int profit[N][2];
vector<int> children[N];
int dp[N][2][2][N]; // node, bossBuy, buy, budget
bitset<N4> vis=0; // visit for (node, bossBuy,  buy)  

class Solution {
public:
    int n;

    void build_tree(const vector<vector<int>>& hierarchy) {
        for (int i=0; i<n; i++) children[i].clear();
        for (auto& e : hierarchy)
            children[e[0]-1].push_back(e[1]-1);
    }

    void dfs(int node, bool bossBuy, bool buy, int budget,
             const vector<int>& present) {

        if (vis[(node<<2)|(bossBuy<<1)|buy]) return;
        vis[(node<<2)|(bossBuy<<1)|buy]=1;

        int* cache=dp[node][bossBuy][buy];
        fill(cache, cache+budget+1, INT_MIN);

        int cost=buy?(bossBuy?present[node]/2:present[node]):0;
        if (cost<=budget)
            cache[cost]=buy?profit[node][bossBuy]:0;

        int* cur=(int*)alloca(sizeof(int)*(budget+1));
        int* merged=(int*)alloca(sizeof(int)*(budget+1));
        memcpy(cur, cache, sizeof(int)*(budget+1));

        for (int child : children[node]) {
            dfs(child, buy, 1, budget, present);
            dfs(child, 0, 0, budget, present);

            int* take=dp[child][buy][1];
            int* skip=dp[child][0][0];

            fill(merged, merged+budget+1, INT_MIN);

            for (int b=0; b<=budget; b++) if (cur[b]!=INT_MIN) {
                for (int x=0; b+x <= budget; x++) {
                    int best=max(take[x], skip[x]);
                    if (best!=INT_MIN)
                        merged[b+x]=max(merged[b+x], cur[b]+best);
                }
            }
            memcpy(cur, merged, sizeof(int)*(budget+1));
        }
        memcpy(cache, cur, sizeof(int)*(budget+1));
    }

    int maxProfit(int n, vector<int>& present, vector<int>& future,
                  vector<vector<int>>& hierarchy, int budget) {
        this->n=n;
        vis.reset();

        for (int i=0; i<n; i++) {
            profit[i][0]=future[i]-present[i];
            profit[i][1]=future[i]-present[i]/2;
        }

        build_tree(hierarchy);

        // root buys or does not buy
        dfs(0, 0, 0, budget, present);
        dfs(0, 0, 1, budget, present);

        int ans=0;
        for (int b=0; b<=budget; b++) {
            ans=max(ans, dp[0][0][0][b]);
            ans=max(ans, dp[0][0][1][b]);
        }
        return ans;
    }
};
