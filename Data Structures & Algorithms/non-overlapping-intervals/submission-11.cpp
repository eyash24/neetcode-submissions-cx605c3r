class Solution {
public:
    int solve(int idx, int r, vector<vector<int>>& ivl,int n){
        if(idx >= n) return 0;
        int a = 1 + solve(idx+1,r,ivl,n); 
        int b= INT_MAX;
        if(ivl[idx][0] >= r){
            b = solve(idx+1,ivl[idx][1],ivl,n);
        }

        return min(a,b);
    }
    int eraseOverlapIntervals(vector<vector<int>>& ivl) {
        sort(ivl.begin(),ivl.end());

        int n = ivl.size();

        return solve(0,INT_MIN,ivl,n);
        
    }
};
