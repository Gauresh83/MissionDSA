class Solution {
public:
    int numberOfWays(string& corridor) {
        const long long mod=1e9+7;
        int n=corridor.rfind('S'), count=1;
        if (n<1) return 0;
        int seat[2]={-1, -1};
        seat[0]=corridor.find('S');

        if (seat[0]==-1) return 0;

        long long ans=1;

        for(int i=seat[0]+1; i<=n; i++){
            if (corridor[i]=='S'){
                seat[count&1]=i;
                if ((count&1)==0) {
                //    cout<<"d="<<i-seat[1]<<endl;
                    ans=(ans*(i-seat[1])%mod);
                }
                count++;
            }     
        }
        if (count&1) return 0;
        return ans;
    }
};
auto init = []()
{ 
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();
