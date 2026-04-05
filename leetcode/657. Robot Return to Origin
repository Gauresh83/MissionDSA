class Solution {
public:
    static bool judgeCircle(string& moves) {
        int balanced=0;
        for(char c: moves){
            balanced+=(c=='R')-(c=='L');
            balanced+=((c=='U')-(c=='D'))<<15;
        }
        return balanced==0;
    }
};
