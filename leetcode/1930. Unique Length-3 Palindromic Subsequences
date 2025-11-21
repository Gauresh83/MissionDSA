int n;
int ll[26], rr[26];
class Solution {
public:
    static inline void find_ll_rr(string& s){
        fill(ll, ll+26, n);
        memset(rr, -1, sizeof(rr));
        
        for(unsigned i=0; i<n; i++){
            unsigned x=s[i]-'a';
            if (ll[x]==n){
                ll[x]=i;
            }
            rr[x]=i;
        }
    }

    static inline void find_ll_rr_2(string& s){
        fill(ll, ll+26, n);
        memset(rr, -1, sizeof(rr));
    
        int seen=0;
        
        for(unsigned i=0; i<n && seen<26; i++){
            unsigned x=s[i]-'a';
            if (ll[x]==n){
                ll[x]=i;
                seen++;
            }
        }
    
        for(unsigned i=n-1; i>=0 && seen>0; i--){
            unsigned x=s[i]-'a';
            if (rr[x]==-1){
                rr[x]=i;
                seen--;
            }
        }
    }

    static inline int hasPal3(char x,  string& s, int l, int r){
        unsigned m;
        bitset<26> seen=0;

        for(m=l+1; m<r; m++){
            seen[s[m]-'a']=1;
        } 
        return seen.count();
    }

    static int countPalindromicSubsequence(string& s) {
        n=s.size();
        find_ll_rr(s);
        int count=0;
    
        for(char x='a'; x<='z'; x++){
            int l=ll[x-'a'], r=rr[x-'a'];
            if (l+1>=r) continue;
            count+=hasPal3(x, s, l, r);
        }   
        return count;
    }
};


auto init = []()
{ 
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
    return 'c';
}();
