class Solution {
public:
    int numberOfSubstrings(string s) {
        int n = s.size();
        int ans = 0;
        vector<int> count(3, 0);  // Count for 'a', 'b', and 'c'
        int left = 0;  // Left pointer of the window

        // Iterate through the string with the right pointer
        for (int right = 0; right < n; right++) {
            // Update the count of the current character
            count[s[right] - 'a']++;

            // Check if the current window contains at least one 'a', 'b', and 'c'
            while (count[0] > 0 && count[1] > 0 && count[2] > 0) {
                // Count all valid substrings from 'left' to 'right'
                ans += (n - right);

                // Move the left pointer to reduce the window size
                count[s[left] - 'a']--;
                left++;
            }
        }

        return ans;
    }
};
