class Solution {
public:
	int findSmallestInteger(vector<int>& nums, int v) {
		long long n = nums.size(), x, res = 0;
		vector<int> rem(v, 0);
		for (int i = 0; i < n; i++) {
			x = ((nums[i] % v) + v) % v;
			rem[x]++;
		}

		while (rem[res % v]--) res++;
		return res;
	}
};
